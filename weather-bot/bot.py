import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from config_reader import settings_config
from dotenv import load_dotenv
from handlers import router


load_dotenv()


async def main():
    bot = Bot(token=settings_config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.include_router(router=router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
