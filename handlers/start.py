import sqlite3
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.deep_linking import _create_link

from config import bot, MEDIA_DEST
from database import db
from keyboards import inline_buttons
from const import START_MENU
from scrapping.anime_scrapper import AnimeScrapper


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
    print(message.get_full_command())
    command = message.get_full_command()
    if command[1] != "":
        link = await _create_link("start", payload=command[1])
        owner = datab.sql_select_user_by_link(
            link=link
        )
        if owner["telegram_id"] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="You cant use own link",
            )
            return
        try:
            datab.sql_insert_referral(
                owner=owner["telegram_id"],
                referral=message.from_user.id
            )
            datab.sql_update_balance(
                owner=owner["telegram_id"]
            )
        except sqlite3.IntegrityError:
            pass

    with open(MEDIA_DEST + "booot.gif", "rb") as animation:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=animation,
            caption=START_MENU.format(
                name=message.from_user.first_name
            ),
            reply_markup=await inline_buttons.start_keyboard()
    )

async def anime_call(call: types.CallbackQuery):
    datab = db.Database()
    scraper = AnimeScrapper()
    data = scraper.parse_data()

    for link in data[:5]:
        datab.sql_insert_anime_link(link=link)
        await bot.send_message(
            chat_id=call.from_user.id,
            text=scraper.START_URL + link
        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])
    dp.register_callback_query_handler(anime_call,
                                       lambda call: call.data == "anime")
