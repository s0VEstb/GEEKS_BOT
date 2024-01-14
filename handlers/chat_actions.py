import datetime
import sqlite3
from aiogram import types, Dispatcher
from config import bot, MEDIA_DEST, GROUP_ID
from database import db
from keyboards import inline_buttons
from const import START_MENU, BAN_USER_TEXT, BAN_COUNT_OFF, BAN_COUNT_ON
from profanity_check import predict_prob


async def chat_messages(message: types.Message):
    datab = db.Database()
    if message.chat.id == int(GROUP_ID):
        ban_words_predict = predict_prob([message.text])
        print(message.chat)
        if ban_words_predict > 0.8:
            potential = datab.sql_select_ban_user(
                tg_id=message.from_user.id
            )
            print(potential)
            if potential:
                if potential['count'] >= 3:
                    await bot.ban_chat_member(
                        chat_id=message.chat.id,
                        user_id=message.from_user.id,
                        until_date=datetime.datetime.now() + datetime.timedelta(minutes=5)
                    )
                    return
                datab.sql_update_ban_count(
                    tg_id=message.from_user.id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=BAN_USER_TEXT.format(
                        name=message.from_user.username,
                        count=potential['count'] + 1
                    )
                )
            elif not potential:
                datab.sql_insert_ban_user(
                    tg_id=message.from_user.id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=BAN_USER_TEXT.format(
                        name=message.from_user.username,
                        count=1
                    )
                )
            await message.delete()


async def check_ban_count(message: types.Message):
    datab = db.Database()
    user = datab.sql_select_ban_user(message.from_user.id)
    if user:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=BAN_COUNT_ON.format(
                name=message.from_user.username,
                count=user['count']
            ),
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=BAN_COUNT_OFF.format(
                name=message.from_user.username,
            ),
        )



def register_chat_actions_handler(dp: Dispatcher):
    dp.register_message_handler(chat_messages)
    dp.register_callback_query_handler(check_ban_count,
                                       lambda call: call.data == "start_check_ban_count")

