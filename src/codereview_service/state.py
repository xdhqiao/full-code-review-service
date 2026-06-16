from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ReviewState:
    projects: dict[str, str] = field(default_factory=dict)

    @classmethod
    def load(cls, path: str | Path) -> "ReviewState":
        state_path = Path(path)
        if not state_path.exists():
            return cls()
        with state_path.open("r", encoding="utf-8") as fp:
            raw = json.load(fp)
        projects = raw.get("projects", {})
        return cls(projects=projects if isinstance(projects, dict) else {})

    def save(self, path: str | Path) -> None:
        state_path = Path(path)
        state_path.parent.mkdir(parents=True, exist_ok=True)
        tmp_path = state_path.with_suffix(state_path.suffix + ".tmp")
        with tmp_path.open("w", encoding="utf-8") as fp:
            json.dump({"projects": self.projects}, fp, ensure_ascii=False, indent=2)
        tmp_path.replace(state_path)

    def is_reviewed(self, project_id: str, revision: str) -> bool:
        return self.projects.get(project_id) == revision

    def mark_reviewed(self, project_id: str, revision: str) -> None:
        self.projects[project_id] = revision

