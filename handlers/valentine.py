import sqlite3
from aiogram import types, Dispatcher
from aiogram.types import Update, InlineKeyboardMarkup, InlineKeyboardButton

from config import bot
from database import db
from keyboards import inline_buttons

async def valentine_start():
    markup = InlineKeyboardMarkup()
    valentine_button = InlineKeyboardButton(
        "Valentine",
        callback_data="valentine"
    )
    markup.add(valentine_button)
    return markup


async def valentine(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Will you be my valentine?",
        reply_markup=await valentine_answers()
    )


async def valentine_answers():
    markup = InlineKeyboardMarkup()
    val_yes_button = InlineKeyboardButton(
        "yes ❤️",
        callback_data="1"
    )
    val_no_button = InlineKeyboardButton(
        "no (",
        callback_data="0"
    )
    markup.add(val_yes_button)
    markup.add(val_no_button)
    return markup


async def no_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Are you sure?",
        reply_markup=await valentine_answers()
    )



async def no_answer_0(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Are you sure?",
        reply_markup=await valentine_answers_2()
    )
    print("wkmccwcw")

async def no_answer_2(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="2Are you sure?",
        reply_markup=await valentine_answers_3()
    )
    print(333333)

async def no_answer_3(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="3Are you sure?",
        reply_markup=await valentine_answers_4()
    )

async def no_answer_4(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="4Are you sure?",
        reply_markup=await valentine_answers_5()
    )

async def no_answer_5(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="5Are you sure?",
        reply_markup=await valentine_answers_final()
    )


async def yes_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Thank you!, i love u so much)",
    )


async def valentine_answers_2():
    markup = InlineKeyboardMarkup()
    val_yes_button = InlineKeyboardButton(
        "yes ❤️",
        callback_data="1"
    )
    val_no_button = InlineKeyboardButton(
        "no (",
        callback_data="2"
    )
    val_no_button_2 = InlineKeyboardButton(
        "no (",
        callback_data="2"
    )
    markup.add(val_yes_button)
    markup.add(val_no_button)
    markup.add(val_no_button_2)
    return markup



async def valentine_answers_3():
    markup = InlineKeyboardMarkup()
    val_yes_button = InlineKeyboardButton(
        "yes ❤️",
        callback_data="1"
    )
    val_no_button = InlineKeyboardButton(
        "no (",
        callback_data="3"
    )
    val_no_button_2 = InlineKeyboardButton(
        "no (",
        callback_data="3"
    )
    val_no_button_3 = InlineKeyboardButton(
        "no (",
        callback_data="3"
    )
    markup.add(val_yes_button)
    markup.add(val_no_button)
    markup.add(val_no_button_2)
    markup.add(val_no_button_3)
    return markup


async def valentine_answers_4():
    markup = InlineKeyboardMarkup()
    val_yes_button = InlineKeyboardButton(
        "yes ❤️",
        callback_data="1"
    )
    val_no_button = InlineKeyboardButton(
        "no (",
        callback_data="4"
    )
    val_no_button_2 = InlineKeyboardButton(
        "no (",
        callback_data="4"
    )
    val_no_button_3 = InlineKeyboardButton(
        "no (",
        callback_data="4"
    )
    val_no_button_4 = InlineKeyboardButton(
        "no (",
        callback_data="4"
    )
    markup.add(val_yes_button)
    markup.add(val_no_button)
    markup.add(val_no_button_2)
    markup.add(val_no_button_3)
    markup.add(val_no_button_4)
    return markup


async def valentine_answers_5():
    markup = InlineKeyboardMarkup()
    val_yes_button = InlineKeyboardButton(
        "yes ❤️",
        callback_data="1"
    )
    val_no_button = InlineKeyboardButton(
        "no (",
        callback_data="5"
    )
    val_no_button_2 = InlineKeyboardButton(
        "no (",
        callback_data="5"
    )
    val_no_button_3 = InlineKeyboardButton(
        "no (",
        callback_data="5"
    )
    val_no_button_4 = InlineKeyboardButton(
        "no (",
        callback_data="5"
    )
    val_no_button_5 = InlineKeyboardButton(
        "no (",
        callback_data="5"
    )
    markup.add(val_yes_button)
    markup.add(val_no_button)
    markup.add(val_no_button_2)
    markup.add(val_no_button_3)
    markup.add(val_no_button_4)
    markup.add(val_no_button_5)
    return markup


async def valentine_answers_final():
    markup = InlineKeyboardMarkup()
    val_yes_button = InlineKeyboardButton(
        "yes ❤️",
        callback_data="1"
    )
    markup.add(val_yes_button)
    return markup




def register_valentine_handler(dp: Dispatcher):
    dp.register_callback_query_handler(valentine,
                                       lambda call: call.data == "valentine")
    dp.register_callback_query_handler(no_answer_2,
                                       lambda call: call.data == "2")
    dp.register_callback_query_handler(yes_answer,
                                       lambda call: call.data == "1")
    dp.register_callback_query_handler(no_answer_3,
                                       lambda call: call.data == "3")
    dp.register_callback_query_handler(no_answer_4,
                                       lambda call: call.data == "4")
    dp.register_callback_query_handler(no_answer_5,
                                       lambda call: call.data == "5")
    dp.register_callback_query_handler(no_answer_0,
                                       lambda call: call.data == "0")

