# Food Analyzer Telegram Bot

## Описание
Бот принимает фото еды (и опциональное описание), анализирует КБЖУ, состав, вес, определяет полезность (здоровое питание или нет).

## Файлы:
- `bot.py` — основной код бота
- `config.py` — конфиги (токены)
- `utils.py` — функции для анализа через OpenAI Vision
- `requirements.txt` — зависимости

## Быстрый старт

1. Склонируйте проект, создайте файл `.env` с переменными:
```
TELEGRAM_BOT_TOKEN=ваш_токен
OPENAI_API_KEY=ваш_openai_ключ
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Запустите бота:
```
python bot.py
```

## Гайд по деплою на Render

1. Создайте новый сервис на [render.com](https://dashboard.render.com/)
2. Укажите публичный репозиторий или залейте свой проект
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `python bot.py`
5. Добавьте переменные окружения `TELEGRAM_BOT_TOKEN` и `OPENAI_API_KEY`
6. Запустите сервис

Бот готов к работе!
