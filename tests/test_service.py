import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from codereview_service.config import AppConfig, CodexConfig, ProjectConfig, ScannerConfig
from codereview_service.models import FileReview, ReviewIssue
from codereview_service.reviewer import MockReviewer
from codereview_service.service import FullCodeReviewService, aggregate_reviews


class FakePoster:
    def __init__(self):
        self.payloads = []

    def post(self, payload):
        self.payloads.append(payload)


class ServiceTest(unittest.TestCase):
    def test_aggregate_reviews_blocks_on_high_issues(self):
        files = [
            FileReview(
                path="a.py",
                language="python",
                overall_comment="x",
                score=80,
                issues=[
                    ReviewIssue("security", "high", 1, 1, "d", "f"),
                    ReviewIssue("security", "high", 1, 1, "d", "f"),
                    ReviewIssue("security", "high", 1, 1, "d", "f"),
                ],
            )
        ]

        aggregate = aggregate_reviews(files)

        self.assertEqual(aggregate["overall_score"], 80)
        self.assertEqual(aggregate["high_count"], 3)
        self.assertIs(aggregate["blocking"], True)

    def test_service_scans_posts_and_updates_state(self):
        with TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            repo = root / "repo"
            repo.mkdir()
            (repo / "app.py").write_text("print('hello')\n", encoding="utf-8")
            state_path = root / "state.json"
            poster = FakePoster()
            config = AppConfig(
                scanner=ScannerConfig(
                    run_once=True,
                    state_path=str(state_path),
                    max_files_per_project=10,
                    post_result_url="http://example.test",
                ),
                codex=CodexConfig(mode="mock"),
                projects=[
                    ProjectConfig(
                        id="p1",
                        name="Project 1",
                        path=str(repo),
                        include_globs=["**/*.py"],
                        exclude_globs=[],
                    )
                ],
            )

            service = FullCodeReviewService(config, reviewer=MockReviewer(), poster=poster)
            service.run_once()

            self.assertEqual(len(poster.payloads), 1)
            self.assertEqual(poster.payloads[0]["project_id"], "p1")
            self.assertEqual(poster.payloads[0]["files"][0]["path"], "app.py")
            self.assertTrue(state_path.exists())
