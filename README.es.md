<div align="center">

# Ten Thousand Soul Banners.Skill

> *"Cuando el estandarte se alza, recoge todas las máscaras públicas; cuando la bandera se despliega, convoca cada voz a su sitio."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Monorepo](https://img.shields.io/badge/monorepo-8%20personas%20%2B%201%20router-black)
![Categories](https://img.shields.io/badge/categories-6-blue)
![Style](https://img.shields.io/badge/style-derivativo%20%2F%20ludico-orange)

**Idiomas / Languages**: [中文](README.md) · [English](README.en.md) · **Español** · [日本語](README.ja.md) · [한국어](README.ko.md)

<br>

<img src="Overview.png" alt="Póster general de Ten Thousand Soul Banners.Skill" width="460">

<br>
<br>

**Un repositorio multi-persona que destila figuras públicas, personalidades de internet y personajes ficticios en módulos `.skill`.**

<br>

8 personas, 1 skill de entrada, 6 páginas de categorías y un sistema de plantillas que puede seguir creciendo vía PRs.<br>
No se trata de repetir citas ni de fingir una inmortalidad digital. Convierte el estilo estable, los marcos de juicio y la tensión narrativa del material público en módulos invocables.

[Ejemplos](#examples) · [Instalación](#install) · [Qué se destila](#what-gets-distilled) · [Nombre](#naming) · [Límites honestos](#honest-boundaries)

</div>

---

<a id="examples"></a>
## Ejemplos

```text
Usuario       ❯ ¿Quién sirve mejor para analizar "¿debería renunciar y lanzarme a emprender?"

all-personas  ❯ Si quieres el ángulo de "no te precipites, revisa primero tu retirada",
                empieza con Hanli.

                Si quieres la versión de "empuja fuerte, encuentra el cuello de botella y pregunta cuál es la restricción real",
                cambia a Musk.

                No mezclaré personalidades al azar por defecto.
                Elige una y cambio con claridad.
```

```text
Usuario    ❯ Cambia a modo Hanli y dime si debería ir all in por esta oportunidad.

Hanli      ❯ Esto no debe hacerse con ligereza.

             Que una oportunidad resulte tentadora no significa que merezca tu apuesta completa.
             Primero debes hacerte dos preguntas:
             ¿puedes soportar el peor resultado,
             y si fallas, todavía tienes un camino de regreso?

             Si la respuesta es no en ambos casos,
             entonces esto no es una oportunidad,
             sino riesgo con un nombre más bonito.

             Preserva tu base primero y habla de ambición después.
             Planea antes de moverte, y así podrás durar.
```

```text
Usuario    ❯ Haz que Trump y Musk digan una frase cada uno: "Deja de arrastrar este proyecto."

Trump      ❯ Esto ya está clarísimo. No decidir ahora es desperdiciar una posición ganadora.
             No es un problema complicado. Lo has pospuesto demasiado.

Musk       ❯ Primero identifica cuál es el cuello de botella real.
             Si la meta es válida, elimina los pasos no críticos y lanza una prueba de inmediato.
```

Esto no consiste en pegarle a un personaje una simple piel de chat. Ten Thousand Soul Banners.Skill busca que el marco de juicio, el ADN expresivo y el ritmo narrativo de cada persona participen de verdad en el análisis.

---

<a id="install"></a>
## Instalación

### Instalar todo el repositorio

```bash
git clone https://github.com/pzy2000/Ten-thousand-soul-banners.git
cd Ten-thousand-soul-banners
```

### Instalar el skill de entrada

Tomando como ejemplo el directorio local de skills de Codex:

```bash
cp -R skills/all-personas ~/.codex/skills/all-personas
```

Luego puedes activarlo directamente con prompts como:

```text
> Lista todas las personas de Ten Thousand Soul Banners
> ¿Quién es mejor para analizar este problema?
> Cambia al modo Changshu Arno
> Mira esto desde el ángulo de Power Figures
> Haz que Trump y Musk digan una frase cada uno
```

### Instalar un skill individual

```bash
cp -R skills/tong-jincheng ~/.codex/skills/tong-jincheng
```

Después de activarlo, puedes preguntar directamente:

```text
> Mira esta relación desde la perspectiva de Tong Jincheng
> Cambia al modo Hanli y analiza si debería asumir este riesgo
> Di algo absurdo con la voz de Changshu Arno
> Desde la perspectiva de Yann LeCun, ¿por qué los LLM todavía no bastan?
```

Si usas otro cliente compatible con `SKILL.md`, también puedes importar directamente el directorio del personaje correspondiente.

---

<a id="what-gets-distilled"></a>
## Qué Se Destila

Ten Thousand Soul Banners.Skill no es un repositorio de un solo personaje, sino un monorepo de Skills multi-persona. La primera versión actual incluye:

| Módulo | Contenido |
|------|------|
| **Entrada principal** | `all-personas`, encargado de listar personajes, navegar por categorías, recomendar, cambiar y comparar múltiples personas |
| **Personas actuales** | Changshu Arno, Liangzi, Tong Jincheng, Trump, Musk, Yu Dazui, Hanli, Yann LeCun |
| **Sistema de categorías** | `Power Figures (renhuang-flag)`, `abstract-flag`, `jianghu-flag`, `business-flag`, `fiction-flag`, `research-flag` |
| **Estructura de investigación** | Cada persona incluye `SKILL.md`, `README.md` y el conjunto de seis archivos en `references/research/` |
| **Mecanismo de extensión** | `CONTRIBUTING.md`, plantilla de PR, plantillas de issues y directorio de plantillas |

Lo que se destila aquí no es "qué frases famosas dijo alguien", sino estas capas:

* estilo de expresión estable
* marco cognitivo central
* heurísticas de decisión
* ADN expresivo
* tensión del personaje
* límites de uso

En una frase: **las citas te dicen qué dijo alguien; Ten Thousand Soul Banners.Skill intenta volver invocable "cómo juzgaría".**

---

## Personas Actuales

| Persona | Posicionamiento | Categoría |
|------|------|------|
| **Changshu Arno** | abstracción, sinceridad extraña, lenguaje de promesas, aire de seudoproverbio | `abstract-flag` |
| **Liangzi** | creador de mukbang de base popular, crudeza corporal, fuerte instinto de supervivencia | `jianghu-flag` |
| **Tong Jincheng** | gurú de relaciones, juicio emocional, anti-frases hechas | `jianghu-flag` |
| **Trump** | narrativa fuerte, confrontación fuerte, lenguaje absolutista | `renhuang-flag` |
| **Musk** | primeros principios, obsesión ingenieril, impulso por visión | `renhuang-flag` |
| **Yu Dazui** | presión de keynote, energía de guerra comercial, retórica tecnológica de ventas | `business-flag` |
| **Hanli** | personaje ficticio, supervivencia prudente, actuar solo después de planear | `fiction-flag` |
| **Yann LeCun** | ruta de investigación, modelos del mundo, aprendizaje autosupervisado, anti-hype | `research-flag` |

Índice completo: [PEOPLE.md](PEOPLE.md).

---

<a id="naming"></a>
## Nombre

### ¿Por qué se llama "Ten Thousand Soul Banners"?

"Ten Thousand Soul Banners" es el nombre de ambientación del repositorio para esta colección multi-persona de `.skill`. Aquí, "souls" es una forma juguetona de hablar de estilos de persona, plantillas de expresión y caparazones narrativos.

Solo puede entenderse como:

* destilación de ciber-personas
* dobles digitales derivados
* un conjunto de módulos de persona invocables

No debe entenderse como:

* invocación espiritual real
* inmortalidad literal
* resurrección real de ninguna persona

### ¿Por qué existe la categoría "Power Figures"?

"Power Figures" es una etiqueta interna y bromista para agrupar personas que, dentro de la narrativa pública, proyectan voluntad fuerte, producción fuerte, marca personal fuerte y sensación de dominio.

Ese nombre:

* no clasifica la capacidad real de nadie
* no implica superioridad genética ni humana
* no emite un juicio de valor sobre la realidad
* no respalda ninguna postura política

Por ahora, `Power Figures` solo incluye:

* `trump`
* `musk`

---

## Navegación por Categorías

* [Power Figures](categories/renhuang-flag.md)
* [abstract-flag](categories/abstract-flag.md)
* [jianghu-flag](categories/jianghu-flag.md)
* [business-flag](categories/business-flag.md)
* [fiction-flag](categories/fiction-flag.md)
* [research-flag](categories/research-flag.md)

Una persona puede aparecer en varias páginas de categorías, pero en el repositorio solo se mantiene una copia física del directorio.

---

## Materiales y Estructura de Investigación

Este repositorio permite usar cualquier material público, pero cada personaje debe hacer el proceso de destilación lo más transparente posible.

Cada directorio de persona sigue esta estructura:

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

Estos seis archivos de research se usan para organizar:

* expresiones clave y patrones de escritura
* conversaciones largas y modos de interacción
* ADN expresivo
* perspectivas externas y controversias
* estilo de toma de decisiones
* línea temporal de formación del personaje

---

<a id="honest-boundaries"></a>
## Límites Honestos

**Lo que este repositorio sí puede hacer:**

* construir personas a partir de estilos estables presentes en material público
* simular ritmo expresivo, marcos de juicio y tensión narrativa
* ofrecer perspectivas analíticas con diferencias claras entre personajes
* poner varias personas lado a lado ante la misma pregunta

**Lo que este repositorio no puede hacer:**

| Dimensión | Explicación |
|------|------|
| Sustituir a la persona real | Estos skills no son la persona real y no copian su personalidad privada ni su estado actual |
| Garantizar actualidad | Las respuestas del personaje no equivalen a los hechos más recientes y nunca deben reemplazar una verificación en línea |
| Habilitar una suplantación "legítima" | No deben usarse para suplantación, fraude, engaño, manipulación política ni otros escenarios engañosos |
| Responderlo todo a la fuerza | Cuando falte material de base, el skill debe admitir sus límites en vez de sobreactuar |
| Crear un sistema de clasificación real | "Ten Thousand Soul Banners" y "Power Figures" son nombres juguetones, no rankings ni respaldos del mundo real |

**Un repositorio de Skills que no te dice dónde están sus límites no merece confianza.**

---

## Expansión de la Comunidad

Se aceptan más personas en el futuro, pero cada nueva incorporación debe:

* seguir la plantilla común
* completar los seis archivos de research
* explicar claramente sus límites honestos
* declarar su categoría
* evitar presentar una persona derivada como "resurrección real"

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para las reglas de contribución.

Plantilla de PR: [.github/pull_request_template.md](.github/pull_request_template.md).

---

## Estructura del Repositorio

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

**Las citas** solo te dicen lo que alguna vez dijeron.<br>
**Ten Thousand Soul Banners.Skill** quiere que puedas invocar cómo pensarían, juzgarían y hablarían.<br><br>
*No es resurrección. Es destilación.*

</div>
