from __future__ import annotations

import json

from .models import CodeFile


FILE_REVIEW_SCHEMA: dict = {
    "type": "object",
    "properties": {
        "path": {"type": "string"},
        "language": {"type": "string"},
        "overall_comment": {"type": "string"},
        "score": {"type": "integer", "minimum": 0, "maximum": 100},
        "issues": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},
                    "severity": {
                        "type": "string",
                        "enum": ["critical", "high", "medium", "low", "info"],
                    },
                    "line_start": {"type": "integer", "minimum": 1},
                    "line_end": {"type": "integer", "minimum": 1},
                    "description": {"type": "string"},
                    "fix": {"type": "string"},
                    "confidence": {"type": "number", "minimum": 0, "maximum": 1},
                },
                "required": [
                    "type",
                    "severity",
                    "line_start",
                    "line_end",
                    "description",
                    "fix",
                    "confidence",
                ],
                "additionalProperties": False,
            },
        },
    },
    "required": ["path", "language", "overall_comment", "score", "issues"],
    "additionalProperties": False,
}


def build_file_review_prompt(project_name: str, code_file: CodeFile) -> str:
    numbered = "\n".join(
        f"{line_no}: {line}" for line_no, line in enumerate(code_file.content.splitlines(), start=1)
    )
    schema = json.dumps(FILE_REVIEW_SCHEMA, ensure_ascii=False, indent=2)
    return f"""你是一个资深代码审查专家。请对仓库 `{project_name}` 中的单个文件做全量代码审查。

审查目标：
1. 发现真实、高价值的问题，不要输出泛泛建议。
2. 优先关注安全、正确性、并发/事务、资源泄漏、异常处理、边界条件、可维护性、测试可测性。
3. 问题行号必须来自下面的带行号源码；如果问题跨多行，请给出起止行。
4. 如果没有明确问题，issues 返回空数组，score 应该较高。
5. 只输出 JSON，不要 Markdown，不要代码块，不要解释性前后缀。

评分规则：
- 满分 100，不及格 60。
- critical 问题通常扣 30 分以上，high 扣 15 分左右，medium 扣 6 分左右，low 扣 2 分左右。
- 不要为了凑数量虚构问题。

输出必须符合 JSON Schema：
{schema}

文件路径：{code_file.path}
语言：{code_file.language}
文件 SHA256：{code_file.sha256}

带行号源码：
<<<CODE
{numbered}
CODE
"""

