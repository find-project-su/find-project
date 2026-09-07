<img class="logo-light" src="assets/fINd_logo_project_v01.webp" width="100" alt="Логотип Find Project">
<img class="logo-dark" src="assets/fINd_logo_project_v02.webp" width="100" alt="Логотип Find Project">

# f**IN**d Project

Добро пожаловать в систему документации, основанную на подходе **Docs as Code**.

## 🎨 Настройка оформления

Документация построена на теме **Material for MkDocs**, которая предоставляет широкие возможности кастомизации.

### 🌈 Цветовая палитра

Цвета задаются в файле `mkdocs.yml` через параметры `primary` и `accent`:

```yaml
theme:
  name: material
  palette:
    primary: teal    # Основной цвет (шапка сайта)
    accent: indigo   # Акцентный цвет (ссылки, кнопки)
```

??? tip "Доступные цвета для `primary`"
    - <span style="color:#EF5552">:material-circle:</span> `red` — красный
    - <span style="color:#E92063">:material-circle:</span> `pink` — розовый
    - <span style="color:#AB47BD">:material-circle:</span> `purple` — фиолетовый
    - <span style="color:#7E56C2">:material-circle:</span> `deep-purple` — тёмно-фиолетовый
    - <span style="color:#4051B5">:material-circle:</span> `indigo` — индиго
    - <span style="color:#2094F3">:material-circle:</span> `blue` — синий
    - <span style="color:#02A6F2">:material-circle:</span> `light-blue` — голубой
    - <span style="color:#00BBD4">:material-circle:</span> `cyan` — циан
    - <span style="color:#009485">:material-circle:</span> `teal` — сине-зелёный **(текущий)**
    - <span style="color:#4CAE50">:material-circle:</span> `green` — зелёный
    - <span style="color:#8BC34B">:material-circle:</span> `light-green` — светло-зелёный
    - <span style="color:#CBDC38">:material-circle:</span> `lime` — лаймовый
    - <span style="color:#FFEC3D">:material-circle:</span> `yellow` — жёлтый
    - <span style="color:#FFC105">:material-circle:</span> `amber` — янтарный
    - <span style="color:#FF9100">:material-circle:</span> `orange` — оранжевый
    - <span style="color:#FF6E42">:material-circle:</span> `deep-orange` — тёмно-оранжевый
    - <span style="color:#795649">:material-circle:</span> `brown` — коричневый
    - <span style="color:#757575">:material-circle:</span> `grey` — серый
    - <span style="color:#607D8B">:material-circle:</span> `blue-grey` — серо-голубой
    - <span style="color:#000000">:material-circle:</span> `black` — чёрный
    - <span style="color:#FFFFFF; text-shadow:0 0 1px #999999">:material-circle:</span> `white` — белый

**Примеры сочетаний:**

- <span style="color:#009485">:material-circle:</span> `primary: teal` + <span style="color:#3F51B5">:material-circle:</span> `accent: indigo` — **(текущее)**
- <span style="color:#2094F3">:material-circle:</span> `primary: blue` + <span style="color:#FF9100">:material-circle:</span> `accent: orange`
- <span style="color:#4051B5">:material-circle:</span> `primary: indigo` + <span style="color:#009485">:material-circle:</span> `accent: teal`

После изменения `mkdocs.yml` перезапустите сервер (`mkdocs serve`) или обновите страницу — изменения применятся автоматически.

### 💬 Типы выносок (admonitions)

Для выделения важной информации используйте специальные блоки.

??? info "Показать все типы выносок"
    ```markdown
    !!! note "Заметка"
        Обычная заметка (синий)

    !!! info "Информация"
        Информационный блок (голубой)

    !!! success "Успешно"
        Выполнено, работает (зелёный)

    !!! warning "Предупреждение"
        Будьте осторожны (оранжевый)

    !!! danger "Опасно"
        Критическая ошибка (красный)

    !!! tip "Совет"
        Полезная рекомендация (зелёный)
    ```

### 📂 Разворачивающиеся блоки

Сворачиваемые блоки создаются расширением `pymdownx.details` (оно уже включено в `mkdocs.yml` проекта). Синтаксис такой же, как у выносок, но вместо `!!!` используются вопросительные знаки.

**Свёрнутый по умолчанию (`???`):**

```markdown
??? note "Нажмите, чтобы развернуть"
    Скрытое содержимое блока (отступ 4 пробела).
```

**Развёрнутый по умолчанию (`???+`):**

```markdown
???+ note "Открыт сразу, можно свернуть"
    Содержимое видно сразу, но пользователь может свернуть блок.
```

**Цвет** блока зависит от типа (`note`, `info`, `success`, `warning`, `danger`, `tip`, `example`) — так же, как у обычных выносок.

??? example "Живой пример сворачиваемого блока"
    Это содержимое сворачиваемого блока.
    Внутри может быть любой Markdown.

    Например, список:

    - Пункт 1
    - Пункт 2

    Или код:

    ```bash
    mkdocs serve
    ```

⚠️ **Важно:** содержимое внутри блока должно иметь отступ **4 пробела**, иначе оно окажется снаружи блока.

