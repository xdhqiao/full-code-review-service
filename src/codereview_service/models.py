from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CodeFile:
    path: str
    language: str
    content: str
    sha256: str
    size_bytes: int


@dataclass
class ReviewIssue:
    type: str
    severity: str
    line_start: int
    line_end: int
    description: str
    fix: str
    confidence: float = 0.0


@dataclass
class FileReview:
    path: str
    language: str
    overall_comment: str
    score: int
    issues: list[ReviewIssue] = field(default_factory=list)
    reviewer: str = "codex"


@dataclass
class ProjectReviewPayload:
    task_id: str
    project_id: str
    project_name: str
    repository_path: str
    revision: str
    review_type: str
    started_at: str
    finished_at: str
    files: list[FileReview]
    aggregate: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def stable_task_id(project_id: str, revision: str) -> str:
    raw = f"{project_id}:{revision}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:32]


LANGUAGE_BY_SUFFIX = {
    ".py": "python",
    ".js": "javascript",
    ".jsx": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".java": "java",
    ".go": "go",
    ".rs": "rust",
    ".c": "c",
    ".h": "c",
    ".cpp": "cpp",
    ".hpp": "cpp",
    ".cs": "csharp",
    ".php": "php",
    ".rb": "ruby",
    ".kt": "kotlin",
    ".swift": "swift",
    ".scala": "scala",
    ".sql": "sql",
    ".sh": "shell",
    ".ps1": "powershell",
    ".yml": "yaml",
    ".yaml": "yaml",
    ".json": "json",
    ".toml": "toml",
}


def detect_language(path: str) -> str:
    return LANGUAGE_BY_SUFFIX.get(Path(path).suffix.lower(), "text")


def codefile_from_bytes(path: str, data: bytes) -> CodeFile:
    return CodeFile(
        path=path,
        language=detect_language(path),
        content=data.decode("utf-8", errors="replace"),
        sha256=hashlib.sha256(data).hexdigest(),
        size_bytes=len(data),
    )

