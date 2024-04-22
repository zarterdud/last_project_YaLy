from db_api.database import DataBase
from telegram.ext import ApplicationBuilder

TOKEN = "7044106538:AAH9_X-BiUZd-YEdGJwlkLmDp6A1FUvx0ME"
db_name = "database.sqlite"
admins = [1077886176, 1283802964]


def get_bot_and_db():
    bot = ApplicationBuilder().token(TOKEN).build()
    db = DataBase(db_name)
    return bot, db
