import logging
from keyboard.dynamic import start_kb
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
)
from db_api.database import DataBase
from handler.callback_handler import callback_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


class MyBot:
    def __init__(self, application: ApplicationBuilder, database: DataBase):
        self.application = application
        self.db = database

    async def start(self, update, context):
        user = update.effective_user
        full_name = f"{user.first_name} {user.last_name}"
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Приветствую, {full_name}, в боте!\nВыберите опцию!",
            reply_markup=start_kb,
        )

    def register_handlers(self):
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CallbackQueryHandler(callback_handler))

    def run(self):
        self.register_handlers()
        self.application.run_polling()
