# 开源 Deep Research 调研

调研日期：2026-04-07

口径说明：这里的“主流”主要按 GitHub 星标、社区影响力、方法复用度和近一年维护活跃度综合判断，不只看某个 leaderboard。

## 当前最值得借鉴的开源路线

| 项目 | 2026-04-07 观察到的 GitHub Stars | 借鉴点 | 链接 |
| --- | --- | --- | --- |
| DeerFlow | 58.5k | 把 deep research 扩成“skills + memory + sandbox + subagents”的长流程 agent harness | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) |
| GPT Researcher | 26.3k | 最典型的 planner / execution / publisher 架构，强调引用和报告汇总 | [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher) |
| Open Deep Research | 11k | 配置化程度高，支持多搜索工具、MCP、评测；同时保留 workflow 与 multi-agent 两条实现脉络 | [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research) |
| Local Deep Researcher | 9k | “搜索 -> 总结 -> 反思缺口 -> 再搜”的迭代闭环，非常适合本地/隐私场景 | [langchain-ai/local-deep-researcher](https://github.com/langchain-ai/local-deep-researcher) |
| Open Deep Research | 6.2k | 强调 search + extract，把网页抽取当成一等能力，而不是只看搜索摘要 | [nickscamara/open-deep-research](https://github.com/nickscamara/open-deep-research) |
| node-DeepResearch | 5.1k | 极简的 search-read-reason loop，更像深答引擎而不是长报告机器 | [jina-ai/node-DeepResearch](https://github.com/jina-ai/node-DeepResearch) |

## 我看到的五条方法主线

### 1. Scope -> Research -> Write

这是 LangChain `deep_research_from_scratch` 和 `open_deep_research` 里最清楚的一条主线：先澄清任务，再研究，再写最终产物。优点是边界清晰，容易插入人工澄清、结构化输出和评测。

对这个仓库的启发：

* 角色蒸馏也必须先做 scope，不能一上来就搜。
* scope 不是“这个人是谁”，而是“这个 skill 想蒸馏哪种稳定人格资产”。

## 2. Planner / Executor / Publisher

GPT Researcher 把 deep research 拆成 planner、execution agents、publisher。它的关键不是多 agent 本身，而是先把大问题拆成多个研究问题，再并行找证据，最后统一汇总。

对这个仓库的启发：

* “人物经典语录”“性格证据”“决策方式”“时间线”本质上就是四个子问题。
* 角色生成不需要一口气总结全部人格，应先把证据槽位拆开。

## 3. Search -> Summarize -> Reflect -> Search

Local Deep Researcher 明确写了它受 IterDRAG 启发：先搜，先总结，再反思当前总结的缺口，再发下一轮搜索。这个 loop 非常适合开放主题。

对这个仓库的启发：

* 语录检索不能只搜一次“名言”。
* 应该先拉到第一批语录候选，再反思：
  * 哪些是真人一手表达？
  * 哪些只是二手引用或鸡汤号搬运？
  * 哪些语录能解释他的稳定性格，而不是只会出圈？

## 4. Search + Extract，而不是只读搜索摘要

nickscamara 的 `open-deep-research` 把 Firecrawl 的 search 和 extract 绑定在一起，说明现在主流方法已经不满足于“搜搜 snippet 再写报告”，而是更重视把原网页抽成结构化正文。

对这个仓库的启发：

* 人物语录特别容易被错引，必须看正文、逐字稿、原始采访，而不是只看 snippet。
* 对 persona 仓库来说，网页抽取优先级比 fancy UI 更高。

## 5. 两种分叉：长报告 vs 深答引擎

node-DeepResearch 很明确地把自己和 OpenAI/Gemini/Perplexity 那种长报告 deep research 区分开来。它更追求“持续搜索和推理直到找到答案”，而不是生成长文。

对这个仓库的启发：

* 角色 skill 生成更接近“证据驱动的深答引擎”，不是长报告生成器。
* 最终产物虽然是 markdown 文件，但中间态应该是结构化 evidence bundle，而不是一篇大作文。

## 我认为真正可复用的公共骨架

从上面这些项目抽象下来，当前最稳的开源 deep research 骨架是：

1. 明确 scope，把大任务压成 3 到 6 个研究槽位。
2. 为每个槽位生成 query pack，而不是只打一条总 query。
3. 搜索后拉正文，不只看 snippet。
4. 先做中间摘要，再做 gap reflection。
5. 对独立子问题并行化，但在最终汇总前做统一标准化。
6. 输出时保留 citation / source trace，不把“模型觉得像”当证据。

这六步里，真正不稳定的是 UI 和部署方式；真正稳定的是 evidence loop。

## 对本仓库最有价值的迁移判断

这个仓库不是要“研究一个问题”，而是要“蒸馏一个人”。所以最该借的不是长报告 UI，而是这些方法里的：

* 任务拆解
* 迭代反思
* 原文抽取
* 并行证据搜集
* 结构化中间层
* 明确引用边界

反过来，下面这些不是当前子项目的重点：

* 很重的前端交互
* 多人实时协作界面
* 复杂沙箱执行
* 通用 agent marketplace

## 参考来源

* [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
* [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
* [langchain-ai/open_deep_research](https://github.com/langchain-ai/open_deep_research)
* [langchain-ai/deep_research_from_scratch](https://github.com/langchain-ai/deep_research_from_scratch)
* [langchain-ai/local-deep-researcher](https://github.com/langchain-ai/local-deep-researcher)
* [nickscamara/open-deep-research](https://github.com/nickscamara/open-deep-research)
* [jina-ai/node-DeepResearch](https://github.com/jina-ai/node-DeepResearch)

说明：这里的“方法抽象”是我基于这些仓库 README 和公开说明做的归纳，不是直接摘录某一个项目的原文。
