from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from data.config import ADMINS
from utils.db.sqlite import SQLiteBaza


router = Router()
data = SQLiteBaza('db.sqlite3')


@router.message(CommandStart())
async def do_start(message: Message):
    await message.answer(text="Hello")   
    user_id = message.from_user.id
    full_name = message.from_user.full_name

    users = data.read('Users')
    if users and any(i[0] == user_id for i in users):
        print('yes')
    else:
        try:
            data.insert('Users', user_id=user_id, full_name=full_name)
        except Exception as error:
            print("User qo'shishda xatolik: ", error)     