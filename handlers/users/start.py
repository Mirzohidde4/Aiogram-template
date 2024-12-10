from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from data.config import ADMINS

router = Router()


@router.message(CommandStart())
async def do_start(message: Message):
    await message.answer(text="Hello")