import logging, asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states.state import UserState
from utils.db.sqlite import SQLiteBaza


router = Router()
data = SQLiteBaza('db.sqlite3')


@router.message(Command('allusers'))
async def get_all_users(message: Message):
    if data.read('Users'):
        users = ",\n".join(i[1] for i in data.read('Users'))
        await message.answer(text=users)
    else:
        await message.answer(text='User not found')
