import re
import sqlite3
from aiogram import types, Dispatcher, Bot
from config import bot, MEDIA_DEST
from database.db import Database
from const import START_MENU, PROFILE_TEXT
from keyboards import inline_buttons
import random
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class ComplaintsStates(StatesGroup):
    username = State()

async def complaint_by_user(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Send his Username"
    )
    await ComplaintsStates.username.set()


async def username_outputs(message: types.Message, state: FSMContext):
    datab = Database()
    compl_user = datab.sql_select_complainted_profile(message.text)
    if compl_user:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Your complaint has been accepted"
        )
        print(compl_user)
        comp_tg_id = datab.sql_select_id_from_username_profile(compl_user[0])
        print(comp_tg_id[0])
        await bot.send_message(
            chat_id=comp_tg_id[0],
            text="Your complaint, be careful"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="There is no such kind of user in my db"
        )
    await state.finish()
    compl_user = datab.sql_select_complaint_user(
        tg_id=message.from_user.id
    )
    print(0)
    if compl_user:
        print(compl_user['bad_count'])
        if compl_user['bad_count'] == 3:
            await bot.send_message(
                chat_id=comp_tg_id[0],
                text="Yoy have 3 or more counts, we will write about it soon."
            )
        datab.sql_update_bad_count(
            tg_id=message.from_user.id

        )
    elif not compl_user:
        try:
            datab.sql_insert_bad_user(
                complained_user=message.from_user.id,
                bad_user=comp_tg_id[0],
                reason="",
            )
        except sqlite3.IntegrityError:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="Error"
            )



def register_complaints_handler(dp: Dispatcher):
    dp.register_callback_query_handler(complaint_by_user,
                                lambda call: call.data == "complaint")
    dp.register_message_handler(username_outputs,
                                state=ComplaintsStates.username,
                                content_types=["text"])






