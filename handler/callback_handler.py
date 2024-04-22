from config import get_bot_and_db
from keyboard.static import (
    auth_keyboard,
    cancel_operation,
)
from keyboard.dynamic import start_keyboard
from datetime import datetime


async def callback_handler(update, context):
    data = datetime.now()
    bot, db = get_bot_and_db()
    user = update.effective_user
    tg_id = user.id
    chat_id = update.effective_chat.id
    callback_data = update.callback_query.data
    if callback_data == "menu":
        await update.effective_message.edit_text(
            f"Меню", reply_markup=start_keyboard(tg_id)
        )
    elif callback_data == "menu2":
        await update.effective_message.edit_text(
            f"Меню", reply_markup=start_keyboard(tg_id)
        )

    elif callback_data == "reg":
        await update.effective_message.edit_text(
            f"Введите пароль для конечной регистрации!",
        )

    elif callback_data == "auth":
        await update.effective_message.edit_text(
            f"Выберите тип авторизации", reply_markup=auth_keyboard
        )

    elif callback_data == "auth_with_passw":
        await update.effective_message.edit_text(
            text=f"Отправьте пароль",
            reply_markup=cancel_operation,
        )

    elif callback_data == "auth_with_name_passw":
        await update.effective_message.edit_text(
            text=f"Отправьте имя пользователя",
            reply_markup=cancel_operation,
        )

    elif callback_data == "parser":
        pass
