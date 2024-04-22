from telegram import InlineKeyboardMarkup, InlineKeyboardButton


back_to_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Назад", callback_data="menu")],
    ]
)


auth_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Паролем", callback_data="auth_with_passw")],
        [InlineKeyboardButton("Имя + пароль", callback_data="auth_with_name_passw")],
        [InlineKeyboardButton("Username + пароль")]
    ]
)
