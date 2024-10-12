from aiogram import F, Router, types
from aiogram.filters import CommandStart
from weather import get_weather


router = Router()

WELCOME_MESSAGE = '👋🏼 Привет, {}! \nЯ умею показывать погоду в вашем городе, \nвведите название города в чат.'


async def send_welcome_message(message: types.Message) -> None:
    await message.answer(WELCOME_MESSAGE.format(message.from_user.full_name), parse_mode='Markdown')


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await send_welcome_message(message)


@router.message(F.text)
async def city_weather(message: types.Message) -> None:
    city = message.text
    weather = await get_weather(city)
    await message.answer(weather)
