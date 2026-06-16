from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


DEFAULT_EXCLUDES = [
    "**/.git/**",
    "**/node_modules/**",
    "**/dist/**",
    "**/build/**",
    "**/target/**",
    "**/.venv/**",
    "**/vendor/**",
]


@dataclass(frozen=True)
class ScannerConfig:
    interval_seconds: int = 3600
    run_once: bool = False
    state_path: str = "/app/state/review_state.json"
    post_result_url: str = "http://demo.api/save/codereview/result"
    post_timeout_seconds: int = 30
    max_files_per_project: int = 500
    max_file_bytes: int = 200_000
    review_unchanged_on_start: bool = True


@dataclass(frozen=True)
class CodexConfig:
    mode: str = "sdk"
    model: str | None = None
    sandbox: str = "read_only"
    timeout_seconds: int = 900
    cli_bin: str = "codex"
    reasoning_effort: str | None = None


@dataclass(frozen=True)
class ProjectConfig:
    id: str
    name: str
    path: str
    enabled: bool = True
    include_globs: list[str] = field(default_factory=lambda: ["**/*"])
    exclude_globs: list[str] = field(default_factory=lambda: list(DEFAULT_EXCLUDES))


@dataclass(frozen=True)
class AppConfig:
    scanner: ScannerConfig
    codex: CodexConfig
    projects: list[ProjectConfig]


def _require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} must be an object")
    return value


def load_config(path: str | os.PathLike[str]) -> AppConfig:
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as fp:
        raw = _require_mapping(json.load(fp), "root")

    scanner_raw = _require_mapping(raw.get("scanner", {}), "scanner")
    codex_raw = _require_mapping(raw.get("codex", {}), "codex")
    projects_raw = raw.get("projects", [])
    if not isinstance(projects_raw, list):
        raise ValueError("projects must be an array")

    scanner = ScannerConfig(**scanner_raw)
    codex = CodexConfig(**codex_raw)
    projects = [ProjectConfig(**_require_mapping(item, "project")) for item in projects_raw]

    if scanner.interval_seconds <= 0:
        raise ValueError("scanner.interval_seconds must be greater than 0")
    if scanner.max_files_per_project <= 0:
        raise ValueError("scanner.max_files_per_project must be greater than 0")
    if scanner.max_file_bytes <= 0:
        raise ValueError("scanner.max_file_bytes must be greater than 0")
    if codex.mode not in {"sdk", "cli", "mock"}:
        raise ValueError("codex.mode must be one of: sdk, cli, mock")

    return AppConfig(scanner=scanner, codex=codex, projects=projects)

