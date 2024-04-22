from telegram import InlineKeyboardMarkup, InlineKeyboardButton


back_to_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Назад", callback_data="menu")],
    ]
)


auth_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Ввести пароль", callback_data="auth_with_passw")],
        [InlineKeyboardButton("Отменить операцию", callback_data="menu")],
    ]
)


cancel_operation = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Отменить операцию", callback_data="menu")],
    ]
)
