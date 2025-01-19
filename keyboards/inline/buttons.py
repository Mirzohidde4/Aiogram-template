from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def CreateInline(*button_rows, just=(1,)) -> InlineKeyboardMarkup: #! {a: a, b: b}
    builder = InlineKeyboardBuilder()
    for row in button_rows:
        for text, callback_data in row.items():
            if callback_data.startswith('https:'):
                builder.add(InlineKeyboardButton(text=text,url=callback_data))
            else:
                builder.add(InlineKeyboardButton(text=text, callback_data=callback_data))
    builder.adjust(*just)
    return builder.as_markup()