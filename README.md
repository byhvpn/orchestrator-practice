# orchestrator-practice

练手仓库：试验 Orchestrator 编排"Codex 写代码、Claude 审查、GitHub Actions 自动测试"的流程。

- 代码：`textstats.py`（简单的文本统计函数）
- 测试：`tests/`，运行 `pytest -q`
- 自动测试：每个 PR 与推送到 main 时由 GitHub Actions 运行（检查名 `test`）
- 规则：见 `AGENTS.md`
