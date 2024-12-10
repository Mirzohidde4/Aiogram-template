from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from data.config import BOT_TOKEN
from aiogram.client.bot import DefaultBotProperties


bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))