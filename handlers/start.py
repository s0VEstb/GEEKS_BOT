import sqlite3
from aiogram import types, Dispatcher
from config import bot, MEDIA_DEST
from database import db
from keyboards import inline_buttons
from const import START_MENU


async def start_button(message: types.Message):
    datab = db.Database()
    try:
        datab.sql_insert_user(
            tg_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name
        )
    except sqlite3.IntegrityError:
        pass
    print(message)

    #await bot.send_message(
    #    chat_id=message.from_user.id,
    #    text=f"Hello {message.from_user.first_name}",
    #    reply_markup=await inline_buttons.start_keyboard()
    #)

    with open(MEDIA_DEST + "booot.gif", "rb") as animation:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=animation,
            caption=START_MENU.format(
                name=message.from_user.first_name
            ),
            reply_markup=await inline_buttons.start_keyboard()
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])