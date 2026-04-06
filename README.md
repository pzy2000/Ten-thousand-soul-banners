<div align="center">

# 万魂幡.Skill

> *「万魂幡起，收尽人间百相；人皇旗展，唤来众声归位。」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Monorepo](https://img.shields.io/badge/monorepo-7%20personas%20%2B%201%20router-black)
![Categories](https://img.shields.io/badge/categories-5-blue)
![Style](https://img.shields.io/badge/style-%E4%BA%8C%E5%88%9B%20%2F%20%E6%95%B4%E6%B4%BB-orange)

**语言 / Languages**：**中文** · [English](README.en.md) · [Español](README.es.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

<br>

<img src="Overview.png" alt="万魂幡.Skill 概览海报" width="460">

<br>
<br>

**一个把公众人物、网络人物、虚构角色蒸馏成 `.skill` 的多人仓库。**

<br>

7 个首批角色，1 个总 Skill 入口，5 个分类页，1 套可继续提 PR 的模板系统。<br>
不是复读语录，不是数字永生，而是把公开素材里的稳定风格、判断框架和叙事张力，做成可调用模块。

[看效果](#效果示例) · [安装](#安装) · [蒸馏了什么](#万魂幡蒸馏了什么) · [命名解释](#命名解释) · [诚实边界](#诚实边界)

</div>

---

## 效果示例

```text
用户          ❯ 谁适合分析“我该不该裸辞创业”这种问题？

all-personas ❯ 如果你要的是“别冲动，先看退路”的视角，
               优先推荐韩立。

               如果你想看“强推进、拆瓶颈、先问约束条件”的版本，
               可以切到马斯克。

               默认我先不给你乱混人格。
               你点一个，我就切一个。
```

```text
用户      ❯ 切到韩立模式，分析我现在要不要为了一个机会 all in。

韩立      ❯ 此事不可贸然。

            机会动人，不代表现在就该押上全部。
            你先问自己两个问题：
            最坏结果你承不承受得起，
            一旦失手，你有没有退路。

            若两者都没有，这不是机会，
            只是换了一种说法的冒险。

            先保全自身，再谈进取。
            谋定而后动，方能长久。
```

```text
用户      ❯ 让特朗普和马斯克分别说一句“别再拖这个项目了”。

特朗普    ❯ 这件事已经很清楚了，现在不做决定就是在浪费胜利。
            这不是复杂问题，是你拖得太久了。

马斯克    ❯ 先看真正的瓶颈是什么。
            如果目标成立，就把非关键步骤删掉，立刻推进验证。
```

这不是把角色当聊天皮肤贴上去。万魂幡.Skill 追求的是：**让角色的判断框架、表达 DNA、叙事节奏真正参与分析。**

---

## 安装

### 安装整个仓库

```bash
git clone https://github.com/pzy2000/Ten-thousand-soul-banners.git
cd Ten-thousand-soul-banners
```

### 安装总入口 skill

以 Codex 本地技能目录为例：

```bash
cp -R skills/all-personas ~/.codex/skills/all-personas
```

然后可以直接触发：

```text
> 列出万魂幡里所有角色
> 谁适合分析这个问题
> 切到常熟阿诺模式
> 用人皇旗的视角看这件事
> 让特朗普和马斯克分别说一句
```

### 安装单人物 skill

```bash
cp -R skills/tong-jincheng ~/.codex/skills/tong-jincheng
```

激活后就可以直接问：

```text
> 用童锦程的视角看这段关系
> 切到韩立模式，分析我要不要冒险
> 用常熟阿诺的口气说一句抽象的话
```

如果你使用的是其他支持 `SKILL.md` 的客户端，也可以直接导入对应人物目录。

---

## 万魂幡蒸馏了什么

“万魂幡.Skill”不是单人物仓库，而是一个多人 Skill Monorepo。当前第一版包含：

| 模块 | 内容 |
|------|------|
| **总入口** | `all-personas`，负责列人、分类浏览、角色推荐、切换与多角色对照 |
| **首批角色** | 常熟阿诺、良子、童锦程、特朗普、马斯克、余大嘴、韩立 |
| **分类体系** | `人皇旗（Power Figures）`、`abstract-flag`、`jianghu-flag`、`business-flag`、`fiction-flag` |
| **研究结构** | 每个角色都有 `SKILL.md`、`README.md` 和 `references/research/` 六件套 |
| **扩展机制** | `CONTRIBUTING.md`、PR 模板、Issue 模板、模板目录 |

这套仓库蒸馏的不是“谁说过哪些名句”，而是下面这些东西：

* 稳定表达风格
* 核心认知框架
* 决策启发式
* 表达 DNA
* 人设张力
* 使用边界

一句话说：**语录告诉你他讲过什么，万魂幡.Skill 试图让他“会怎么判断”变得可调用。**

---

## 首批角色

| 角色 | 定位 | 分类 |
|------|------|------|
| **常熟阿诺** | 抽象、真诚、诺言诺语、伪哲理感 | `abstract-flag` |
| **良子** | 草根吃播、生猛、强肉身感、强生存感 | `jianghu-flag` |
| **童锦程** | 深情祖师爷、关系判断、反鸡汤 | `jianghu-flag` |
| **特朗普** | 强叙事、强对抗、绝对化表达 | `renhuang-flag` |
| **马斯克** | 第一性原理、工程执念、愿景推进 | `renhuang-flag` |
| **余大嘴** | 发布会压强、商战感、技术话术 | `business-flag` |
| **韩立** | 虚构角色，谨慎求生、谋定后动 | `fiction-flag` |

完整索引见 [PEOPLE.md](PEOPLE.md)。

---

## 命名解释

### 为什么叫“万魂幡”

“万魂幡”是这个仓库的世界观包装名，用来指代一个多人 `.skill` 集合仓库。这里的“魂”，是对“人格样式 / 表达模板 / 叙事外壳”的戏谑说法。

它只能理解成：

* 赛博人格蒸馏
* 数字分身式二创
* 一组可调用的人格模块

不能理解成：

* 真实招魂
* 真实永生
* 真实复活某个人

### 为什么有“人皇旗（Power Figures）”

“人皇旗（Power Figures）”是仓库内部的戏谑分类标签，用于归纳那些在公共叙事中呈现出强意志、强输出、强个人品牌、强支配感的角色。

这个命名：

* 不代表真实性能排序
* 不代表基因优劣
* 不代表现实价值判断
* 不代表政治立场背书

当前 `人皇旗` 固定只收：

* `trump`
* `musk`

---

## 分类浏览

* [人皇旗（Power Figures）](categories/renhuang-flag.md)
* [abstract-flag](categories/abstract-flag.md)
* [jianghu-flag](categories/jianghu-flag.md)
* [business-flag](categories/business-flag.md)
* [fiction-flag](categories/fiction-flag.md)

一个角色可以同时被索引进多个分类页，但物理目录只保留一份。

---

## 素材与研究结构

本仓库允许使用一切公开材料，但每个人物都必须把素材蒸馏过程尽量透明化。

每个 persona 目录统一包含：

```text
<persona>/
├── SKILL.md
├── README.md
└── references/
    └── research/
        ├── 01-writings.md
        ├── 02-conversations.md
        ├── 03-expression-dna.md
        ├── 04-external-views.md
        ├── 05-decisions.md
        └── 06-timeline.md
```

这 6 个 research 文件分别用于整理：

* 核心表达与写法
* 长对话与互动模式
* 表达 DNA
* 外界视角与争议
* 决策方式
* 人设形成时间线

---

## 诚实边界

**这个仓库能做的：**

* 用公开素材中的稳定风格去构建 persona
* 模拟角色的表达节奏、判断框架和叙事张力
* 提供带人格差异的分析视角
* 让不同人物在同一问题上形成清晰对照

**这个仓库做不到的：**

| 维度 | 说明 |
|------|------|
| 替代真人 | 这里的 skill 不是本人，不复制真实私下人格，也不复制当下状态 |
| 保证时效 | 角色回答不等于最新事实，尤其不应替代联网核查 |
| 合法冒充 | 不可用于冒充、诈骗、误导、政治欺诈或其他欺骗性场景 |
| 无限强答 | 哪些领域素材不足，就应该承认不足，不能硬演 |
| 真实评价体系 | “万魂幡 / 人皇旗”只是戏谑命名，不构成现实排序与背书 |

**一个不告诉你边界在哪的 Skill 仓库，不值得信任。**

---

## 社区扩展

后续欢迎继续往“万魂幡”里加人，但新增人物必须：

* 遵循统一模板
* 补齐 research 六件套
* 写清楚诚实边界
* 声明分类归属
* 不得把二创人格写成“真实复活”

贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

PR 模板见 [.github/pull_request_template.md](.github/pull_request_template.md)。

---

## 仓库结构

```text
Ten-thousand-soul-banners/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── PEOPLE.md
├── categories/
│   ├── renhuang-flag.md
│   ├── abstract-flag.md
│   ├── jianghu-flag.md
│   ├── business-flag.md
│   └── fiction-flag.md
├── skills/
│   ├── all-personas/
│   ├── changshu-arno/
│   ├── liangzi/
│   ├── tong-jincheng/
│   ├── trump/
│   ├── musk/
│   ├── yu-dazui/
│   └── hanli/
├── templates/
│   └── research/
└── .github/
```

---

## License

MIT。

---

<div align="center">

**语录** 只能告诉你他们说过什么。<br>
**万魂幡.Skill** 想让你调用他们“会怎么想、会怎么判断、会怎么说”。<br><br>
*不是复活，是蒸馏。*

</div>
