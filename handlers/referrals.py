import sqlite3
from aiogram import types, Dispatcher, Bot
from aiogram.types import Update, InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, MEDIA_DEST
from database import db
from database.db import Database
from keyboards import inline_buttons
from const import PROFILE_TEXT
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.deep_linking import _create_link
import os
import binascii
from const import REFERRENS_MENU_TEXT


async def reference_menu(call: types.CallbackQuery):
    datab = Database()
    data = datab.sql_select_referrals_menu(
        owner=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=REFERRENS_MENU_TEXT.format(
            total_referrals=data["total_referrals"]
        ),
        reply_markup=await inline_buttons.balance_and_referral()
    )


async def generate_link(call: types.CallbackQuery):
    datab = Database()
    user = datab.sql_select_user(tg_id=call.from_user.id)
    #print(user["reference_link"])
    if not user["reference_link"] or user["reference_link"] is None:
        token = binascii.hexlify(os.urandom(8)).decode()
        link = await _create_link("start", payload=token)
        datab.sql_update_link(
            link=link,
            tg_id=call.from_user.id
        )
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Here is your link {link}"
        )
    else:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Here is your old link {user['reference_link']}"
            )

async def balance_button(call: types.CallbackQuery):
    datab = Database()
    data = datab.sql_select_referrals_menu(
        owner=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=f"Here is your Balance: {data['balance']}"
    )

async def referrals_button(call: types.CallbackQuery):
    datab = Database()
    referral = datab.sql_select_referrals_button(
        tg_id=call.from_user.id
    )
    if len(referral) == 0:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Here is your Referrals: {0}"
        )
    else:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Here is your Referrals: {referral}"
        )


def register_reference_handler(dp: Dispatcher):
    dp.register_callback_query_handler(reference_menu,
                                       lambda call: call.data == "referral")
    dp.register_callback_query_handler(generate_link,
                                       lambda call: call.data == "link")
    dp.register_callback_query_handler(balance_button,
                                       lambda call: call.data == "balance")
    dp.register_callback_query_handler(referrals_button,
                                       lambda call: call.data == "your_referrals")

