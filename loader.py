from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties
import sys, logging
from data.config import BOT_TOKEN
from .handlers.users.start import user_private_router


bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dispatcher = Dispatcher()
dispatcher.include_router(user_private_router)


async def on_startup(bot):
    print('bot ishladi')

async def main():
    try:
        dispatcher.startup.register(on_startup)
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        await dispatcher.start_polling(bot)
    except:
        pass