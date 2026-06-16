import unittest

from codereview_service.models import codefile_from_bytes
from codereview_service.reviewer import parse_file_review


class ReviewerParsingTest(unittest.TestCase):
    def test_parse_file_review_json_fence_and_line_clamp(self):
        code_file = codefile_from_bytes("src/app.py", b"print('a')\nprint('b')\n")
        raw = """```json
{
  "path": "src/app.py",
  "language": "python",
  "overall_comment": "ok",
  "score": 120,
  "issues": [
    {
      "type": "correctness",
      "severity": "bad",
      "line_start": 10,
      "line_end": 20,
      "description": "desc",
      "fix": "fix",
      "confidence": 2
    }
  ]
}
```"""

        review = parse_file_review(raw, code_file, reviewer="test")

        self.assertEqual(review.score, 100)
        self.assertEqual(review.issues[0].severity, "medium")
        self.assertEqual(review.issues[0].line_start, 2)
        self.assertEqual(review.issues[0].line_end, 2)
