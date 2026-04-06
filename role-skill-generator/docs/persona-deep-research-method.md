# 人物语录与性格资料 Deep Research 方法

这份方法不是从某一个开源仓库原封不动搬过来，而是基于调研结果做的改写，目标是服务本仓库的 persona skill 生成。

## 目标变化

通用 deep research 的目标通常是：

* 回答一个复杂问题
* 或生成一篇带引用的长报告

但这个仓库真正需要的是：

* 找到人物的稳定表达材料
* 追溯经典语录出处
* 识别性格、判断框架和叙事张力
* 最后压成 `SKILL.md` / `README.md` / `references/research/*.md`

所以这里的核心不是“长文写作”，而是“证据蒸馏”。

## 新工作流

### 1. Scope 人物画像

输入不是一个自然语言问题，而是一张 `target profile`：

* 角色名 / slug
* 分类
* 输出目录归属：`soulbanner_skills` 或 `sovereign_skills`
* 已知别名
* 目标语言
* 想重点蒸馏什么：经典语录、第一手表达、性格标签、决策方式、时间线

这一步决定后续 query pack 的覆盖面，也决定最后 `SKILL.md` 的 frontmatter 和场景定位。

### 2. Query Pack 分槽位检索

我把人物研究拆成六个槽位：

1. `quote-bank-primary`
2. `first-person-writings`
3. `conversations-and-interviews`
4. `personality-and-external-views`
5. `decision-style`
6. `timeline-and-evolution`

这样做的原因很直接：

* 语录检索和性格检索不是一回事。
* 能当口头禅的表达，必须尽量回到一手文本。
* 外界评价可以帮助补“人设张力”，但不应直接决定核心认知框架。

## 3. Source Ladder 证据分层

人物研究必须分层用源：

### A 层：第一手

* 公开采访逐字稿
* 演讲全文
* 书信、专栏、著作
* 原视频和原音频转写

用途：

* 口头禅
* 句长和节奏
* 经典语录候选
* 自己如何定义自己

### B 层：高质量二手

* 权威传记
* 主流媒体长访
* 学术资料
* 高质量机构简介

用途：

* 时间线
* 外界标签
* 关键决策事件
* 稳定性格描述

### C 层：社区 / 二创 / 粉黑大战

* forum
* 梗图二创
* 粉丝总结
* 吐槽帖

用途：

* “最容易被二创放大的点”
* 支持者 / 吐槽者视角
* 二创社区视角

限制：

* 不能单独决定 `SKILL.md` 主体判断。

## 4. Quote Verification 语录核验

这里是通用 deep research 和人物蒸馏差异最大的地方。

语录必须带 provenance：

* `high`：可追到一手原文、逐字稿、书信、演讲或可靠原始出版物
* `medium`：只能追到高质量二手资料，但来源链较清楚
* `low`：只在语录站、搬运站、梗图帖里出现

规则：

* `high` 可以影响 `SKILL.md` 的口头禅和表达 DNA。
* `medium` 只能放进 `references/research/01-writings.md` 的候选区，谨慎上主文案。
* `low` 不进入主 skill，只能保留在人工复核区或直接丢弃。

## 5. Trait Stabilization 性格特征稳定化

一个“性格点”至少满足以下之一，才值得进主 persona：

* 有一手表达直接支撑，且能在多个场景复现
* 有两个以上互相独立的来源反复提到
* 能同时被“支持者视角”和“吐槽者视角”解释，只是褒贬不同

不满足这些条件的，最多写进：

* `research/04-external-views.md`
* 或 `research/06-timeline.md`

不应直接升级为：

* 核心认知框架
* 决策启发式
* 标志性表达动作

## 6. 从证据表到仓库文件的映射

### `01-writings.md`

放：

* 高频表达结论
* 关键词
* 经典语录候选和出处置信度

### `02-conversations.md`

放：

* 对话模式
* 面对赞美 / 质疑 / 冲突的回应方式
* 代表性互动场景

### `03-expression-dna.md`

放：

* 节奏
* 风格关键词
* 标志动作
* 语录指纹

### `04-external-views.md`

放：

* 支持者视角
* 吐槽者视角
* 二创社区视角
* trait 证据表

### `05-decisions.md`

放：

* 判断规则
* 风险偏好
* 常见取舍

### `06-timeline.md`

放：

* 人设形成
* 出圈
* 风格转折
* 形象固化

## 7. 渲染目标不是报告，而是 persona bundle

我把中间层定成 `persona bundle JSON`，原因是：

* 检索和渲染解耦
* 可以人工审 bundle，再决定是否真正写入仓库
* LLM 输出不直接碰最终 markdown，便于复核
* 后面如果想换模型、换搜索源、换 prompt，不影响最终渲染器

## 子项目里的落地

这个方法在子项目里对应为：

1. `plan-queries`
   生成人物 query pack
2. `collect`
   搜索并抓取页面正文
3. `synthesize`
   把正文合成为 `persona bundle`
4. `render`
   把 bundle 渲染成仓库格式

## 推荐使用策略

对这个仓库，我建议把自动化放在“收集证据”和“生成初稿”上，把人工审核放在下面几项：

* 经典语录是否真有出处
* 口头禅是否足够稳定
* 分类是否合理
* `SKILL.md` 的输出风格是否真的可调用，而不是泛泛模仿

自动化能提高吞吐，但不能替代最后的人设判断。
