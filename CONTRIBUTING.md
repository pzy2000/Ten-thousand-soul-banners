# Contributing

欢迎往“万魂幡.Skill”继续加角色，但请把它当成一个“结构化蒸馏仓库”来维护，而不是梗图堆料区。

## 如何新增一个人物

1. 根据角色归属，在仓库根目录创建人物目录，目录名使用稳定、可读、便于引用的英文或拼音 kebab-case。
   * `sovereign_skills/<persona>/`：仅用于 `renhuang-flag` 角色
   * `soulbanner_skills/<persona>/`：用于其余角色
2. 复制以下模板：
   * `templates/skill.template.md`
   * `templates/persona-readme.template.md`
   * `templates/research/*.template.md`
3. 补齐 `SKILL.md`、`README.md` 与 `references/research/` 六个 research 文件。
4. 在 `PEOPLE.md` 与对应 `categories/*.md` 中登记该人物。
5. 提交 PR，并按模板补齐风险说明。

说明：`skills/` 目录现在只保留 `all-personas` 这类总入口或基础设施 skill，不再放单角色目录。

## 必须提供的文件

每个角色目录至少包含：

* `SKILL.md`
* `README.md`
* `references/research/01-writings.md`
* `references/research/02-conversations.md`
* `references/research/03-expression-dna.md`
* `references/research/04-external-views.md`
* `references/research/05-decisions.md`
* `references/research/06-timeline.md`

## 人物分类如何填写

请在 `SKILL.md` frontmatter 的 `category_tags` 中填写分类标签，并同步更新对应分类页。

当前已启用分类：

* `renhuang-flag`
* `abstract-flag`
* `jianghu-flag`
* `business-flag`
* `fiction-flag`
* `research-flag`

说明：

* 一个角色可以出现在多个分类页
* 物理目录只保留一份
* `renhuang-flag` 角色的物理目录放在 `sovereign_skills/`
* 其他当前分类角色的物理目录放在 `soulbanner_skills/`
* `人皇旗（Power Figures）` 角色统一收录在 `sovereign_skills/`

## 如何写“诚实边界”

每个角色 README 与 `SKILL.md` 都必须明确写清：

* 这是基于公开素材蒸馏出来的二创人格
* 不替代本人
* 不保证时效事实正确
* 不得用于冒充、诈骗、误导
* 哪些领域素材不足，不能强答

## 哪些内容会被拒绝

以下 PR 会被直接要求修改或拒绝：

* 纯空壳目录
* 无 research 支撑
* 直接冒充本人
* 文案全是烂梗、没有结构化蒸馏
* 分类解释存在明显冒犯且无边界说明
* 把“人皇旗”写成真实等级评价
* 把“二创人格”写成“真实复活”

## 建议的质量标准

一个合格人物至少应该做到：

* 能说明“为什么值得蒸馏”
* 能说明“适合回答什么问题”
* 有稳定输出风格，而不是随机模仿
* 有最少两组示例对话
* 有可继续扩展的 research 骨架
