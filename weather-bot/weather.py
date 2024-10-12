import httpx

from config_reader import settings_config


WEATHER_API_KEY = settings_config.weather_api_key.get_secret_value()
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'


async def get_weather(city: str) -> str:
    try:
        url = f'{BASE_URL}q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru'
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        data = response.json()

        if response.status_code != 200:
            return 'Не удалось получить погоду. Проверьте название города!'

        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        wind = data['wind']['speed']

        return (
            f'Погода в городе {city.capitalize()}:\n{weather.capitalize()}'
            f'\nТемпература: {temp}°C\nОщущается как: {feels_like}°C\nВетер: {wind} м/с'
        )

    except Exception as e:
        return f'При получении погоды в городе {city} произошла ошибка: {e}'
