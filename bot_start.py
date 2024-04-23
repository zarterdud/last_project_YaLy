from tg_bot_main import MyBot
from db_api.database import DataBase
from config import TOKEN, db_name
from telegram.ext import ApplicationBuilder


bot = ApplicationBuilder().token(TOKEN).build()
db = DataBase(db_name)

my_bot = MyBot(application=bot, database=db)
my_bot.run()
