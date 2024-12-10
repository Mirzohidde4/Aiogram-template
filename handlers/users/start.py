from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from loader import db, bot
from data.config import ADMIN

user_private_router = Router()


@user_private_router.message(CommandStart())
async def do_start(message: types.Message):
    pass