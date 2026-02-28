# openclaw-docs

Этот репозиторий собирает документацию OpenClaw в один мастер-файл для загрузки в **NotebookLM**.

## Что здесь происходит

- Источник документации: локальная папка OpenClaw `docs`
  - `/var/lib/openclaw/.npm-global/lib/node_modules/openclaw/docs`
- Генератор: `scripts/build-master-docs.py`
- Результат: `MASTER_DOCS.md`
- Исключения из сборки: папки `zh-cn` и `ja-jp`

Во время сборки каждый markdown-файл из `docs` и подпапок добавляется в `MASTER_DOCS.md` отдельным блоком:
- подзаголовок `## <имя_файла.md>`
- строка с источником `_Source: <relative/path.md>_`

## Версионирование OpenClaw

- Текущая обработанная версия хранится в `OPENCLAW_VERSION.txt`.
- Это нужно, чтобы понимать, когда документация устарела относительно установленного OpenClaw.

## Еженедельное автообновление

Скрипт: `scripts/weekly-refresh.sh`

Логика:
1. Проверяет `openclaw --version`.
2. Сравнивает с версией в `OPENCLAW_VERSION.txt`.
3. Если версия выше:
   - пересобирает `MASTER_DOCS.md`,
   - обновляет `OPENCLAW_VERSION.txt`,
   - коммитит изменения,
   - пушит в `origin/main`.

Cron (понедельник, 12:00 UTC):

```cron
0 12 * * 1 /var/lib/openclaw/.openclaw/workspace/projects/openclaw-docs/scripts/weekly-refresh.sh >> /var/lib/openclaw/.openclaw/workspace/projects/openclaw-docs/weekly-refresh.log 2>&1
```

## Зачем это сделано

Основная цель — поддерживать один актуальный мастер-файл документации, который удобно загружать в **NotebookLM** для поиска, Q&A и контекстной работы с докой.
