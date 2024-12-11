import logging, asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from states.state import UserState
from filters.group import GroupFilter
from data.config import ADMINS


router = Router()
router.message.filter()

@router.message(CommandStart(), GroupFilter())
async def group_messages(message: Message):
    await message.answer(text="group")
