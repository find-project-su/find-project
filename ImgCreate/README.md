# ImgCreate — Visual Content Creation System 🎨

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Companion dataset](https://img.shields.io/badge/examples-Hugging%20Face-yellow)

[🇬🇧 English](#english) | [🇷🇺 Русский](#русский)

---

## English

**Contents:** [Overview](#-overview) · [Visual Examples](#-visual-examples) · [Repository Structure](#-repository-structure) · [Style Characteristics](#-style-characteristics) · [Compatibility](#-compatibility--how-to-use-these-prompts) · [Available Instructions](#-available-instructions) · [Getting Started](#-getting-started) · [Recommendations](#-recommendations) · [Use Cases](#-use-cases) · [Technical Requirements](#-technical-requirements) · [Tips](#-tips) · [Contributing](#-contributing) · [Related Projects](#-related-projects) · [License](#-license)

### 🎯 Overview

The ImgCreate system helps create visual content for presentations, landing pages, websites, and other media while maintaining a unified artistic style.

**Main Character:** Rosa Romashkina (Роза Ромашкина) — central visual anchor for character-based illustrations.

This repository contains the **instructions/prompts only**. What they actually produce is shown below and in the companion image dataset — see [Visual Examples](#-visual-examples).

### 🖼 Visual Examples

A few outputs actually generated with the prompts in this repository:

<table>
<tr>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/MainChar/00001_Roza%20on%20SkateBoard_DarkTheme_Color.webp" width="200"/><br/><sub><b>Main character</b> — dark theme + color accent</sub></td>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Icons/10001_Protection_BaseTheme_Color.webp" width="200"/><br/><sub><b>Icon</b> — "Protection"</sub></td>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30001_SpiderChart_5axis.webp" width="200"/><br/><sub><b>Spider chart</b> — 5 axes</sub></td>
</tr>
<tr>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/MainChar/00002_Roza%20is%20coding%20by%20Basic_BaseTheme.webp" width="200"/><br/><sub><b>Main character</b> — base theme</sub></td>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Icons/10002_Development_BaseTheme_Color.webp" width="200"/><br/><sub><b>Icon</b> — "Development"</sub></td>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Reference_Imgs/Charts/20001_Donut.webp" width="200"/><br/><sub><b>Donut chart</b> — style reference</sub></td>
</tr>
</table>

Full gallery, resolutions, file-naming convention, and more examples: **[LS_ImgCreate dataset on Hugging Face](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)**.

### 📁 Repository Structure

```text
ImgCreate/
├── README.md
└── Instruction/
    ├── init_creation_v01.md              # Load first for any new project
    ├── slide_structure_types_v01.md      # Slide layout & structure guide
    ├── img_cat_v01.md                    # Category catalog / reference
    ├── img01_main_char_v01.md            # Main character (Rosa) illustrations
    ├── img02_no_char_v01.md              # Character-free illustrations
    ├── img03_icon_v01.md                 # Icon illustrations
    ├── img04_charts_v01.md               # Chart illustrations (overview)
    ├── img05_background_v01.md           # Background illustrations
    ├── img06_dark_theme_v01.md           # Dark theme variants
    ├── img07_color_details_v01.md        # Color accent guidelines
    ├── charts/                           # Ready-to-use chart prompts
    │   ├── Spider_Chart_Manual.md
    │   ├── 5axis_Spider 0-10scale_v01.md
    │   ├── 5axis_Spider 0-10scale Template_v01.md
    │   ├── 6axis_Spider 0-10scale_v01.md
    │   ├── 6axis_Spider 0-10scale Template_v01.md
    │   ├── donut_v01.md
    │   ├── histogram_v01.md
    │   └── Spider 0-10scale_Examples.xlsx
    └── review/                           # Presentation review system
        ├── review_manual.md
        ├── start_review.md
        ├── Example_review_context.md
        └── Example_review_result.md
```

### ✨ Style Characteristics

**Core Style**
- **Technique:** Black-and-white pencil sketch, hand-drawn
- **Background:** Clean white (default) or deep black (dark variant)
- **Color Accents:** Applied only when explicitly requested

**Visual Language**
- Hand-drawn aesthetic with organic lines
- High contrast and clear silhouettes
- Minimalist approach focusing on essential elements
- Consistent stroke weight and texture

### 🤖 Compatibility — How to Use These Prompts

These files are not code — they are structured instruction/prompt sets meant to be given as context to an AI assistant capable of generating and editing images (typically: attach or paste the relevant instruction file(s) into the chat/project as reference material, then provide your topic, or an Excel sketch for charts, as input, following the flow in [Getting Started](#-getting-started)).

> **Note for maintainers:** the README doesn't currently say which AI tool(s), models, or app(s) this system was built and tested with (e.g. a specific assistant, whether "project"/custom-instructions support or file-attachment support is required, whether image-generation must be built in or is a separate step). Adding that here would save new users a lot of trial and error.

### 📂 Available Instructions

| File | Description | When to Use | Example |
|------|-------------|-------------|---------|
| [init_creation_v01.md](Instruction/init_creation_v01.md) | Initial setup guide | Load first for new projects | — |
| [slide_structure_types_v01.md](Instruction/slide_structure_types_v01.md) | Slide layout and structure guide | For designing presentation slides | — |
| [img01_main_char_v01.md](Instruction/img01_main_char_v01.md) | Main character illustrations | When Rosa is featured | [preview](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/MainChar/00001_Roza%20on%20SkateBoard_DarkTheme_Color.webp) |
| [img02_no_char_v01.md](Instruction/img02_no_char_v01.md) | Character-free illustrations | For objects, scenes, concepts | — |
| [img03_icon_v01.md](Instruction/img03_icon_v01.md) | Icon illustrations | For UI elements, navigation | [preview](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Icons/10001_Protection_BaseTheme_Color.webp) |
| [img04_charts_v01.md](Instruction/img04_charts_v01.md) | Chart illustrations | For data visualization | see chart table below |
| [img05_background_v01.md](Instruction/img05_background_v01.md) | Background illustrations | For textures, decorations | — |
| [img06_dark_theme_v01.md](Instruction/img06_dark_theme_v01.md) | Dark theme variants | When black background needed | [preview](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/MainChar/00001_Roza%20on%20SkateBoard_DarkTheme_Color.webp) |
| [img07_color_details_v01.md](Instruction/img07_color_details_v01.md) | Color accent guidelines | When adding color elements | — |
| [img_cat_v01.md](Instruction/img_cat_v01.md) | Category catalog | Reference for all types | — |

#### Presentation Review System
| File | Description | When to Use |
|------|-------------|-------------|
| [review/review_manual.md](Instruction/review/review_manual.md) | Comprehensive review checklist | For evaluating finished presentations |
| [review/start_review.md](Instruction/review/start_review.md) | Review initiation prompt | To start AI-assisted review process |
| [review/Example_review_context.md](Instruction/review/Example_review_context.md) | Context template example | When preparing presentation context |
| [review/Example_review_result.md](Instruction/review/Example_review_result.md) | Review report example | To understand expected output format |

#### Universal Chart Prompts
| File | Description | When to Use | Example |
|------|-------------|-------------|---------|
| [charts/Spider_Chart_Manual.md](Instruction/charts/Spider_Chart_Manual.md) | Spider chart workflow guide | For creating radar/spider charts | — |
| [charts/5axis_Spider 0-10scale_v01.md](Instruction/charts/5axis_Spider%200-10scale_v01.md) | 5-axis spider chart prompt, with worked example data | For 5-axis radar diagrams | [preview](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30001_SpiderChart_5axis.webp) |
| [charts/5axis_Spider 0-10scale Template_v01.md](Instruction/charts/5axis_Spider%200-10scale%20Template_v01.md) | Same 5-axis prompt with `[placeholders]` instead of example data | When plugging in your own categories/values | [preview](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30001_SpiderChart_5axis.webp) |
| [charts/6axis_Spider 0-10scale_v01.md](Instruction/charts/6axis_Spider%200-10scale_v01.md) | 6-axis spider chart prompt, with worked example data | For 6-axis radar diagrams | [preview](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30002_SpiderChart_6axis.webp) |
| [charts/6axis_Spider 0-10scale Template_v01.md](Instruction/charts/6axis_Spider%200-10scale%20Template_v01.md) | Same 6-axis prompt with `[placeholders]` instead of example data | When plugging in your own categories/values | [preview](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30002_SpiderChart_6axis.webp) |
| [charts/donut_v01.md](Instruction/charts/donut_v01.md) | Donut chart creation prompt | For creating ring/donut diagrams | [preview](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Reference_Imgs/Charts/20001_Donut.webp) |
| [charts/histogram_v01.md](Instruction/charts/histogram_v01.md) | Histogram creation prompt | For creating vertical bar charts | [preview](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Reference_Imgs/Charts/20002_Histogram.webp) |
| [charts/Spider 0-10scale_Examples.xlsx](Instruction/charts/Spider%200-10scale_Examples.xlsx) | Excel template with examples | For preparing spider chart data | — |

**📚 Style References:** the full set of style/reference samples is in the [LS_ImgCreate Hugging Face dataset](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate) (`Reference_Imgs/` for style samples, `Example_Imgs/` for ready-made outputs across all categories — main character, icons, and charts, not just charts).

### 🚀 Getting Started

**1. Project Initialization**
- Load `Instruction/init_creation_v01.md` first
- Review the process: clarify the task → plan → create → refine

**2. Choose Illustration Type**
- Main character? → `Instruction/img01_main_char_v01.md`
- Scene without characters? → `Instruction/img02_no_char_v01.md`
- UI icons? → `Instruction/img03_icon_v01.md`
- Data visualization? → `Instruction/img04_charts_v01.md`
- Spider chart, own data? → `Instruction/charts/Spider_Chart_Manual.md` + the matching **Template** file (5 or 6 axis) + [style reference](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)
- Spider chart, want a worked example first? → the non-Template 5/6-axis file
- Donut chart? → `Instruction/charts/donut_v01.md` + [style reference](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)
- Histogram? → `Instruction/charts/histogram_v01.md` + [style reference](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)
- Backgrounds? → `Instruction/img05_background_v01.md`
- Dark theme? → `Instruction/img06_dark_theme_v01.md`
- Color accents? → `Instruction/img07_color_details_v01.md`
- Presentation slides? → `Instruction/slide_structure_types_v01.md`

**3. Review Your Presentation**
When your presentation is ready, use the review system:
1. Prepare context: describe topic, audience, goals (`Instruction/review/Example_review_context.md`)
2. Load the review manual (`Instruction/review/review_manual.md`)
3. Upload your PDF presentation
4. Use the start prompt (`Instruction/review/start_review.md`)
5. Get structured feedback with specific recommendations

**4. Follow the Process**
Each instruction provides:
- General principles and rules
- Technical specifications
- Step-by-step creation process
- Quality standards
- Common mistakes to avoid

### 📋 Recommendations

**Consistency**
- Maintain the same stroke weight across all illustrations
- Use consistent proportions for recurring elements
- Keep the same level of detail throughout the series

**Composition**
- Leave adequate white space
- Balance visual weight across the canvas
- Consider the intended display size and context

**Character Rules (Rosa Romashkina)**
- Maintain recognizable facial features
- Keep consistent body proportions
- Preserve character personality in poses and expressions

**File Organization**
- Use descriptive file names
- Version your files (v01, v02, etc.)
- Keep source files and exports separate

### 🎨 Use Cases

- **Presentations:** slide headers, concept illustrations, process diagrams, quality review
- **Data Visualization:** spider charts, donut charts, histograms, infographics with consistent style
- **Websites and landing pages:** hero illustrations, feature highlights, call-to-action graphics
- **Marketing:** social media posts, banners, newsletter graphics
- **Documentation:** tutorial illustrations, infographics, step-by-step guides

### 🔧 Technical Requirements

**Output Format**
- **WEBP only** — quality 75%, low compression (level 2). Applies to every category: main character, icons, and charts.
- Need PNG/PDF for print or a tool that doesn't accept WEBP? Export from the WEBP source rather than generating directly in that format — WEBP is the canonical output.

**Color Modes**
- **Standard:** grayscale (black pencil on white)
- **Dark variant:** light pencil on black background
- **Color accents:** RGB for digital, CMYK for print

**Size Requirements**
- **Main character illustrations:** 2048×2048 px, 1:1
- **Icons:** 1024×1024 px, 1:1 (export smaller raster sizes for specific UI placements by downscaling this source)
- **Character-free / background illustrations:** 800×600 px to 1920×1080 px *(not covered by dataset examples — treat as a recommendation rather than a verified spec)*
- **Spider charts:** 1:1 aspect ratio (square format)
- **Donut charts, Histograms:** 2:1 aspect ratio (landscape format)
- **Backgrounds:** match target display dimensions

Format and sizes above match the verified outputs in the [LS_ImgCreate dataset](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate).

### 💡 Tips

1. Start with rough sketches before finalizing
2. Create multiple versions to compare
3. Test at the actual display size
4. Get feedback before finalizing
5. Use the review system to catch overlooked issues
6. Download style references from Hugging Face for consistent chart, icon, and character design
7. Document style decisions for future reference

### 🤝 Contributing

Found a mismatch between an instruction and its actual output, a broken link, or want to add a new illustration type? Open an issue or a pull request in this repository. When adding a new prompt file, please also add or update its row in the [Available Instructions](#-available-instructions) table and, if possible, an example output in the companion dataset.

### 🔗 Related Projects

- **[LS_ImgCreate dataset](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)** (Hugging Face) — example and reference images actually produced with these prompts, with resolutions, file-naming convention, and category breakdown.

### 📄 License

MIT License — free to use, modify, and distribute with attribution to the original source.

---

## Русский

**Содержание:** [Обзор](#-обзор) · [Примеры результата](#-примеры-результата) · [Структура репозитория](#-структура-репозитория) · [Характеристики стиля](#-характеристики-стиля) · [Совместимость](#-совместимость--как-использовать-эти-промты) · [Доступные инструкции](#-доступные-инструкции) · [Начало работы](#-начало-работы) · [Рекомендации](#-рекомендации) · [Области применения](#-области-применения) · [Технические требования](#-технические-требования) · [Советы](#-советы) · [Контрибьюция](#-контрибьюция) · [Связанные проекты](#-связанные-проекты) · [Лицензия](#-лицензия)

### 🎯 Обзор

Система ImgCreate помогает создавать визуальный контент для презентаций, посадочных страниц, сайтов и других материалов, сохраняя единый художественный стиль.

**Главный персонаж:** Роза Ромашкина — центральный визуальный образ для иллюстраций с участием персонажа.

Этот репозиторий содержит **только инструкции/промты**. То, что они реально производят, показано ниже и в сопроводительном датасете — см. [Примеры результата](#-примеры-результата).

### 🖼 Примеры результата

Несколько изображений, реально сгенерированных по промтам из этого репозитория:

<table>
<tr>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/MainChar/00001_Roza%20on%20SkateBoard_DarkTheme_Color.webp" width="200"/><br/><sub><b>Главный персонаж</b> — тёмная тема + цветовой акцент</sub></td>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Icons/10001_Protection_BaseTheme_Color.webp" width="200"/><br/><sub><b>Иконка</b> — «Защита»</sub></td>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30001_SpiderChart_5axis.webp" width="200"/><br/><sub><b>Паутинка</b> — 5 осей</sub></td>
</tr>
<tr>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/MainChar/00002_Roza%20is%20coding%20by%20Basic_BaseTheme.webp" width="200"/><br/><sub><b>Главный персонаж</b> — базовая тема</sub></td>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Icons/10002_Development_BaseTheme_Color.webp" width="200"/><br/><sub><b>Иконка</b> — «Разработка»</sub></td>
<td align="center"><img src="https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Reference_Imgs/Charts/20001_Donut.webp" width="200"/><br/><sub><b>Кольцевая диаграмма</b> — референс стиля</sub></td>
</tr>
</table>

Полная галерея, разрешения, правила именования файлов и другие примеры: **[датасет LS_ImgCreate на Hugging Face](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)**.

### 📁 Структура репозитория

```text
ImgCreate/
├── README.md
└── Instruction/
    ├── init_creation_v01.md              # Загружать первым для нового проекта
    ├── slide_structure_types_v01.md      # Правила компоновки слайдов
    ├── img_cat_v01.md                    # Каталог категорий / справочник
    ├── img01_main_char_v01.md            # Иллюстрации с главным персонажем (Розой)
    ├── img02_no_char_v01.md              # Иллюстрации без персонажей
    ├── img03_icon_v01.md                 # Иконки
    ├── img04_charts_v01.md               # Иллюстрации графиков (обзор)
    ├── img05_background_v01.md           # Фоновые иллюстрации
    ├── img06_dark_theme_v01.md           # Варианты в тёмной теме
    ├── img07_color_details_v01.md        # Правила цветовых акцентов
    ├── charts/                           # Готовые промты для диаграмм
    │   ├── Spider_Chart_Manual.md
    │   ├── 5axis_Spider 0-10scale_v01.md
    │   ├── 5axis_Spider 0-10scale Template_v01.md
    │   ├── 6axis_Spider 0-10scale_v01.md
    │   ├── 6axis_Spider 0-10scale Template_v01.md
    │   ├── donut_v01.md
    │   ├── histogram_v01.md
    │   └── Spider 0-10scale_Examples.xlsx
    └── review/                           # Система ревью презентаций
        ├── review_manual.md
        ├── start_review.md
        ├── Example_review_context.md
        └── Example_review_result.md
```

### ✨ Характеристики стиля

**Основной стиль**
- **Техника:** чёрно-белый карандашный набросок, выполненный от руки
- **Фон:** чистый белый (по умолчанию) или глубокий чёрный (тёмный вариант)
- **Цветовые акценты:** добавляются только по явному запросу

**Визуальный язык**
- Эстетика ручного рисунка с естественными линиями
- Высокий контраст и чёткие силуэты
- Минималистичный подход с акцентом на главном
- Единообразная толщина штриха и фактура

### 🤖 Совместимость — как использовать эти промты

Файлы в этом репозитории — не код, а структурированные наборы инструкций/промтов, которые нужно передать AI-ассистенту, способному генерировать и редактировать изображения (обычно: прикрепить или вставить нужный файл инструкции как контекст в чат/проект, затем дать тему или Excel-эскиз в качестве входных данных — по схеме из раздела [Начало работы](#-начало-работы)).

> **Заметка для мейнтейнеров:** в README пока не указано, с каким именно AI-инструментом, моделью или приложением эта система разрабатывалась и тестировалась (конкретный ассистент, нужна ли поддержка «проектов»/кастомных инструкций, нужна ли загрузка файлов как вложений, встроена ли генерация изображений или это отдельный шаг). Если добавить эту информацию, новым пользователям не придётся выяснять это методом проб и ошибок.

### 📂 Доступные инструкции

| Файл | Описание | Когда использовать | Пример |
|------|----------|---------------------|--------|
| [init_creation_v01.md](Instruction/init_creation_v01.md) | Руководство по начальной настройке | Загружать первым при начале нового проекта | — |
| [slide_structure_types_v01.md](Instruction/slide_structure_types_v01.md) | Правила компоновки и структуры слайдов | Для оформления презентаций | — |
| [img01_main_char_v01.md](Instruction/img01_main_char_v01.md) | Иллюстрации с главным персонажем | Когда в кадре присутствует Роза | [пример](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/MainChar/00001_Roza%20on%20SkateBoard_DarkTheme_Color.webp) |
| [img02_no_char_v01.md](Instruction/img02_no_char_v01.md) | Иллюстрации без персонажей | Для предметов, сцен, понятий | — |
| [img03_icon_v01.md](Instruction/img03_icon_v01.md) | Иконки | Для элементов интерфейса, навигации | [пример](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Icons/10001_Protection_BaseTheme_Color.webp) |
| [img04_charts_v01.md](Instruction/img04_charts_v01.md) | Иллюстрации графиков и схем | Для наглядного представления данных | см. таблицу диаграмм ниже |
| [img05_background_v01.md](Instruction/img05_background_v01.md) | Фоновые иллюстрации | Для текстур и декоративных элементов | — |
| [img06_dark_theme_v01.md](Instruction/img06_dark_theme_v01.md) | Варианты в тёмной теме | Когда нужен чёрный фон | [пример](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/MainChar/00001_Roza%20on%20SkateBoard_DarkTheme_Color.webp) |
| [img07_color_details_v01.md](Instruction/img07_color_details_v01.md) | Правила использования цветовых акцентов | При добавлении цветных элементов | — |
| [img_cat_v01.md](Instruction/img_cat_v01.md) | Каталог категорий | Справочник по всем типам иллюстраций | — |

#### Система ревью презентаций
| Файл | Описание | Когда использовать |
|------|----------|---------------------|
| [review/review_manual.md](Instruction/review/review_manual.md) | Подробный чек-лист ревью | Для оценки готовых презентаций |
| [review/start_review.md](Instruction/review/start_review.md) | Промт для запуска ревью | Для начала процесса ревью с ИИ |
| [review/Example_review_context.md](Instruction/review/Example_review_context.md) | Пример контекста презентации | При подготовке контекста для ревью |
| [review/Example_review_result.md](Instruction/review/Example_review_result.md) | Пример отчёта по ревью | Для понимания формата результата |

#### Универсальные промты для диаграмм
| Файл | Описание | Когда использовать | Пример |
|------|----------|---------------------|--------|
| [charts/Spider_Chart_Manual.md](Instruction/charts/Spider_Chart_Manual.md) | Руководство по радиолокационным диаграммам | Для создания диаграмм-паутинок | — |
| [charts/5axis_Spider 0-10scale_v01.md](Instruction/charts/5axis_Spider%200-10scale_v01.md) | Промт для 5-осевой паутинки с готовым примером данных | Для радиолокационных диаграмм с 5 осями | [пример](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30001_SpiderChart_5axis.webp) |
| [charts/5axis_Spider 0-10scale Template_v01.md](Instruction/charts/5axis_Spider%200-10scale%20Template_v01.md) | Тот же промт для 5 осей, но с `[плейсхолдерами]` вместо примера данных | Когда нужно подставить свои категории/значения | [пример](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30001_SpiderChart_5axis.webp) |
| [charts/6axis_Spider 0-10scale_v01.md](Instruction/charts/6axis_Spider%200-10scale_v01.md) | Промт для 6-осевой паутинки с готовым примером данных | Для радиолокационных диаграмм с 6 осями | [пример](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30002_SpiderChart_6axis.webp) |
| [charts/6axis_Spider 0-10scale Template_v01.md](Instruction/charts/6axis_Spider%200-10scale%20Template_v01.md) | Тот же промт для 6 осей, но с `[плейсхолдерами]` вместо примера данных | Когда нужно подставить свои категории/значения | [пример](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Example_Imgs/Charts/30002_SpiderChart_6axis.webp) |
| [charts/donut_v01.md](Instruction/charts/donut_v01.md) | Промт для создания кольцевой диаграммы | Для создания диаграмм-бубликов | [пример](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Reference_Imgs/Charts/20001_Donut.webp) |
| [charts/histogram_v01.md](Instruction/charts/histogram_v01.md) | Промт для создания гистограммы | Для создания вертикальных столбчатых диаграмм | [пример](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate/resolve/main/Reference_Imgs/Charts/20002_Histogram.webp) |
| [charts/Spider 0-10scale_Examples.xlsx](Instruction/charts/Spider%200-10scale_Examples.xlsx) | Excel-шаблон с примерами | Для подготовки данных для паутинок | — |

**📚 Референсы стиля:** полный набор эталонных образцов — в [датасете LS_ImgCreate на Hugging Face](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate) (`Reference_Imgs/` — образцы стиля, `Example_Imgs/` — готовые примеры по всем категориям: персонаж, иконки, диаграммы, а не только диаграммы).

### 🚀 Начало работы

**1. Запуск проекта**
- Сначала загрузите `Instruction/init_creation_v01.md`
- Ознакомьтесь с порядком работы: уточнение задачи → планирование → создание → доработка

**2. Выберите тип иллюстрации**
- Главный персонаж? → `Instruction/img01_main_char_v01.md`
- Сцена без персонажей? → `Instruction/img02_no_char_v01.md`
- Иконки интерфейса? → `Instruction/img03_icon_v01.md`
- Наглядное представление данных? → `Instruction/img04_charts_v01.md`
- Паутинка со своими данными? → `Instruction/charts/Spider_Chart_Manual.md` + соответствующий **Template**-файл (5 или 6 осей) + [референс стиля](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)
- Паутинка, сначала хочется увидеть готовый пример? → файл без Template (5 или 6 осей)
- Кольцевая диаграмма? → `Instruction/charts/donut_v01.md` + [референс стиля](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)
- Гистограмма? → `Instruction/charts/histogram_v01.md` + [референс стиля](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)
- Фоны? → `Instruction/img05_background_v01.md`
- Тёмная тема? → `Instruction/img06_dark_theme_v01.md`
- Цветовые акценты? → `Instruction/img07_color_details_v01.md`
- Оформление слайдов? → `Instruction/slide_structure_types_v01.md`

**3. Ревью готовой презентации**
Когда презентация готова, используйте систему ревью:
1. Подготовьте контекст: опишите тему, аудиторию, цели (`Instruction/review/Example_review_context.md`)
2. Загрузите руководство по ревью (`Instruction/review/review_manual.md`)
3. Загрузите PDF-файл презентации
4. Используйте стартовый промт (`Instruction/review/start_review.md`)
5. Получите структурированную обратную связь с конкретными рекомендациями

**4. Следуйте порядку работы**
Каждая инструкция содержит:
- общие принципы и правила;
- технические требования;
- пошаговый процесс создания;
- критерии качества;
- типичные ошибки, которых следует избегать.

### 📋 Рекомендации

**Единообразие**
- Сохраняйте одинаковую толщину штриха во всех иллюстрациях
- Используйте согласованные пропорции для повторяющихся элементов
- Выдерживайте одинаковый уровень детализации во всей серии

**Композиция**
- Оставляйте достаточно свободного пространства
- Уравновешивайте визуальную нагрузку по всей площади рисунка
- Учитывайте предполагаемый размер и место отображения

**Правила для персонажа (Роза Ромашкина)**
- Сохраняйте узнаваемые черты лица
- Выдерживайте постоянные пропорции фигуры
- Передавайте характер персонажа через позы и выражения

**Организация файлов**
- Используйте понятные имена файлов
- Указывайте версию (v01, v02 и т. д.)
- Храните исходные файлы и готовые версии отдельно

### 🎨 Области применения

- **Презентации:** заголовки слайдов, иллюстрации к понятиям, схемы процессов, контроль качества
- **Визуализация данных:** радиолокационные диаграммы, кольцевые диаграммы, гистограммы, инфографика в едином стиле
- **Сайты и посадочные страницы:** обложки, иллюстрации к функциям, графика для призывов к действию
- **Маркетинг:** публикации в социальных сетях, баннеры, графика для рассылок
- **Документация:** иллюстрации к обучающим материалам, инфографика, пошаговые руководства

### 🔧 Технические требования

**Формат файлов**
- **Только WEBP** — качество 75%, низкая степень сжатия (уровень 2). Относится ко всем категориям: персонаж, иконки, диаграммы.
- Нужен PNG/PDF для печати или инструмента, не принимающего WEBP? Экспортируйте из WEBP-исходника, а не генерируйте сразу в этом формате — WEBP остаётся основным (каноничным) форматом вывода.

**Цветовые режимы**
- **Стандартный:** оттенки серого (чёрный карандаш на белом)
- **Тёмный вариант:** светлый карандаш на чёрном фоне
- **Цветовые акценты:** RGB для цифровых материалов, CMYK для печати

**Требования к размерам**
- **Иллюстрации главного персонажа:** 2048×2048 px, 1:1
- **Иконки:** 1024×1024 px, 1:1 (более мелкие растровые версии под конкретные места в интерфейсе получайте уменьшением этого исходника)
- **Иллюстрации без персонажа / фоны:** от 800×600 до 1920×1080 px *(в датасете таких примеров нет — считать рекомендацией, а не подтверждённой спецификацией)*
- **Радиолокационные диаграммы (паутинки):** соотношение сторон 1:1 (квадратный формат)
- **Кольцевые диаграммы, гистограммы:** соотношение сторон 2:1 (альбомный формат)
- **Фоны:** соответствуют размерам места отображения

Формат и размеры выше соответствуют подтверждённым примерам результата в [датасете LS_ImgCreate](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate).

### 💡 Советы

1. Начинайте с черновых набросков перед чистовым вариантом
2. Делайте несколько вариантов для сравнения
3. Проверяйте результат в том размере, в котором он будет отображаться
4. Получайте обратную связь перед утверждением
5. Используйте систему ревью для выявления упущенных проблем
6. Скачивайте референсы стиля с Hugging Face для персонажа, иконок и диаграмм в едином стиле
7. Записывайте принятые стилевые решения, чтобы использовать их в дальнейшем

### 🤝 Контрибьюция

Нашли несоответствие между инструкцией и реальным результатом, битую ссылку, или хотите добавить новый тип иллюстрации? Откройте issue или pull request в этом репозитории. При добавлении нового файла-промта, пожалуйста, также обновите его строку в таблице [Доступные инструкции](#-доступные-инструкции) и, по возможности, добавьте пример результата в сопроводительный датасет.

### 🔗 Связанные проекты

- **[Датасет LS_ImgCreate](https://huggingface.co/datasets/LeonidSmoliuk/LS_ImgCreate)** (Hugging Face) — примеры и референсные изображения, реально созданные по этим промтам, с разрешениями, правилами именования файлов и разбивкой по категориям.

### 📄 Лицензия

MIT License — свободное использование, изменение и распространение при условии указания источника.
