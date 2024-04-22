from config import get_bot_and_db
from keyboard.static import back_to_menu_keyboard
from keyboard.dynamic import start_kb
from datetime import datetime
from db_api.database import DataBase


async def callback_handler(update, context):
    data = datetime.now()
    bot, db = get_bot_and_db()
    user = update.effective_user
    tg_id = user.id
    callback_data = update.callback_query.data
    if callback_data == "menu":
        await update.effective_message.edit_text(f"Меню", reply_markup=start_kb)
    elif callback_data == "reg":
        full_name = f"{user.first_name} {user.last_name}"
        username = user.username
        db.register_user(tg_id, full_name, username)
        current_data = f"{data.day}:{data.month:02}:{data.year}"
        await update.effective_message.edit_text(
            f"Вы были успешно зарегистрированны!\nДата: {current_data}",
            reply_markup=back_to_menu_keyboard,
        )
    elif callback_data == "auth":
        await update.effective_message.edit_text(f"Выберите тип авторизации", reply_markup=None)
    elif callback_data == "parser":
        pass
