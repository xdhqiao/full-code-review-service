import json
import unittest

from codereview_service.config import load_config


class ConfigTest(unittest.TestCase):
    def test_load_config(self):
        from tempfile import TemporaryDirectory
        from pathlib import Path

        with TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            path = tmp_path / "projects.json"
            path.write_text(
                json.dumps(
                    {
                        "scanner": {"interval_seconds": 10},
                        "codex": {"mode": "mock"},
                        "projects": [{"id": "p1", "name": "Project 1", "path": str(tmp_path)}],
                    }
                ),
                encoding="utf-8",
            )

            config = load_config(path)

            self.assertEqual(config.scanner.interval_seconds, 10)
            self.assertEqual(config.codex.mode, "mock")
            self.assertEqual(config.projects[0].id, "p1")
