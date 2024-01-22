import sqlite3
from aiogram import types, Dispatcher, Bot
from config import bot, MEDIA_DEST
from database import db
from database.db import Database
from keyboards import inline_buttons
from const import START_MENU, PROFILE_TEXT
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup






class RegisterStates(StatesGroup):
    nickname = State()
    bio = State()
    age = State()
    gender = State()
    hobby = State()
    zodiac_sign = State()
    photo = State()


async def register_start(call: types.CallbackQuery):
    datab = Database()
    datab.sql_delete_profile(call.from_user.id)
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Send your Nickname"
    )
    await RegisterStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)
    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send your Bio"
    )
    await RegisterStates.next()


async def load_bio(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="How old are you?\n"
             "Only numeric age!"
    )
    await RegisterStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Send me ONLY numeric\n"
                 "Registration FAILED, Restart."
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send me your gender\n"
             "Only male or female!"
    )
    await RegisterStates.next()


async def load_gender(message: types.Message,
                      state: FSMContext):
    genders = ['male', 'female']
    if message.text.lower() in genders:
        async with state.proxy() as data:
            data['gender'] = message.text
            print(data)

        await bot.send_message(
            chat_id=message.from_user.id,
            text="what is your hobby?"
        )
        await RegisterStates.next()
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="ONLY Male and Female\n"
                 "Registration FAILED!"
        )
        await state.finish()


async def load_hobby(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send your zodiac sign"
    )
    await RegisterStates.next()


async def load_zodiac_sign(message: types.Message,
                           state: FSMContext):
    async with state.proxy() as data:
        data['zodiac_sign'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Send your photo\n"
             "Only in photo mode sender"
    )
    await RegisterStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DEST
    )
    async with state.proxy() as data:
        db.sql_insert_profile(
            tg_id=message.from_user.id,
            nickname=data["nickname"],
            bio=data["bio"],
            age=data["age"],
            gender=data["gender"],
            hobby=data["hobby"],
            zodiac_sign=data["zodiac_sign"],
            photo=path.name,
        )

        with open(path.name, "rb") as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=data["nickname"],
                    bio=data["bio"],
                    age=data["age"],
                    gender=data["gender"],
                    hobby=data["hobby"],
                    zodiac_sign=data["zodiac_sign"],
                ),
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text="You have successfully updated\n"
                 "Congratulations!"
        )
    await state.finish()



def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        register_start,
        lambda call: call.data == "update"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegisterStates.nickname,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_bio,
        state=RegisterStates.bio,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_age,
        state=RegisterStates.age,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_gender,
        state=RegisterStates.gender,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_hobby,
        state=RegisterStates.hobby,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_zodiac_sign,
        state=RegisterStates.zodiac_sign,
        content_types=["text"]
    )
    dp.register_message_handler(
        load_photo,
        state=RegisterStates.photo,
        content_types=types.ContentTypes.PHOTO
    )