# WeatherBot

WeatherBot — это Telegram-бот, созданный с использованием `aiogram`, который предоставляет информацию о погоде для любого города с использованием API OpenWeatherMap.

## Функциональность:

- Отправляет приветственное сообщение с инструкциями по использованию бота.
- Получает и отображает информацию о погоде для указанного города.

## Технологии и инструменты

- Python 3.12
- Aiogram
- Pre-commit
- Ruff
- Docker

## Установка и запуск проекта

1. Клонируйте репозиторий и перейдите в папку проекта:

    ```shell
    git clone git@github.com:babanlive/weather_bot.git && cd weather_bot
    ```

2. Создание файла .env
   - Создайте в папке приложения файл `.env` согласно образцу [.env_example](.env_example).

3. Запуск проекта через Docker
   - Для запуска в режиме разработки выполните команду:

    ```shell
    docker compose -f docker-compose.yaml up --build
    ```
    
##  [Проверить работу бота](https://t.me/quick_reply_weather_bot)

