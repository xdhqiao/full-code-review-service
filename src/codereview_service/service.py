from __future__ import annotations

import logging
import os
import time
from pathlib import Path

from .config import AppConfig, ProjectConfig, load_config
from .models import FileReview, ProjectReviewPayload, stable_task_id, utc_now_iso
from .poster import ResultPoster
from .repository import get_revision, list_reviewable_paths, read_code_file
from .reviewer import BaseReviewer, ReviewError, make_reviewer
from .state import ReviewState


logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
LOGGER = logging.getLogger(__name__)


class FullCodeReviewService:
    def __init__(
        self,
        config: AppConfig,
        reviewer: BaseReviewer | None = None,
        poster: ResultPoster | None = None,
    ):
        self.config = config
        self.reviewer = reviewer or make_reviewer(config.codex)
        self.poster = poster or ResultPoster(
            config.scanner.post_result_url,
            config.scanner.post_timeout_seconds,
        )
        self.state = ReviewState.load(config.scanner.state_path)

    def run_forever(self) -> None:
        while True:
            self.run_once()
            if self.config.scanner.run_once:
                break
            time.sleep(self.config.scanner.interval_seconds)

    def run_once(self) -> None:
        for project in self.config.projects:
            if not project.enabled:
                LOGGER.info("Skip disabled project %s", project.id)
                continue
            try:
                self._review_project(project)
            except Exception:
                LOGGER.exception("Project review failed: %s", project.id)

    def _review_project(self, project: ProjectConfig) -> None:
        repo_path = Path(project.path)
        if not repo_path.exists():
            LOGGER.warning("Project path does not exist: %s", project.path)
            return

        revision = get_revision(repo_path)
        if self.state.is_reviewed(project.id, revision):
            LOGGER.info("Project %s revision %s already reviewed", project.id, revision)
            return

        started_at = utc_now_iso()
        rel_paths = list_reviewable_paths(project, self.config.scanner.max_files_per_project)
        LOGGER.info("Reviewing project=%s revision=%s files=%d", project.id, revision, len(rel_paths))

        file_reviews: list[FileReview] = []
        for rel_path in rel_paths:
            code_file = read_code_file(repo_path, rel_path, self.config.scanner.max_file_bytes)
            if code_file is None:
                continue
            try:
                file_reviews.append(self.reviewer.review_file(repo_path, project.name, code_file))
            except ReviewError as exc:
                LOGGER.error("Review failed for %s/%s: %s", project.id, rel_path, exc)
                file_reviews.append(
                    FileReview(
                        path=code_file.path,
                        language=code_file.language,
                        overall_comment=f"Codex review failed: {exc}",
                        score=0,
                        issues=[],
                        reviewer="error",
                    )
                )

        payload = ProjectReviewPayload(
            task_id=stable_task_id(project.id, revision),
            project_id=project.id,
            project_name=project.name,
            repository_path=str(repo_path),
            revision=revision,
            review_type="full",
            started_at=started_at,
            finished_at=utc_now_iso(),
            files=file_reviews,
            aggregate=aggregate_reviews(file_reviews),
        )
        self.poster.post(payload.to_dict())
        self.state.mark_reviewed(project.id, revision)
        self.state.save(self.config.scanner.state_path)


def aggregate_reviews(files: list[FileReview]) -> dict[str, int | bool | float]:
    if not files:
        return {
            "overall_score": 0,
            "blocking": False,
            "critical_count": 0,
            "high_count": 0,
            "medium_count": 0,
            "low_count": 0,
            "info_count": 0,
            "file_count": 0,
        }
    counts = {"critical": 0, "high": 0, "medium": 0, "low": 0, "info": 0}
    for file_review in files:
        for issue in file_review.issues:
            counts[issue.severity] = counts.get(issue.severity, 0) + 1
    overall_score = round(sum(item.score for item in files) / len(files), 2)
    return {
        "overall_score": overall_score,
        "blocking": counts["critical"] > 0 or counts["high"] >= 3 or overall_score < 60,
        "critical_count": counts["critical"],
        "high_count": counts["high"],
        "medium_count": counts["medium"],
        "low_count": counts["low"],
        "info_count": counts["info"],
        "file_count": len(files),
    }


def main() -> None:
    config_path = os.environ.get("REVIEW_CONFIG_PATH", "/app/config/projects.json")
    service = FullCodeReviewService(load_config(config_path))
    service.run_forever()

