from telegram import InlineKeyboardMarkup, InlineKeyboardButton


back_to_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Назад", callback_data="menu")],
    ]
)


auth_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton("", callback_data="")]]
)
