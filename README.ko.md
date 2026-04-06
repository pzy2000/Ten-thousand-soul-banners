<div align="center">

# Ten Thousand Soul Banners.Skill

> *"깃발이 오르면 세상의 가면을 거두고, 펼쳐지면 온갖 목소리를 제자리로 불러 모은다."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Monorepo](https://img.shields.io/badge/monorepo-8%20personas%20%2B%201%20router-black)
![Categories](https://img.shields.io/badge/categories-6-blue)
![Style](https://img.shields.io/badge/style-%ED%8C%A8%EB%9F%AC%EB%94%94%20%2F%20%EB%86%80%EC%9D%B4-orange)

**언어 / Languages**: [中文](README.md) · [English](README.en.md) · [Español](README.es.md) · [日本語](README.ja.md) · **한국어**

<br>

<img src="Overview.png" alt="Ten Thousand Soul Banners.Skill 개요 포스터" width="460">

<br>
<br>

**공인, 인터넷 인물, 가상 캐릭터를 `.skill` 모듈로 증류한 멀티 페르소나 저장소입니다.**

<br>

8개의 페르소나, 1개의 라우터 skill, 6개의 카테고리 페이지, 그리고 PR로 계속 확장할 수 있는 템플릿 체계를 담고 있습니다.<br>
이 프로젝트는 명언을 복창하거나 디지털 영생을 흉내 내려는 것이 아닙니다. 공개 자료 속의 안정적인 말투, 판단 프레임, 서사적 긴장을 호출 가능한 모듈로 만드는 시도입니다.

**새 기능: [`role-skill-generator`](role-skill-generator/README.md)** 인물 자료, 명언, 성격 근거를 바로 캐릭터 skill로 벼려내서, 리서치를 곧바로 소환으로 바꿉니다.

[예시](#examples) · [설치](#install) · [무엇을 증류하는가](#what-gets-distilled) · [이름의 의미](#naming) · [정직한 경계](#honest-boundaries)

</div>

---

<a id="examples"></a>
## 예시

```text
사용자         ❯ "회사를 그만두고 창업해야 하나?" 같은 문제는 누가 잘 보나요?

all-personas  ❯ "성급하게 가지 말고, 먼저 퇴로를 확인하라"는 관점이 필요하다면
                Hanli가 좋습니다.

                "강하게 밀고, 병목을 찾고, 진짜 제약이 무엇인지 보라"는 버전이 필요하면
                Musk로 전환하면 됩니다.

                기본값으로는 인격을 함부로 섞지 않습니다.
                하나를 고르면 깔끔하게 그 하나로 전환합니다.
```

```text
사용자    ❯ Hanli 모드로 바꿔서, 이 기회에 올인해야 할지 분석해줘.

Hanli     ❯ 이 일은 경솔하게 해서는 안 됩니다.

            기회가 매력적으로 보인다고 해서
            전부를 걸 가치가 있다는 뜻은 아닙니다.
            먼저 스스로에게 두 가지를 물어야 합니다.
            최악의 결과를 감당할 수 있는가,
            실패했을 때 돌아갈 길이 남아 있는가.

            둘 다 없다면,
            그것은 기회가 아니라
            이름만 그럴듯하게 바꾼 위험입니다.

            먼저 자신을 보전하고, 그다음에 전진을 말해야 합니다.
            계획한 뒤 움직여야 오래 갈 수 있습니다.
```

```text
사용자    ❯ Trump와 Musk에게 "이 프로젝트 이제 그만 질질 끌어"라고 한마디씩 시켜줘.

Trump     ❯ 이건 이미 너무 분명합니다. 지금 결정을 안 하는 건 이길 판을 그냥 버리는 겁니다.
            복잡한 문제가 아닙니다. 당신이 너무 오래 끌었을 뿐입니다.

Musk      ❯ 먼저 진짜 병목이 뭔지 보세요.
            목표가 타당하다면 비핵심 단계를 지우고 바로 검증을 돌려야 합니다.
```

현재 구성:
- 페르소나 8종
- 라우터 skill 1개 (`all-personas`)
- 카테고리 페이지 6개
- 확장을 위한 템플릿 세트

<a id="install"></a>
## 설치

### 하나의 페르소나를 OpenClaw의 SOUL로 바꾸기

OpenClaw는 일반 세션에서 워크스페이스 루트의 `SOUL.md`를 읽습니다. claw를 특정 페르소나의 디지털 분신처럼 만들고 싶다면, 그 페르소나의 `SKILL.md`를 원본으로 삼아 더 짧고 행동 중심적인 `SOUL.md`로 증류하는 것이 가장 간단합니다.

1. `soulbanner_skills/hanli/` 또는 `sovereign_skills/musk/` 같은 페르소나 디렉터리를 고릅니다
2. `SKILL.md`에서 말투, 기본 판단 프레임, 직설성, 경계, 말의 리듬을 추려냅니다
3. 그 특성들을 OpenClaw 워크스페이스 루트의 `SOUL.md`에 다시 써 넣습니다
4. 새 세션을 열거나 OpenClaw를 새로고침해서 claw가 새 SOUL을 읽게 합니다

```bash
# 선택 사항: 기존 SOUL.md가 있다면 먼저 백업
cp ~/.openclaw/workspace/SOUL.md ~/.openclaw/workspace/SOUL.md.bak
# 그다음 soulbanner_skills/hanli/SKILL.md를 참고해서
# ~/.openclaw/workspace/SOUL.md에 페르소나 특성을 다시 작성합니다
```

`SOUL.md`에는 상호작용 감각을 실제로 바꾸는 요소만 남기는 것이 좋습니다. 예를 들면 말투, 관점, 간결함, 경계, 기본 직설성입니다. `references/research/` 전체나 긴 인용문 묶음을 그대로 넣지는 마세요.

### 한 페르소나 또는 전체 페르소나 skill을 OpenClaw에 설치하기

OpenClaw는 `<workspace>/skills`, `~/.openclaw/skills` 같은 디렉터리에서 skills를 읽습니다. 여기서는 기본 워크스페이스인 `~/.openclaw/workspace/skills/`를 예로 듭니다.

```bash
mkdir -p ~/.openclaw/workspace/skills

# 단일 페르소나
cp -R soulbanner_skills/hanli ~/.openclaw/workspace/skills/hanli
# 또는
cp -R sovereign_skills/musk ~/.openclaw/workspace/skills/musk

# 전체 페르소나
cp -R soulbanner_skills/* ~/.openclaw/workspace/skills/
cp -R sovereign_skills/* ~/.openclaw/workspace/skills/

# 선택 사항: 라우터도 함께 설치
cp -R skills/all-personas ~/.openclaw/workspace/skills/all-personas
```

이 skills를 모든 워크스페이스에서 공통으로 쓰고 싶다면 대상 경로를 `~/.openclaw/skills/`로 바꾸면 됩니다. 복사 후에는 새 세션을 열고 `openclaw skills list` 또는 `openclaw skills check`로 인식 여부를 확인하세요.

```bash
git clone https://github.com/pzy2000/SoulBanner.git
cd SoulBanner
```

### 라우터 skill 설치

Codex 로컬 skill 디렉터리를 예로 들면:

```bash
cp -R skills/all-personas ~/.codex/skills/all-personas
```

캐릭터 skill 은 이제 루트의 두 폴더로 나뉩니다. `sovereign_skills/` 는 Power Figures, `soulbanner_skills/` 는 그 외 역할용이며, 라우터 skill 은 계속 `skills/all-personas` 에 있습니다.

## 포함된 페르소나
- 창수 아누오
- 량쯔
- 퉁진청
- 트럼프
- 머스크
- 위다쭈이
- 한리
- Yann LeCun

---

## 현재 페르소나

| 페르소나 | 포지셔닝 | 카테고리 |
|------|------|------|
| **Changshu Arno** | 추상 밈, 묘한 진정성, 약속 말투, 가짜 격언 감성 | `abstract-flag` |
| **Liangzi** | 서민형 먹방 캐릭터, 거친 육체감, 강한 생존 감각 | `jianghu-flag` |
| **Tong Jincheng** | 연애 군사형 캐릭터, 관계 판단, 반-치유형 조언 | `jianghu-flag` |
| **Trump** | 강한 서사 장악, 강한 대립성, 절대화된 표현 | `renhuang-flag` |
| **Musk** | 제1원리, 엔지니어링 집착, 비전 중심 추진력 | `renhuang-flag` |
| **Yu Dazui** | 발표회 압박감, 상전 분위기, 기술 세일즈 화법 | `business-flag` |
| **Hanli** | 가상 캐릭터, 신중한 생존 지향, 계획 후 행동 | `fiction-flag` |
| **Yann LeCun** | 연구 노선, 세계 모델, 자기지도학습, 반 hype | `research-flag` |

전체 색인은 [PEOPLE.md](PEOPLE.md)에서 볼 수 있습니다.

---

<a id="naming"></a>
## 이름의 의미

### 왜 "Ten Thousand Soul Banners"인가?

"Ten Thousand Soul Banners"는 이 멀티 페르소나 `.skill` 묶음을 감싸는 세계관용 이름입니다. 여기서 "souls"는 페르소나 스타일, 표현 템플릿, 서사적 외피를 장난스럽게 부르는 말입니다.

이 이름은 오직 다음처럼만 이해해야 합니다:

* 사이버 페르소나 증류
* 2차 창작형 디지털 분신
* 호출 가능한 페르소나 모듈 집합

다음처럼 이해하면 안 됩니다:

* 실제 강령
* 문자 그대로의 불멸
* 특정 인물의 실제 부활

### 왜 "Power Figures" 카테고리가 있는가?

"Power Figures"는 공개 서사 속에서 강한 의지, 강한 발신력, 강한 개인 브랜드, 강한 지배감을 드러내는 페르소나를 묶는 내부의 장난스러운 분류 라벨입니다.

이 이름은:

* 현실 능력 순위를 뜻하지 않습니다
* 유전적 우열이나 인간적 우열을 뜻하지 않습니다
* 현실 가치판단을 내리지 않습니다
* 어떤 정치적 입장도 지지하지 않습니다

현재 `Power Figures`에는 다음 둘만 고정으로 포함됩니다:

* `trump`
* `musk`

---

## 카테고리로 보기

* [Power Figures](categories/renhuang-flag.md)
* [abstract-flag](categories/abstract-flag.md)
* [jianghu-flag](categories/jianghu-flag.md)
* [business-flag](categories/business-flag.md)
* [fiction-flag](categories/fiction-flag.md)
* [research-flag](categories/research-flag.md)

하나의 persona가 여러 카테고리 페이지에 동시에 들어갈 수는 있지만, 물리 디렉터리는 하나만 유지합니다.

---

## 자료와 연구 구조

이 저장소는 공개 자료 사용을 허용하지만, 각 persona는 증류 과정을 가능한 한 투명하게 드러내야 합니다.

모든 persona 디렉터리는 다음 구조를 따릅니다:

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

이 6개의 research 파일은 다음 내용을 정리하는 데 쓰입니다:

* 핵심 표현과 문체
* 긴 대화와 상호작용 패턴
* 표현 DNA
* 외부 시선과 논쟁
* 의사결정 방식
* 캐릭터 형성 타임라인

---

<a id="honest-boundaries"></a>
## 정직한 경계

**이 저장소가 할 수 있는 것:**

* 공개 자료 속 안정적인 스타일을 바탕으로 persona를 구성하기
* 말의 리듬, 판단 프레임, 서사적 긴장을 모사하기
* 페르소나 차이가 분명한 분석 시점을 제공하기
* 같은 질문 위에 여러 persona를 나란히 세워 비교하기

**이 저장소가 할 수 없는 것:**

| 항목 | 설명 |
|------|------|
| 실제 인물 대체 | 이 skill들은 실제 인물이 아니며, 사적인 성격이나 현재 상태를 복제하지도 않습니다 |
| 최신성 보장 | persona의 답변은 최신 사실과 동일하지 않으며, 온라인 검증을 대체해서도 안 됩니다 |
| 합법적인 사칭 지원 | 사칭, 사기, 오도, 정치적 기만 등 어떤 기만적 상황에도 사용하면 안 됩니다 |
| 모든 분야에서 억지로 답하기 | 자료가 부족한 영역이라면 무리해서 연기하지 말고 한계를 인정해야 합니다 |
| 현실 서열 만들기 | "Ten Thousand Soul Banners"와 "Power Figures"는 장난스러운 이름일 뿐, 현실의 순위나 보증이 아닙니다 |

**자기 경계가 어디인지 말하지 않는 Skill 저장소는 신뢰할 가치가 없습니다.**

---

## 커뮤니티 확장

앞으로 더 많은 페르소나를 추가하는 것은 환영하지만, 새 인물은 반드시 다음을 충족해야 합니다:

* 공통 템플릿을 따를 것
* 6개의 research 파일을 채울 것
* 정직한 경계를 명확히 적을 것
* 소속 카테고리를 선언할 것
* 2차 창작 persona를 "실제 부활"처럼 쓰지 말 것

기여 방식은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.

PR 템플릿: [.github/pull_request_template.md](.github/pull_request_template.md).

---

## 저장소 구조

```text
SoulBanner/
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

**명언**은 그들이 무엇을 말했는지만 알려줍니다.<br>
**Ten Thousand Soul Banners.Skill**은 그들이 어떻게 생각하고, 어떻게 판단하고, 어떻게 말할지를 호출하고자 합니다.<br><br>
*부활이 아니라, 증류입니다.*

</div>
