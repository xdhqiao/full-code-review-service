from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any

from .config import CodexConfig
from .models import CodeFile, FileReview, ReviewIssue
from .prompt import FILE_REVIEW_SCHEMA, build_file_review_prompt


class ReviewError(RuntimeError):
    pass


class BaseReviewer(ABC):
    @abstractmethod
    def review_file(self, repo_path: Path, project_name: str, code_file: CodeFile) -> FileReview:
        raise NotImplementedError


def make_reviewer(config: CodexConfig) -> BaseReviewer:
    if config.mode == "sdk":
        return CodexSdkReviewer(config)
    if config.mode == "cli":
        return CodexCliReviewer(config)
    if config.mode == "mock":
        return MockReviewer()
    raise ValueError(f"Unsupported reviewer mode: {config.mode}")


class CodexSdkReviewer(BaseReviewer):
    def __init__(self, config: CodexConfig):
        self.config = config

    def review_file(self, repo_path: Path, project_name: str, code_file: CodeFile) -> FileReview:
        prompt = build_file_review_prompt(project_name, code_file)
        try:
            from openai_codex import Codex, Sandbox
        except ImportError as exc:
            raise ReviewError(
                "openai-codex is not installed. Run `pip install openai-codex` "
                "or set codex.mode to `cli` when a Codex CLI is already installed."
            ) from exc

        sandbox = getattr(Sandbox, self.config.sandbox, Sandbox.read_only)
        old_cwd = Path.cwd()
        os.chdir(repo_path)
        try:
            with Codex() as codex:
                kwargs: dict[str, Any] = {"sandbox": sandbox}
                if self.config.model:
                    kwargs["model"] = self.config.model
                thread = codex.thread_start(**kwargs)
                result = thread.run(prompt, sandbox=sandbox)
                raw = getattr(result, "final_response", str(result))
        finally:
            os.chdir(old_cwd)

        return parse_file_review(raw, code_file, reviewer="codex-sdk")


class CodexCliReviewer(BaseReviewer):
    def __init__(self, config: CodexConfig):
        self.config = config

    def review_file(self, repo_path: Path, project_name: str, code_file: CodeFile) -> FileReview:
        prompt = build_file_review_prompt(project_name, code_file)
        with tempfile.NamedTemporaryFile("w", suffix=".schema.json", encoding="utf-8", delete=False) as fp:
            json.dump(FILE_REVIEW_SCHEMA, fp)
            schema_path = fp.name

        try:
            command = [
                self.config.cli_bin,
                "exec",
                "--ephemeral",
                "--sandbox",
                "read-only",
                "--output-schema",
                schema_path,
            ]
            if self.config.model:
                command.extend(["--model", self.config.model])
            command.append(prompt)

            completed = subprocess.run(
                command,
                cwd=repo_path,
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=self.config.timeout_seconds,
            )
            return parse_file_review(completed.stdout, code_file, reviewer="codex-cli")
        except (subprocess.SubprocessError, FileNotFoundError) as exc:
            raise ReviewError(f"Codex CLI review failed for {code_file.path}: {exc}") from exc
        finally:
            Path(schema_path).unlink(missing_ok=True)


class MockReviewer(BaseReviewer):
    def review_file(self, repo_path: Path, project_name: str, code_file: CodeFile) -> FileReview:
        return FileReview(
            path=code_file.path,
            language=code_file.language,
            overall_comment="Mock review result for local tests.",
            score=100,
            issues=[],
            reviewer="mock",
        )


def parse_file_review(raw: str, code_file: CodeFile, reviewer: str) -> FileReview:
    data = _extract_json_object(raw)
    path = str(data.get("path") or code_file.path)
    language = str(data.get("language") or code_file.language)
    score = _clamp_int(data.get("score", 0), 0, 100)
    overall = str(data.get("overall_comment") or "模型未提供总体评语。")
    issues = [_normalise_issue(item, code_file) for item in data.get("issues", []) if isinstance(item, dict)]
    return FileReview(
        path=path,
        language=language,
        overall_comment=overall,
        score=score,
        issues=issues,
        reviewer=reviewer,
    )


def _normalise_issue(item: dict[str, Any], code_file: CodeFile) -> ReviewIssue:
    max_line = max(1, len(code_file.content.splitlines()))
    line_start = _clamp_int(item.get("line_start", 1), 1, max_line)
    line_end = _clamp_int(item.get("line_end", line_start), line_start, max_line)
    severity = str(item.get("severity", "medium")).lower()
    if severity not in {"critical", "high", "medium", "low", "info"}:
        severity = "medium"
    return ReviewIssue(
        type=str(item.get("type", "quality")),
        severity=severity,
        line_start=line_start,
        line_end=line_end,
        description=str(item.get("description", "")),
        fix=str(item.get("fix", "")),
        confidence=_clamp_float(item.get("confidence", 0.0), 0.0, 1.0),
    )


def _extract_json_object(raw: str) -> dict[str, Any]:
    text = raw.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start < 0 or end < start:
            raise ReviewError("Reviewer did not return a JSON object")
        parsed = json.loads(text[start : end + 1])
    if not isinstance(parsed, dict):
        raise ReviewError("Reviewer JSON root must be an object")
    return parsed


def _clamp_int(value: Any, low: int, high: int) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError):
        number = low
    return max(low, min(high, number))


def _clamp_float(value: Any, low: float, high: float) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        number = low
    return max(low, min(high, number))

