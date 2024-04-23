from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from config import get_bot_and_db


bot, db = get_bot_and_db()


def start_keyboard(tg_id):
    for user in db.take_users():
        if tg_id == user[0]:
            if user[-1] == "True":
                return InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton("Парсер", callback_data="parser")],
                    ]
                )
            return InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton("Авторизироваться", callback_data="auth")],
                    [InlineKeyboardButton("Парсер", callback_data="parser")],
                ]
            )
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("Зарегистрироваться", callback_data="reg")],
            [InlineKeyboardButton("Парсер", callback_data="parser")],
        ]
    )
