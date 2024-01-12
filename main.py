from aiogram import executor, Dispatcher
from config import dp
from handlers import start, questionnaire
from database import db


async def on_startup(_):
    datab = db.Database()
    datab.sql_create_tables()


start.register_start_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)


if __name__ == '__main__':
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )
