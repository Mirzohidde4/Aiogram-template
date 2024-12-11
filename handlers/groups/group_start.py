import logging, asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from states.state import UserState


router = Router()

@router.message(CommandStart())
async def group_messages(message: Message):
    await message.answer(text="group")
