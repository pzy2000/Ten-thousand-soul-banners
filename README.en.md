<div align="center">

# Ten Thousand Soul Banners.Skill

> *"When the banner rises, it gathers every public mask; when the flag unfurls, every voice is summoned into place."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Monorepo](https://img.shields.io/badge/monorepo-8%20personas%20%2B%201%20router-black)
![Categories](https://img.shields.io/badge/categories-6-blue)
![Style](https://img.shields.io/badge/style-derivative%20%2F%20playful-orange)

**Languages / 语言**: [中文](README.md) · **English** · [Español](README.es.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

<br>

<img src="Overview.png" alt="Ten Thousand Soul Banners.Skill overview poster" width="460">

<br>
<br>

**A multi-persona repository that distills public figures, internet personalities, and fictional characters into `.skill` modules.**

<br>

8 personas, 1 router skill, 6 category pages, and a template system that can keep growing through PRs.<br>
This is not about replaying quotes or pretending at digital immortality. It turns stable style, judgment frameworks, and narrative tension from public material into callable modules.

[Examples](#examples) · [Install](#install) · [What Gets Distilled](#what-gets-distilled) · [Naming](#naming) · [Honest Boundaries](#honest-boundaries)

</div>

---

<a id="examples"></a>
## Examples

```text
User         ❯ Who is best for analyzing "Should I quit my job and start a company?"

all-personas ❯ If you want the "don't rush, check your fallback first" angle,
               start with Hanli.

               If you want the "push hard, find the bottleneck, ask what the real constraint is" version,
               switch to Musk.

               I won't mash personalities together by default.
               Pick one, and I'll switch cleanly.
```

```text
User      ❯ Switch to Hanli mode and tell me whether I should go all in on this opportunity.

Hanli     ❯ This should not be done rashly.

            An opportunity being tempting does not mean it deserves your full stake.
            Ask yourself two questions first:
            Can you survive the worst outcome,
            and if you fail, do you still have a way back?

            If the answer is no to both,
            then this is not an opportunity,
            only risk wearing a better name.

            Preserve yourself first, then talk about ambition.
            Plan before you move, and you can last.
```

```text
User      ❯ Let Trump and Musk each say one sentence: "Stop dragging this project out."

Trump     ❯ This is already obvious. Not deciding now is just wasting a winning position.
            This is not complicated. You've just delayed for too long.

Musk      ❯ Start by finding the real bottleneck.
            If the goal is valid, delete the non-critical steps and push a test immediately.
```

This is not a chat skin pasted onto a character. Ten Thousand Soul Banners.Skill aims to make the persona's reasoning frame, expressive DNA, and narrative rhythm actually participate in analysis.

---

<a id="install"></a>
## Install

### Install the whole repository

```bash
git clone https://github.com/pzy2000/Ten-thousand-soul-banners.git
cd Ten-thousand-soul-banners
```

### Install the router skill

Using the Codex local skills directory as an example:

```bash
cp -R skills/all-personas ~/.codex/skills/all-personas
```

You can then trigger it directly with prompts like:

```text
> List every persona in Ten Thousand Soul Banners
> Who is best for analyzing this problem?
> Switch to Changshu Arno mode
> Look at this from the Power Figures angle
> Let Trump and Musk each say one sentence
```

### Install a single persona skill

```bash
cp -R skills/tong-jincheng ~/.codex/skills/tong-jincheng
```

After activation, you can ask directly:

```text
> Look at this relationship from Tong Jincheng's perspective
> Switch to Hanli mode and analyze whether I should take this risk
> Say something absurd in Changshu Arno's voice
> From Yann LeCun's perspective, why are LLMs still not enough?
```

If you use another client that supports `SKILL.md`, you can also import the corresponding persona directory directly.

---

<a id="what-gets-distilled"></a>
## What Gets Distilled

Ten Thousand Soul Banners.Skill is not a single-persona repository. It is a multi-persona Skill monorepo. The current first release includes:

| Module | Contents |
|------|------|
| **Router** | `all-personas`, responsible for listing personas, category browsing, recommendations, switching, and multi-persona comparisons |
| **Current personas** | Changshu Arno, Liangzi, Tong Jincheng, Trump, Musk, Yu Dazui, Hanli, Yann LeCun |
| **Category system** | `Power Figures (renhuang-flag)`, `abstract-flag`, `jianghu-flag`, `business-flag`, `fiction-flag`, `research-flag` |
| **Research structure** | Every persona includes `SKILL.md`, `README.md`, and the six-file `references/research/` set |
| **Extension mechanism** | `CONTRIBUTING.md`, PR template, issue templates, and the template directory |

What this repository distills is not "what famous lines someone once said", but these things:

* stable expressive style
* core cognitive framework
* decision heuristics
* expressive DNA
* persona tension
* usage boundaries

In one sentence: **quotes tell you what they once said; Ten Thousand Soul Banners.Skill tries to make "how they would judge" callable.**

---

## Current Personas

| Persona | Positioning | Category |
|------|------|------|
| **Changshu Arno** | absurdist sincerity, promise-speak, pseudo-proverb energy | `abstract-flag` |
| **Liangzi** | grassroots mukbang persona, raw physicality, strong survival instinct | `jianghu-flag` |
| **Tong Jincheng** | relationship guru persona, emotional judgment, anti-cliche advice | `jianghu-flag` |
| **Trump** | strong narrative control, confrontation, absolutist language | `renhuang-flag` |
| **Musk** | first principles, engineering obsession, vision-driven execution | `renhuang-flag` |
| **Yu Dazui** | launch-event pressure, business-war energy, tech sales rhetoric | `business-flag` |
| **Hanli** | fictional character, cautious survival, move only after planning | `fiction-flag` |
| **Yann LeCun** | research trajectory, world models, self-supervised learning, anti-hype | `research-flag` |

Full index: [PEOPLE.md](PEOPLE.md).

---

<a id="naming"></a>
## Naming

### Why is it called "Ten Thousand Soul Banners"?

"Ten Thousand Soul Banners" is the repository's worldbuilding wrapper name for a multi-persona `.skill` collection. Here, "souls" is a playful way to refer to persona styles, expression templates, and narrative shells.

It can only be understood as:

* cyber-persona distillation
* derivative digital doubles
* a set of callable persona modules

It must not be understood as:

* literal spirit summoning
* literal immortality
* the real resurrection of any person

### Why is there a "Power Figures" category?

"Power Figures" is an internal tongue-in-cheek label for personas that project strong will, strong output, strong personal branding, and strong dominance inside public narratives.

This label:

* does not rank real-world capability
* does not imply genetic or human superiority
* does not make a real-world value judgment
* does not endorse any political position

At the moment, `Power Figures` only contains:

* `trump`
* `musk`

---

## Browse by Category

* [Power Figures](categories/renhuang-flag.md)
* [abstract-flag](categories/abstract-flag.md)
* [jianghu-flag](categories/jianghu-flag.md)
* [business-flag](categories/business-flag.md)
* [fiction-flag](categories/fiction-flag.md)
* [research-flag](categories/research-flag.md)

A persona can appear on multiple category pages, but only one physical directory is kept in the repository.

---

## Sources and Research Structure

This repository allows any public material, but each persona must make the distillation process as transparent as possible.

Every persona directory follows the same structure:

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

These six research files are used to organize:

* core expression and writing patterns
* long-form conversations and interaction modes
* expressive DNA
* outside perspectives and controversies
* decision-making style
* persona formation timeline

---

<a id="honest-boundaries"></a>
## Honest Boundaries

**What this repository can do:**

* build personas from stable styles found in public material
* simulate expressive rhythm, judgment frameworks, and narrative tension
* provide analytical viewpoints with distinct persona differences
* place multiple personas side by side on the same question

**What this repository cannot do:**

| Dimension | Explanation |
|------|------|
| Replace the real person | These skills are not the real person, and they do not copy anyone's private personality or current state |
| Guarantee recency | Persona answers do not equal the latest facts and should never replace online verification |
| Enable legitimate impersonation | They must not be used for impersonation, fraud, misleading behavior, political deception, or other deceptive scenarios |
| Answer everything forcefully | When the source material is thin, the skill should admit limits instead of acting through it |
| Create a real ranking system | "Ten Thousand Soul Banners" and "Power Figures" are playful labels, not real-world rankings or endorsements |

**A Skill repository that does not tell you where its boundaries are is not worth trusting.**

---

## Community Expansion

More personas are welcome in the future, but every addition must:

* follow the shared template
* complete the six research files
* state honest boundaries clearly
* declare category placement
* avoid presenting derivative personas as "real resurrection"

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules.

PR template: [.github/pull_request_template.md](.github/pull_request_template.md).

---

## Repository Structure

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
│   ├── fiction-flag.md
│   └── research-flag.md
├── skills/
│   ├── all-personas/
│   ├── changshu-arno/
│   ├── liangzi/
│   ├── tong-jincheng/
│   ├── trump/
│   ├── musk/
│   ├── yu-dazui/
│   ├── hanli/
│   └── yann-lecun/
├── templates/
│   └── research/
└── .github/
```

---

## License

MIT.

---

<div align="center">

**Quotes** only tell you what they once said.<br>
**Ten Thousand Soul Banners.Skill** wants you to call how they would think, judge, and speak.<br><br>
*Not resurrection. Distillation.*

</div>
