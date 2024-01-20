import re
import sqlite3
from aiogram import types, Dispatcher, Bot
from config import bot, MEDIA_DEST
from database.db import Database
from const import START_MENU, PROFILE_TEXT
from keyboards import inline_buttons
import random


async def my_profile_call(call: types.CallbackQuery):
    datab = Database()
    profile = datab.sql_select_profile(
        tg_id=call.from_user.id
    )
    print(profile)
    if profile:
        with open(profile['photo'], "rb") as photo:
            await bot.send_photo(
                chat_id=call.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=profile["nickname"],
                    bio=profile["bio"],
                    age=profile["age"],
                    gender=profile["gender"],
                    hobby=profile["hobby"],
                    zodiac_sign=profile["zodiac_sign"],
                ),
            )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="You didn't registered, please register!"
        )


async def random_filter_profile_call(call: types.CallbackQuery):
    datab = Database()
    profiles = datab.sql_select_all_profiles(owner=call.from_user.id)
    if not profiles:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="You have liked all profiles, come later!!"
        )
        return

    random_profile = random.choice(profiles)
    with open(random_profile['photo'], "rb") as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=PROFILE_TEXT.format(
                nickname=random_profile["nickname"],
                bio=random_profile["bio"],
                age=random_profile["age"],
                gender=random_profile["gender"],
                hobby=random_profile["hobby"],
                zodiac_sign=random_profile["zodiac_sign"],
            ),
            reply_markup=await inline_buttons.like_dislike(
                owner=random_profile['telegram_id'])
        )


async def detect_like_call(call: types.CallbackQuery):
    datab = Database()
    owner = re.sub("like_", "", call.data)
    try:
        datab.sql_insert_like(
            owner=owner,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U have liked this profile!"
        )
    finally:
        await call.message.delete()
        await random_filter_profile_call(call=call)


async def detect_dislike_call(call: types.CallbackQuery):
    datab = Database()
    owner = re.sub("dis_", "", call.data)
    try:
        datab.sql_insert_dislike(
            owner=owner,
            disliker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="U have disliked this profile!"
        )
    finally:
        await call.message.delete()
        await random_filter_profile_call(call=call)


def register_profile_handler(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        random_filter_profile_call,
        lambda call: call.data == "view_profiles"
    )
    dp.register_callback_query_handler(
        detect_like_call,
        lambda call: "like_" in call.data
    )
    dp.register_callback_query_handler(
        detect_dislike_call,
        lambda call: "dis_" in call.data
    )
