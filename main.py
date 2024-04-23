import logging
from keyboard.dynamic import start_keyboard
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ConversationHandler,
    filters,
)
from telegram import InlineKeyboardMarkup
from web.find_request import take_ans_request
from keyboard.static import back_to_menu_keyboard, cancel_operation
from db_api.database import DataBase
from handler.callback_handler import callback_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


class MyBot:
    def __init__(self, application: ApplicationBuilder, database: DataBase):
        self.application = application
        self.db = database
        self.password_state = 1
        self.reg_state = 1
        self.add_web_page = 1

    async def start(self, update, context):
        user = update.effective_user
        tg_id = user.id
        full_name = f"{user.first_name} {user.last_name}"
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Приветствую, {full_name}, в боте!\nВыберите опцию!",
            reply_markup=start_keyboard(tg_id),
        )

    async def write_name_web_page(self, update, context):
        await update.effective_message.edit_text(
            text="Напишите название web-страницы!",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[]),
        )
        return self.add_web_page

    async def handler_request(self, update, context):
        request = update.message.text
        if request.startswith("https://"):
            ans = take_ans_request(request)
            if ans:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"{ans}",
                    reply_markup=InlineKeyboardMarkup(inline_keyboard=[]),
                )
            else:
                await context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"Нет\n{ans}",
                    reply_markup=InlineKeyboardMarkup(inline_keyboard=[]),
                )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Введите корректный url адрес!",
                reply_markup=InlineKeyboardMarkup(inline_keyboard=[]),
            )
        return ConversationHandler.END

    async def write_password_register(self, update, context):
        await update.effective_message.edit_text(
            text="Введите пароль:", reply_markup=cancel_operation
        )
        return self.reg_state

    async def add_user_to_db(self, update, context):
        user = update.effective_user
        tg_id = user.id
        full_name = f"{user.first_name} {user.last_name}"
        username = user.username
        password = update.message.text
        self.db.register_user(tg_id, full_name, username, password)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Вы успешно зарегистрированны",
            reply_markup=back_to_menu_keyboard,
        )
        return ConversationHandler.END

    async def write_password(self, update, context):
        await update.effective_message.edit_text(
            text="Введите пароль:", reply_markup=cancel_operation
        )
        return self.password_state

    async def save_password(self, update, context):
        password = update.message.text
        tg_id = update.effective_user.id
        in_db = self.db.authorize_user(tg_id=tg_id, password=password)
        if in_db:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Вы успешно авторизованны!",
                reply_markup=back_to_menu_keyboard,
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"Ошибка, вы не найдены в системе",
                reply_markup=back_to_menu_keyboard,
            )
        return ConversationHandler.END

    async def cancel(self, update, context) -> int:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Вернуться",
            reply_markup=back_to_menu_keyboard,
        )
        return ConversationHandler.END

    def register_handlers(self):
        self.application.add_handler(
            ConversationHandler(
                entry_points=[
                    CallbackQueryHandler(
                        callback=self.write_name_web_page, pattern="parser"
                    )
                ],
                states={
                    self.add_web_page: [
                        MessageHandler(
                            filters.TEXT & ~filters.COMMAND, self.handler_request
                        ),
                    ],
                },
                fallbacks=[CommandHandler("cancel", self.cancel)],
            )
        )
        self.application.add_handler(
            ConversationHandler(
                entry_points=[
                    CallbackQueryHandler(
                        callback=self.write_password_register, pattern="reg"
                    )
                ],
                states={
                    self.reg_state: [
                        MessageHandler(
                            filters.TEXT & ~filters.COMMAND, self.add_user_to_db
                        ),
                    ],
                },
                fallbacks=[CommandHandler("cancel", self.cancel)],
            )
        )
        self.application.add_handler(
            ConversationHandler(
                entry_points=[
                    CallbackQueryHandler(
                        callback=self.write_password, pattern="auth_with_passw"
                    )
                ],
                states={
                    self.password_state: [
                        MessageHandler(
                            filters.TEXT & ~filters.COMMAND, self.save_password
                        ),
                    ],
                },
                fallbacks=[CommandHandler("cancel", self.cancel)],
            )
        )
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CallbackQueryHandler(callback=callback_handler))

    def run(self):
        self.register_handlers()
        self.application.run_polling()
