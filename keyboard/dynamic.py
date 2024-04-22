from telegram import InlineKeyboardMarkup, InlineKeyboardButton


start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Зарегистрироваться", callback_data="reg")],
        [InlineKeyboardButton("Авторизироваться", callback_data="auth")],
        [InlineKeyboardButton("Меню", callback_data="menu")],
    ]
)
