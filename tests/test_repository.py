import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from codereview_service.config import ProjectConfig
from codereview_service.repository import is_binary, list_reviewable_paths, read_code_file


class RepositoryTest(unittest.TestCase):
    def test_binary_detection(self):
        self.assertTrue(is_binary(b"\x00\x01abc"))
        self.assertFalse(is_binary(b"print('hello')\n"))

    def test_list_and_read_files(self):
        with TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            (tmp_path / "src").mkdir()
            (tmp_path / "src" / "app.py").write_text("print('hello')\n", encoding="utf-8")
            (tmp_path / "node_modules").mkdir()
            (tmp_path / "node_modules" / "x.js").write_text("bad", encoding="utf-8")

            project = ProjectConfig(
                id="p1",
                name="Project 1",
                path=str(tmp_path),
                include_globs=["**/*.py", "*.py"],
                exclude_globs=["**/node_modules/**"],
            )

            paths = list_reviewable_paths(project, max_files=10)
            code_file = read_code_file(tmp_path, "src/app.py", max_file_bytes=1000)

            self.assertEqual(paths, ["src/app.py"])
            self.assertIsNotNone(code_file)
            self.assertEqual(code_file.language, "python")
            self.assertIn("hello", code_file.content)

    def test_double_star_pattern_also_matches_repo_root(self):
        with TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            (tmp_path / "app.py").write_text("print('hello')\n", encoding="utf-8")
            (tmp_path / "node_modules").mkdir()
            (tmp_path / "node_modules" / "x.py").write_text("bad", encoding="utf-8")

            project = ProjectConfig(
                id="p1",
                name="Project 1",
                path=str(tmp_path),
                include_globs=["**/*.py"],
                exclude_globs=["**/node_modules/**"],
            )

            self.assertEqual(list_reviewable_paths(project, max_files=10), ["app.py"])
