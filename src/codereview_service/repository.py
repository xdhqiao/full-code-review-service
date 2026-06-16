from __future__ import annotations

import fnmatch
import subprocess
from pathlib import Path

from .config import ProjectConfig
from .models import CodeFile, codefile_from_bytes


def run_git(repo_path: Path, args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_path,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
    )
    return result.stdout.strip()


def get_revision(repo_path: Path) -> str:
    try:
        return run_git(repo_path, ["rev-parse", "HEAD"])
    except (subprocess.SubprocessError, FileNotFoundError):
        return "nogit-" + str(int(repo_path.stat().st_mtime))


def _normalise_rel(path: Path | str) -> str:
    return str(path).replace("\\", "/").lstrip("./")


def _matches(path: str, patterns: list[str]) -> bool:
    for pattern in patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
        if pattern.startswith("**/") and fnmatch.fnmatch(path, pattern[3:]):
            return True
    return False


def _git_files(repo_path: Path) -> list[str]:
    try:
        output = run_git(repo_path, ["ls-files", "-z"])
    except (subprocess.SubprocessError, FileNotFoundError):
        return []
    return [item for item in output.split("\0") if item]


def _walk_files(repo_path: Path) -> list[str]:
    files: list[str] = []
    for path in repo_path.rglob("*"):
        if path.is_file():
            files.append(_normalise_rel(path.relative_to(repo_path)))
    return files


def list_reviewable_paths(project: ProjectConfig, max_files: int) -> list[str]:
    repo_path = Path(project.path)
    candidates = _git_files(repo_path) or _walk_files(repo_path)
    selected: list[str] = []

    for raw_path in sorted(candidates):
        rel_path = _normalise_rel(raw_path)
        if not _matches(rel_path, project.include_globs):
            continue
        if _matches(rel_path, project.exclude_globs):
            continue
        selected.append(rel_path)
        if len(selected) >= max_files:
            break

    return selected


def is_binary(data: bytes) -> bool:
    if b"\0" in data:
        return True
    sample = data[:4096]
    if not sample:
        return False
    control_count = sum(1 for b in sample if b < 9 or (13 < b < 32))
    return control_count / len(sample) > 0.20


def read_code_file(repo_path: Path, rel_path: str, max_file_bytes: int) -> CodeFile | None:
    full_path = (repo_path / rel_path).resolve()
    if not full_path.is_file():
        return None
    data = full_path.read_bytes()
    if len(data) > max_file_bytes or is_binary(data):
        return None
    return codefile_from_bytes(rel_path, data)
