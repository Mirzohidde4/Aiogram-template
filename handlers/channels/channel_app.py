import logging, asyncio
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext


router = Router()

@router.channel_post()
async def group_messages(message: Message):
    await message.answer(text="channel")