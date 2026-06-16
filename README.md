# Full Code Review Service

这是一个用于“全量代码审查”的后台服务示例：定时扫描已下载到本地的多个代码仓库，用 Codex SDK 调用本地大模型做文件级 review，然后把统一 JSON 结果 POST 到后端 API。

默认上报地址：

```text
http://demo.api/save/codereview/result
```

## 架构

```text
config/projects.json
        |
        v
Scheduler -> Repository Scanner -> Codex Reviewer -> JSON Normalizer -> Result Poster
        |              |                  |                |                 |
        |              |                  |                |                 +--> POST API
        |              |                  |                +--> schema/line clamp
        |              |                  +--> openai-codex + local model provider
        |              +--> git ls-files / fallback walk
        +--> state/review_state.json avoids duplicate revision reviews
```

## 关键设计

- `codereview_service.config`：加载项目列表、调度周期、Codex 参数。
- `codereview_service.repository`：列出可审核文件、过滤二进制/大文件。
- `codereview_service.prompt`：文件级审查提示词和 JSON Schema。
- `codereview_service.reviewer`：Codex SDK / Codex CLI / mock 三种适配。
- `codereview_service.service`：调度、聚合、状态保存、结果上报。

## Codex SDK 安装

官方 Python SDK 包名是：

```bash
pip install openai-codex
```

Docker 镜像会通过 `requirements.txt` 自动安装。Codex SDK 会读取 `$CODEX_HOME/config.toml`，本工程在 `docker-compose.yml` 中把示例配置挂载到 `/app/codex-home/config.toml`。

## 配置本地大模型

编辑 `config/codex-config.toml.example`，让 `base_url` 指向你的本地模型网关：

```toml
model_provider = "local_llm"
model = "qwen2.5-coder:32b"

[model_providers.local_llm]
name = "Local LLM Gateway"
base_url = "http://host.docker.internal:11434/v1"
wire_api = "responses"
```

推荐本地网关支持 Responses API。Codex 当前配置参考：

- Codex SDK：<https://developers.openai.com/codex/sdk>
- 非交互模式和 `--output-schema`：<https://developers.openai.com/codex/noninteractive>
- `model_provider` / `model_providers`：<https://developers.openai.com/codex/config-reference>

## 配置项目列表

编辑 `config/projects.example.json`：

```json
{
  "scanner": {
    "interval_seconds": 3600,
    "run_once": false,
    "state_path": "/app/state/review_state.json",
    "post_result_url": "http://demo.api/save/codereview/result"
  },
  "codex": {
    "mode": "sdk",
    "model": "qwen2.5-coder:32b",
    "sandbox": "read_only"
  },
  "projects": [
    {
      "id": "demo-project",
      "name": "Demo Project",
      "path": "/repos/demo-project",
      "enabled": true
    }
  ]
}
```

`path` 是容器内路径。把宿主机仓库父目录挂载到 `/repos` 即可。

## 运行

1. 准备本地模型服务，例如 Ollama / LM Studio / 内部 LLM Gateway，并暴露 OpenAI-compatible Responses API。

2. 修改 `docker-compose.yml` 的仓库挂载：

```yaml
volumes:
  - /your/local/repos:/repos:ro
```

3. 启动：

```bash
docker compose up --build
```

4. 单次运行可把配置改为：

```json
"run_once": true
```

## CLI 兜底模式

如果你更希望使用 Codex 非交互模式的 `--output-schema`，可改：

```json
"codex": {
  "mode": "cli",
  "model": "qwen2.5-coder:32b",
  "cli_bin": "codex"
}
```

SDK 模式适合程序化控制 Agent；CLI 模式适合对 JSON Schema 强约束要求更高的流水线。

## 上报 JSON 格式

服务按项目 revision 上报一次：

```json
{
  "task_id": "stable-hash",
  "project_id": "demo-project",
  "project_name": "Demo Project",
  "repository_path": "/repos/demo-project",
  "revision": "git-sha",
  "review_type": "full",
  "files": [
    {
      "path": "src/app.py",
      "language": "python",
      "overall_comment": "整体结构清晰。",
      "score": 88,
      "issues": [
        {
          "type": "correctness",
          "severity": "medium",
          "line_start": 12,
          "line_end": 12,
          "description": "边界条件未处理。",
          "fix": "增加空值判断。",
          "confidence": 0.83
        }
      ],
      "reviewer": "codex-sdk"
    }
  ],
  "aggregate": {
    "overall_score": 88,
    "blocking": false,
    "critical_count": 0,
    "high_count": 0,
    "medium_count": 1,
    "low_count": 0,
    "info_count": 0,
    "file_count": 1
  }
}
```

## 单元测试

本工程核心逻辑使用标准库，测试不需要真实 Codex 或本地模型：

```bash
python -m unittest discover -s tests
```

## 生产建议

- Worker 容器使用只读仓库挂载，Codex sandbox 使用 `read_only`。
- 后端 API 增加鉴权和幂等键，幂等键可用 `task_id`。
- 大型仓库先按语言/模块拆分，多 Worker 并行。
- 对安全敏感仓库先接入 Semgrep/CodeQL，把静态扫描结果加入 prompt。
- 状态文件可换成 Redis/PostgreSQL，避免多副本重复 review。