### ✨ Эмодзи и иконки

В проекте включено расширение `pymdownx.emoji` с поддержкой иконок Material и стандартных эмодзи. Это позволяет оживить документацию визуальными элементами.

**Включение в `mkdocs.yml`:**

```yaml
markdown_extensions:
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
```

??? example "Обычные эмодзи"
    - `:smile:` → 😄
    - `:rocket:` → 🚀
    - `:warning:` → ⚠️
    - `:star:` → ⭐
    - `:check:` → ✅

??? example "Иконки Material (более 7000 вариантов)"
    - `:material-github:` → иконка GitHub :material-github:
    - `:fontawesome-brands-telegram:` → иконка Telegram :fontawesome-brands-telegram:
    - `:fontawesome-brands-python:` → иконка Python :fontawesome-brands-python:
    - `:material-book:` → иконка книги :material-book:
    - `:material-rocket-launch:` → иконка ракеты :material-rocket-launch:

    Полный каталог: [https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)

**Примеры использования:**

```markdown
Смотрите наш проект на :material-github: GitHub!

:fontawesome-brands-telegram: Пишите в Telegram для связи.

:material-check-circle: Все тесты пройдены!
```

??? note "Иконки с цветным стилем 🟥🟧🟨🟩🟦🟪"
    Иконки внутри `<span>` с цветным стилем позволяют создать цветные маркеры, как мы использовали в списке цветов палитры:
    
    <span style="color:#4CAE50">:material-github:</span> - цветная зеленая иконка GitHub
    
    Код: `<span style="color:#4CAE50">:material-github:</span>`

??? note "Брендовые иконки :fontawesome-brands-telegram: :fontawesome-brands-python:"
    Логотипы соцсетей и компаний (Telegram, Python, GitHub и др.) ищите в наборе `fontawesome-brands-*`, а не в `material-*`. В наборе Material брендовые иконки отсутствуют.
    
    | Если иконка не отображается | Замените на |
    |----------------------------|-------------|
    | `:material-telegram:` | `:fontawesome-brands-telegram:` |
    | `:material-python:` | `:fontawesome-brands-python:` |
    | `:material-git:` | `:fontawesome-brands-git:` |

### 🖼️ Логотип для разных тем

Цвет фона страницы меняется при переключении темы, поэтому логотип в **теле страницы** может становиться плохо видимым. Чтобы этого избежать, используются два варианта логотипа: один для светлой темы, другой для тёмной.

??? note "Как настроить переключаемый логотип"
    При переключении темы MkDocs Material добавляет на страницу атрибут `data-md-color-scheme` (`default` для светлой, `slate` для тёмной). Используем его, чтобы показывать нужный логотип.

    **Шаг 1.** Подготовьте два файла логотипа и положите их в `docs/assets/`:

    - `logo-light.webp` — версия для светлой темы
    - `logo-dark.webp` — версия для тёмной темы

    !!! tip "Имена файлов"
        Названия могут быть любыми — главное, чтобы они были понятными. Например, можно использовать название проекта: `myproject-logo-light.png`.

    **Шаг 2.** На странице вставьте обе картинки с классами:

    ```html
    <img class="logo-light" src="assets/logo-light.webp" width="100" alt="Логотип">
    <img class="logo-dark" src="assets/logo-dark.webp" width="100" alt="Логотип">
    ```

    **Шаг 3.** Добавьте правила в `docs/stylesheets/extra.css`:

    ```css
    /* Светлая тема: показываем светлую версию, прячем тёмную */
    [data-md-color-scheme="default"] .logo-dark {
      display: none;
    }

    /* Тёмная тема: показываем тёмную версию, прячем светлую */
    [data-md-color-scheme="slate"] .logo-light {
      display: none;
    }
    ```

    **Шаг 4.** Подключите `extra.css` в `mkdocs.yml`:

    ```yaml
    extra_css:
      - stylesheets/extra.css
    ```

    !!! tip "Про логотип в шапке"
        Переключать логотип в шапке сайта **не нужно** — шапка всегда одного цвета (задаётся параметром `primary`), поэтому там достаточно одного логотипа через `theme.logo`.

    Результат: при переключении темы логотип мгновенно меняется без перезагрузки страницы.

## 🔧 Расширения Markdown

??? note "Показать список расширений"
    В проекте включены полезные расширения:

    - **Tasklist** — чекбоксы для списков задач: `- [x] Выполнено`
    - **Snippets** — вставка кода из файлов: `--8<-- "путь/к/файлу.py:10:20"`
    - **Admonition** — цветные выноски
    - **Details** — сворачиваемые блоки
    - **Emoji** — эмодзи и иконки Material (`:material-...:`, `:smile:`)
    - **Attr list** — атрибуты для изображений: `![](image.png){ width=300 }`

## 🔗 Полезные ссылки

??? note "Показать список ссылок"
    - [Официальная документация MkDocs](https://www.mkdocs.org/)
    - [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
    - [GitHub репозиторий проекта](https://github.com/find-project-su/find-project)
    - [Опубликованная документация](https://find-project-su.github.io/find-project/)

---

*Эта страница редактируется в файле `docs/index.md`*