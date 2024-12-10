import logging, asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.state import UserState
from filters.admin import IsBotAdminFilter
from data.config import ADMIN


router = Router()

@router.message(Command('allusers'), IsBotAdminFilter(ADMIN))
async def get_all_users(message: Message):
    await message.answer(text="Users")
