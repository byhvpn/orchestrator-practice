# 给编码代理的规则（Codex 与 Claude 都适用）

这是一个练手仓库，用来试验"Codex 写、Claude 审"的流程。

1. 所有回复、PR 描述、审查意见用中文。
2. 每个改动只做任务要求的事，保持小。
3. 新功能或修改必须同时加上对应的测试；提交 PR 前在本地运行 `pytest -q`，全部通过才提交。
4. 不要修改 `.github/`、`AGENTS.md`、`CLAUDE.md`、`pytest.ini`、`requirements-dev.txt`，除非任务明确要求。
5. 不要新增第三方依赖。
6. 不要直接推送到 main；一律走分支和 PR。
7. 不要合并 PR，不要关闭或重开别人的 PR，不要用 gh 或 GitHub API 修改仓库设置、分支保护、Actions 设置；合并只由仓库主人本人操作。
8. 审查方（Claude）：若 PR 改动了第 4 条列出的文件，必须在审查意见里明确指出并要求修改。
