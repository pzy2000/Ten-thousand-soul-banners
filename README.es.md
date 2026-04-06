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

**Nuevo: [`role-skill-generator`](role-skill-generator/README.md)** Convierte fuentes, citas clásicas y pruebas de personalidad en skills de personaje, para que investigar se vuelva invocar.

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

Alcance actual:
- 8 personas
- 1 skill enrutador (`all-personas`)
- 6 páginas de categorías
- plantillas reutilizables para futuras contribuciones

<a id="install"></a>
## Instalación

### Convertir una persona en el SOUL de OpenClaw

OpenClaw lee `SOUL.md` desde la raíz del workspace durante las sesiones normales. Si quieres que claw se convierta en el gemelo digital de una persona, lo más simple es usar el `SKILL.md` de esa persona como material base y destilarlo en un `SOUL.md` más corto y conductual:

1. Elige un directorio de persona, como `soulbanner_skills/hanli/` o `sovereign_skills/musk/`
2. Extrae de `SKILL.md` el tono, el marco de juicio por defecto, el grado de franqueza, los límites y el ritmo verbal
3. Reescribe esos rasgos en el `SOUL.md` de la raíz de tu workspace de OpenClaw
4. Abre una nueva sesión, o refresca OpenClaw para que claw cargue el nuevo soul

```bash
# Opcional: si ya tienes SOUL.md, haz una copia primero
cp ~/.openclaw/workspace/SOUL.md ~/.openclaw/workspace/SOUL.md.bak
# luego usa soulbanner_skills/hanli/SKILL.md como base
# y reescribe esos rasgos en ~/.openclaw/workspace/SOUL.md
```

Conviene que `SOUL.md` sea breve y conductual: tono, opiniones, nivel de concisión, límites y franqueza por defecto. No pegues ahí todo `references/research/` ni una pared de citas.

### Instalar una persona o todas las personas en OpenClaw

OpenClaw carga skills desde directorios como `<workspace>/skills` y `~/.openclaw/skills`. Tomando como ejemplo el workspace por defecto `~/.openclaw/workspace/skills/`:

```bash
mkdir -p ~/.openclaw/workspace/skills

# Una sola persona
cp -R soulbanner_skills/hanli ~/.openclaw/workspace/skills/hanli
# o
cp -R sovereign_skills/musk ~/.openclaw/workspace/skills/musk

# Todas las personas
cp -R soulbanner_skills/* ~/.openclaw/workspace/skills/
cp -R sovereign_skills/* ~/.openclaw/workspace/skills/

# Opcional: instalar también el skill enrutador
cp -R skills/all-personas ~/.openclaw/workspace/skills/all-personas
```

Si quieres que estos skills estén disponibles en todos tus workspaces, cambia el destino a `~/.openclaw/skills/`. Después de copiarlos, abre una sesión nueva y verifica con `openclaw skills list` o `openclaw skills check`.

```bash
git clone https://github.com/pzy2000/SoulBanner.git
cd SoulBanner
```

### Instalar el skill de entrada

Tomando como ejemplo el directorio local de skills de Codex:

```bash
cp -R skills/all-personas ~/.codex/skills/all-personas
```

Los skills de personajes ahora se dividen en dos carpetas de nivel raíz: `sovereign_skills/` para Power Figures y `soulbanner_skills/` para el resto. El skill enrutador sigue en `skills/all-personas`.

## Personas incluidas
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

**Las citas** solo te dicen lo que alguna vez dijeron.<br>
**Ten Thousand Soul Banners.Skill** quiere que puedas invocar cómo pensarían, juzgarían y hablarían.<br><br>
*No es resurrección. Es destilación.*

</div>
