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

これはキャラクターにチャット用のスキンを貼る話ではありません。Ten Thousand Soul Banners.Skill が目指すのは、判断フレーム、表現 DNA、語りのリズムそのものを分析へ参加させることです。

---

<a id="install"></a>
## 導入

### リポジトリ全体を導入する

```bash
git clone https://github.com/pzy2000/Ten-thousand-soul-banners.git
cd Ten-thousand-soul-banners
```

### ルーター skill を導入する

Codex のローカル skill ディレクトリを例にすると:

```bash
cp -R skills/all-personas ~/.codex/skills/all-personas
```

導入後は、たとえば次のように呼び出せます:

```text
> Ten Thousand Soul Banners の全ペルソナを一覧して
> この問題に向いているのは誰？
> Changshu Arno モードに切り替えて
> Power Figures の視点でこれを見て
> Trump と Musk に一言ずつ言わせて
```

### 単体の persona skill を導入する

```bash
cp -R skills/tong-jincheng ~/.codex/skills/tong-jincheng
```

有効化後は、直接こう聞けます:

```text
> この関係を Tong Jincheng の視点で見て
> Hanli モードに切り替えて、今このリスクを取るべきか分析して
> Changshu Arno の調子で抽象的な一言を言って
> Yann LeCun の視点では、なぜ LLM だけではまだ足りないのか
```

`SKILL.md` を扱える別のクライアントを使っている場合も、対応する persona ディレクトリをそのまま読み込めます。

---

<a id="what-gets-distilled"></a>
## 何を蒸留しているか

Ten Thousand Soul Banners.Skill は単一人物のリポジトリではなく、複数ペルソナの Skill モノレポです。現行の初版には次が含まれます:

| モジュール | 内容 |
|------|------|
| **総合入口** | `all-personas`。ペルソナ一覧、カテゴリ閲覧、推薦、切り替え、複数比較を担当 |
| **現在のペルソナ** | Changshu Arno、Liangzi、Tong Jincheng、Trump、Musk、Yu Dazui、Hanli、Yann LeCun |
| **カテゴリ体系** | `Power Figures (renhuang-flag)`、`abstract-flag`、`jianghu-flag`、`business-flag`、`fiction-flag`、`research-flag` |
| **研究構造** | すべての persona に `SKILL.md`、`README.md`、`references/research/` の 6 点セットを配置 |
| **拡張の仕組み** | `CONTRIBUTING.md`、PR テンプレート、Issue テンプレート、テンプレート用ディレクトリ |

このリポジトリが蒸留しているのは「その人がどんな名言を残したか」ではなく、次のような層です:

* 安定した語り口
* 中核となる認知フレーム
* 意思決定のヒューリスティクス
* 表現 DNA
* 人物像の張力
* 使用上の境界

一言でいえば、**名言は過去に何を言ったかを教えますが、Ten Thousand Soul Banners.Skill は「どう判断しそうか」を呼び出せるようにしたいのです。**

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

MIT。

---

<div align="center">

**名言** が教えてくれるのは、その人が何を言ったかだけです。<br>
**Ten Thousand Soul Banners.Skill** が呼び出したいのは、その人がどう考え、どう判断し、どう語るかです。<br><br>
*復活ではない。蒸留だ。*

</div>
