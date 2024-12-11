import logging, asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.state import UserState


router = Router()

@router.message(Command('allusers'))
async def get_all_users(message: Message):
    await message.answer(text="Users")
