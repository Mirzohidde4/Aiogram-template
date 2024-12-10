from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def Createreply(*args, contact=False, just=int) -> ReplyKeyboardBuilder: #! 'a', 'b', ..
    bulder = ReplyKeyboardBuilder()
    for i in args:
        bulder.add(KeyboardButton(text=i, request_contact=True if contact else False))
    bulder.adjust(just)
    return bulder.as_markup(resize_keyboard=True, one_time_keyboard=True)