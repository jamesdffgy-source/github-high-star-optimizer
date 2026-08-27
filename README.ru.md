# GitHub High-Star Optimizer

[English](README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português (Brasil)](README.pt-BR.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Türkçe](README.tr.md) · [Bahasa Indonesia](README.id.md)

<p align="center">
  <img src="docs/assets/github-high-star-optimizer-readme-hero.png" alt="Процесс GitHub High-Star Optimizer: Audit, Prepare, Apply и Publish без изменения кода." />
</p>

> Переносимый Skill на основе стандарта Agent Skills для Codex, Claude Code и совместимых платформ. Он превращает реальный существующий GitHub-проект в более понятный, убедительный и готовый к публикации репозиторий, не изменяя код продукта.

GitHub High-Star Optimizer улучшает только публичный слой проекта: позиционирование, структуру README, визуальные материалы с доказательной основой, метаданные репозитория, Release Notes, локализованные описания и этичные материалы запуска. Он не обещает количество Stars и не манипулирует вовлечённостью.

> Канонический источник — [README на английском](README.md). Перевод ещё не проверен носителем языка; при расхождениях ориентируйтесь на английскую версию.

## Что оптимизируется

- **Название и поиск:** соответствие словам задачи, текущие выборки поиска GitHub, коллизии, согласованность метаданных и стоимость переименования.
- **Ясность:** аудитория, проблема, результат, отличие и следующий шаг.
- **Доверие:** утверждения с доказательствами из репозитория, явные ограничения и реальные результаты.
- **Представление:** README Hero, Social Preview, изображение Release, бейджи и иерархия.
- **Распространение:** тексты под каждую платформу, сухой запуск, одобренная отправка через API/Webhook, вспомогательная очередь форумов, идемпотентность и журнал результатов.
- **Границы:** без изменений исходного кода, зависимостей, сборки, тестов, CI, конфигурации выполнения и поведения продукта.

## Четыре режима

| Режим | Что делает | Изменения |
|---|---|---|
| **Audit** | Оценивает публичный слой и расставляет приоритеты. | Нет |
| **Prepare** | Создаёт тексты и материалы в отдельном каталоге. | Нет |
| **Apply** | Применяет только явно одобренные некодовые файлы. | Только одобренный список |
| **Publish** | После разрешения обновляет метаданные, Releases или внешние страницы. | Только разрешённые действия |

## Быстрый старт

1. Клонируйте репозиторий.
2. Следуйте [руководству по установке](docs/INSTALLATION.md), чтобы установить внутренний каталог [`github-high-star-optimizer`](github-high-star-optimizer) в Codex, Claude Code или совместимую с Agent Skills платформу.
3. Используйте синтаксис вызова платформы и укажите реальный репозиторий или рабочее пространство.

```text
Use $github-high-star-optimizer to audit this existing repository.
Only optimize its public presentation and release package; do not change code.
```

## Правила достоверности

Каждое существенное утверждение должно опираться на файлы, Releases, демонстрации, Issues, факты пользователя или явно отмеченный вывод. Сгенерированные изображения не должны выдумывать интерфейс, вывод команд, метрики, интеграции, клиентов, функции или количество Stars. Покупка и обмен Stars, автоматическая активность и условные награды запрещены.

Полный процесс описан в [`github-high-star-optimizer/SKILL.md`](github-high-star-optimizer/SKILL.md), правила локализации — в [`multilingual-publishing.md`](github-high-star-optimizer/references/multilingual-publishing.md), автоматизация внешнего распространения — в [`distribution-automation.md`](github-high-star-optimizer/references/distribution-automation.md).

## Лицензия

[MIT](LICENSE)
