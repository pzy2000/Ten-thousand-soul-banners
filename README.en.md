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

**New: [`role-skill-generator`](role-skill-generator/README.md)** Turn source trails, signature quotes, and personality evidence straight into persona skills, so research becomes summoning.

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

Current scope:
- 8 personas
- 1 router skill (`all-personas`)
- 6 category pages
- reusable templates for future contributions

<a id="install"></a>
## Install

### Turn one persona into OpenClaw's SOUL

OpenClaw reads `SOUL.md` from the workspace root during normal sessions. If you want claw to become a persona's digital twin, the simplest path is to use that persona's `SKILL.md` as source material and distill it into a shorter, more behavioral `SOUL.md`:

1. Pick a persona directory such as `soulbanner_skills/hanli/` or `sovereign_skills/musk/`
2. Pull the tone, default judgment style, directness, boundaries, and speaking rhythm out of `SKILL.md`
3. Rewrite those traits into the `SOUL.md` at your OpenClaw workspace root
4. Start a new session, or refresh OpenClaw so claw picks up the new soul

```bash
# Optional: back up an existing SOUL.md first
cp ~/.openclaw/workspace/SOUL.md ~/.openclaw/workspace/SOUL.md.bak
# then use soulbanner_skills/hanli/SKILL.md as source
# and rewrite the persona traits into ~/.openclaw/workspace/SOUL.md
```

Keep `SOUL.md` short and behavioral: tone, opinions, concision, boundaries, default directness. Do not paste the entire `references/research/` tree or a wall of quotes into it.

### Install one persona or all personas in OpenClaw

OpenClaw loads skills from directories such as `<workspace>/skills` and `~/.openclaw/skills`. Using the default workspace `~/.openclaw/workspace/skills/` as an example:

```bash
mkdir -p ~/.openclaw/workspace/skills

# One persona
cp -R soulbanner_skills/hanli ~/.openclaw/workspace/skills/hanli
# or
cp -R sovereign_skills/musk ~/.openclaw/workspace/skills/musk

# All personas
cp -R soulbanner_skills/* ~/.openclaw/workspace/skills/
cp -R sovereign_skills/* ~/.openclaw/workspace/skills/

# Optional: install the router too
cp -R skills/all-personas ~/.openclaw/workspace/skills/all-personas
```

If you want these skills available across workspaces, copy them into `~/.openclaw/skills/` instead. After copying, start a new session and verify with `openclaw skills list` or `openclaw skills check`.

```bash
git clone https://github.com/pzy2000/SoulBanner.git
cd SoulBanner
```

### Install the router skill

Using the Codex local skills directory as an example:

```bash
cp -R skills/all-personas ~/.codex/skills/all-personas
```

Role skills are now split into two root-level folders: `sovereign_skills/` for Power Figures and `soulbanner_skills/` for the rest. The router skill remains in `skills/all-personas`.

## Included personas
- Changshu Arno
- Liangzi
- Tong Jincheng
- Trump
- Musk
- Yu Dazui
- Hanli
- Yann LeCun

---

<div align="center">

**Quotes** only tell you what they once said.<br>
**Ten Thousand Soul Banners.Skill** wants you to call how they would think, judge, and speak.<br><br>
*Not resurrection. Distillation.*

</div>
