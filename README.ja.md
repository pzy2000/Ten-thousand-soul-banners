<div align="center">

# Ten Thousand Soul Banners.Skill

> *「幡が立てば世の仮面を集め、旗が開けばあらゆる声を所に呼び戻す。」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Monorepo](https://img.shields.io/badge/monorepo-8%20personas%20%2B%201%20router-black)
![Categories](https://img.shields.io/badge/categories-6-blue)
![Style](https://img.shields.io/badge/style-%E4%BA%8C%E6%AC%A1%E5%89%B5%E4%BD%9C%20%2F%20%E9%81%8A%E3%81%B3-orange)

**言語 / Languages**: [中文](README.md) · [English](README.en.md) · [Español](README.es.md) · **日本語** · [한국어](README.ko.md)

<br>

<img src="Overview.png" alt="Ten Thousand Soul Banners.Skill の概要ポスター" width="460">

<br>
<br>

**公開人物・ネット人物・架空キャラクターを `.skill` モジュールへ蒸留する、マルチペルソナのリポジトリです。**

<br>

8 人のペルソナ、1 つのルーター skill、6 つのカテゴリページ、そして PR で拡張し続けられるテンプレート群を収録しています。<br>
これは名言集の焼き直しでも、デジタル不死のふりでもありません。公開素材にある安定した話し方、判断フレーム、物語の張力を、呼び出せるモジュールにする試みです。

**新機能: [`role-skill-generator`](role-skill-generator/README.md)** 人物資料、名言、性格の証拠をそのままペルソナ skill に鍛え直し、調査をそのまま召喚へつなげます。

[実例](#examples) · [導入](#install) · [何を蒸留しているか](#what-gets-distilled) · [命名](#naming) · [誠実な境界](#honest-boundaries)

</div>

---

<a id="examples"></a>
## 実例

```text
ユーザー        ❯ 「会社を辞めて起業すべきか」みたいな話は誰に向いている？

all-personas   ❯ 「焦るな、まず退路を見ろ」という視点が欲しいなら、
                 まずは Hanli です。

                 「強く押し込め、ボトルネックを見つけ、本当の制約を問え」
                 という版が欲しいなら Musk に切り替えてください。

                 何も指定されなければ、人格を勝手に混ぜません。
                 一人選べば、その一人にきれいに切り替えます。
```

```text
ユーザー   ❯ Hanli モードに切り替えて、この機会に all in すべきか見てほしい。

Hanli      ❯ 軽々しく動くべきではありません。

             魅力的に見える機会だからといって、
             すべてを賭ける価値があるとは限りません。
             先に二つ、自分へ問いなさい。
             最悪の結果に耐えられるか。
             失敗したとき、まだ退路があるか。

             どちらもないなら、
             それは機会ではなく、
             名を変えた危険にすぎません。

             まず身を保ち、その後で前進を語るべきです。
             準備してから動けば、長く持ちます。
```

```text
ユーザー   ❯ Trump と Musk に「このプロジェクトをもう引き延ばすな」と一言ずつ言わせて。

Trump      ❯ もう十分はっきりしています。今決めないのは勝てる局面を無駄にしているだけです。
             複雑な話じゃない。あなたが引き延ばしすぎたのです。

Musk       ❯ まず本当のボトルネックを見てください。
             目標が正しいなら、非本質な工程を削って今すぐ検証を回すべきです。
```

現在の構成:
- 8 ペルソナ
- 1 つのルーター skill（`all-personas`）
- 6 つのカテゴリページ
- 今後の追加に使えるテンプレート

<a id="install"></a>
## 導入

### 1人のペルソナを OpenClaw の SOUL にする

OpenClaw は通常セッションで、ワークスペースのルートにある `SOUL.md` を読み込みます。claw を特定ペルソナのデジタル分身のようにしたいなら、その人物の `SKILL.md` を素材にして、より短く振る舞い中心の `SOUL.md` に蒸留するのがいちばん簡単です。

1. `soulbanner_skills/hanli/` や `sovereign_skills/musk/` のようなペルソナディレクトリを選ぶ
2. `SKILL.md` から、口調、標準の判断フレーム、直接さ、境界線、話すリズムを抜き出す
3. それらを OpenClaw ワークスペースのルートにある `SOUL.md` に書き直す
4. 新しいセッションを開くか OpenClaw をリフレッシュして、新しい SOUL を claw に読み込ませる

```bash
# 任意: 既存の SOUL.md があるなら先にバックアップ
cp ~/.openclaw/workspace/SOUL.md ~/.openclaw/workspace/SOUL.md.bak
# その後 soulbanner_skills/hanli/SKILL.md を参照し、
# ~/.openclaw/workspace/SOUL.md にペルソナ特性を書き直す
```

`SOUL.md` には、会話体験を本当に変える要素だけを残すのがおすすめです。たとえば口調、意見、簡潔さ、境界線、標準の直接さなどです。`references/research/` 全体や長い引用集をそのまま貼り付けないでください。

### 1人分 / 全員分の skill を OpenClaw に入れる

OpenClaw は `<workspace>/skills` や `~/.openclaw/skills` などのディレクトリから skill を読み込みます。ここでは既定のワークスペース `~/.openclaw/workspace/skills/` を例にします。

```bash
mkdir -p ~/.openclaw/workspace/skills

# 1人分
cp -R soulbanner_skills/hanli ~/.openclaw/workspace/skills/hanli
# または
cp -R sovereign_skills/musk ~/.openclaw/workspace/skills/musk

# 全員分
cp -R soulbanner_skills/* ~/.openclaw/workspace/skills/
cp -R sovereign_skills/* ~/.openclaw/workspace/skills/

# 任意: ルーターも一緒に入れる
cp -R skills/all-personas ~/.openclaw/workspace/skills/all-personas
```

これらの skill を全ワークスペースで共通利用したいなら、コピー先を `~/.openclaw/skills/` に変えてください。コピー後は新しいセッションを開き、`openclaw skills list` または `openclaw skills check` で認識を確認できます。

```bash
git clone https://github.com/pzy2000/SoulBanner.git
cd SoulBanner
```

### ルーター skill を導入する

Codex のローカル skill ディレクトリを例にすると:

```bash
cp -R skills/all-personas ~/.codex/skills/all-personas
```

キャラクター skill は現在、ルート直下の 2 つのフォルダに分割されています。`sovereign_skills/` は Power Figures、`soulbanner_skills/` はそれ以外の役割用です。ルーター skill は引き続き `skills/all-personas` にあります。

## 収録ペルソナ
- 常熟アーノ
- 良子
- 童錦程
- トランプ
- マスク
- 余大嘴
- 韓立
- Yann LeCun

---

## 現在のペルソナ

| ペルソナ | 位置づけ | カテゴリ |
|------|------|------|
| **Changshu Arno** | 抽象ミーム、妙な誠実さ、約束口調、偽ことわざ感 | `abstract-flag` |
| **Liangzi** | 庶民派の食べ配信、むき出しの肉体感、強い生存感覚 | `jianghu-flag` |
| **Tong Jincheng** | 恋愛軍師系、関係判断、反・定番説教 | `jianghu-flag` |
| **Trump** | 強い物語化、強い対立性、断定口調 | `renhuang-flag` |
| **Musk** | 第一原理、工学への執着、ビジョン駆動の推進 | `renhuang-flag` |
| **Yu Dazui** | 発表会の圧、商戦の気配、技術営業的な語り | `business-flag` |
| **Hanli** | 架空キャラクター、慎重な生存志向、謀ってから動く | `fiction-flag` |
| **Yann LeCun** | 研究路線、世界モデル、自己教師あり学習、反 hype | `research-flag` |

完全な一覧は [PEOPLE.md](PEOPLE.md) を参照してください。

---

<a id="naming"></a>
## 命名

### なぜ "Ten Thousand Soul Banners" なのか

"Ten Thousand Soul Banners" は、この複数 persona `.skill` 集合につけた世界観上のラベルです。ここでいう "souls" は、人格の型、話し方のテンプレート、物語的な外殻を少し戯画的に呼んだものです。

これは次のようにだけ理解してください:

* サイバー人格の蒸留
* 二次創作としてのデジタル分身
* 呼び出し可能な persona モジュール群

次のように理解してはいけません:

* 本物の招魂
* 文字どおりの不死
* 誰かの現実の復活

### なぜ "Power Figures" があるのか

"Power Figures" は、公開的な物語の中で強い意志、強い発信力、強い個人ブランド、強い支配感を見せる persona をまとめるための、内部的で冗談めいた分類ラベルです。

この名前は:

* 現実の能力順位を意味しません
* 遺伝的・人間的優劣を意味しません
* 現実の価値判断を与えません
* 政治的立場への支持を意味しません

現在 `Power Figures` に入るのは次の 2 名のみです:

* `trump`
* `musk`

---

## カテゴリ別に見る

* [Power Figures](categories/renhuang-flag.md)
* [abstract-flag](categories/abstract-flag.md)
* [jianghu-flag](categories/jianghu-flag.md)
* [business-flag](categories/business-flag.md)
* [fiction-flag](categories/fiction-flag.md)
* [research-flag](categories/research-flag.md)

1 つの persona が複数カテゴリに載ることはありますが、物理ディレクトリは 1 つだけです。

---

## 素材と研究構造

このリポジトリでは公開素材の利用を認めていますが、各 persona は蒸留の過程をできるだけ透明にしなければなりません。

各 persona ディレクトリは、次の統一構造を持ちます:

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

この 6 つの research ファイルでは、主に次を整理します:

* 中核的な表現と書き方
* 長い対話とインタラクションの型
* 表現 DNA
* 外部からの見え方と論争
* 意思決定のしかた
* 人物像が形成された時間軸

---

<a id="honest-boundaries"></a>
## 誠実な境界

**このリポジトリにできること:**

* 公開素材にある安定したスタイルから persona を組み立てる
* 語りのリズム、判断フレーム、物語の張力を模擬する
* 人物差のある分析視点を提供する
* 同じ問いに複数 persona を並べて比較させる

**このリポジトリにできないこと:**

| 項目 | 説明 |
|------|------|
| 本人の代替 | これらの skill は本人ではなく、私的な人格や現在の状態を複製するものでもありません |
| 最新性の保証 | persona の回答は最新事実と同義ではなく、オンライン確認の代わりにもなりません |
| 正当ななりすまし | なりすまし、詐欺、ミスリード、政治的欺瞞などの用途には使えません |
| 何でも強引に答えること | 素材が不足している領域では、無理に演じず限界を認めるべきです |
| 現実の序列づけ | "Ten Thousand Soul Banners" や "Power Figures" は冗談めいた名称であり、現実のランキングや後ろ盾ではありません |

**境界を明かさない Skill リポジトリは、信頼に値しません。**

---

## コミュニティ拡張

今後さらに persona を追加していくことは歓迎ですが、新規追加には次が必須です:

* 共通テンプレートに従うこと
* 6 つの research ファイルを埋めること
* 誠実な境界を明記すること
* 所属カテゴリを宣言すること
* 二次創作 persona を「本当に復活した本人」として書かないこと

貢献方法は [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

PR テンプレート: [.github/pull_request_template.md](.github/pull_request_template.md)。

---

## リポジトリ構造

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

MIT。

---

<div align="center">

**名言** が教えてくれるのは、その人が何を言ったかだけです。<br>
**Ten Thousand Soul Banners.Skill** が呼び出したいのは、その人がどう考え、どう判断し、どう語るかです。<br><br>
*復活ではない。蒸留だ。*

</div>
