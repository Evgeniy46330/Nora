# Nora — Telegram ChatGPT Assistant

## Описание
Нора — это Telegram-бот на базе OpenAI GPT, который отвечает с лёгким юмором и искрой.

## Установка и запуск

### Требования
- Python 3.11+
- Telegram Bot Token
- OpenAI API Key

### Локальный запуск

1. Клонируйте репозиторий
2. Создайте файл `.env` по примеру `.env.example` с вашими ключами
3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Запустите бота:
   ```
   python main.py
   ```

### Запуск в облаке (например, Koyeb)

1. Подключите репозиторий к Koyeb
2. Используйте Dockerfile для сборки и запуска
3. Добавьте переменные окружения в настройках сервиса:
   - TELEGRAM_BOT_TOKEN
   - OPENAI_API_KEY
   - SYSTEM_PROMPT (по желанию)

---

Вопросы и помощь: пиши Евгению или в репозиторий.
