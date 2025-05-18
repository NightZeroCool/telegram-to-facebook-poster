# Telegram to Facebook Poster (Lite)

Автоматически берёт посты из Telegram-канала, делает простой рерайт и публикует в Facebook-группу.

## Установка

1. Установите зависимости:
```
pip install -r requirements.txt
```

2. Создайте `.env` файл на основе `.env.example`

3. Запустите:
```
python scheduler.py
```

## Требования
- Chrome + chromedriver
- Аккаунт Telegram (api_id, api_hash)
- Аккаунт Facebook