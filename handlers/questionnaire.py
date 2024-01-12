import sqlite3
from aiogram import types, Dispatcher
from config import bot
from database import db
from keyboards import inline_buttons


async def questionnaire(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You are human ?",
        reply_markup=await inline_buttons.human_answers()
    )


async def nomonkey_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="I know about it...",
        reply_markup=await inline_buttons.second_question()
    )

async def monkey_answers(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Dont lie you are a human!",
        reply_markup=await inline_buttons.second_question()
    )


async def male_question(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Your male ?",
        reply_markup=await inline_buttons.male_answers()
    )


async def male_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Yes, male is better than female",
        reply_markup=await inline_buttons.third_question()
    )


async def female_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Yes, female is better than male",
        reply_markup=await inline_buttons.third_question()
    )


async def programing_question(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Do you love programing ?",
        reply_markup=await inline_buttons.last_answers()
    )


async def prog_yes_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Great, Goog luck",
    )


async def prog_no_answer(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Then why a u programing ?",
    )

def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(questionnaire,
                                       lambda call: call.data == "start_questionnaire")
    dp.register_callback_query_handler(nomonkey_answer,
                                       lambda call: call.data == "human_yes")
    dp.register_callback_query_handler(monkey_answers,
                                       lambda call: call.data == "human_no")
    dp.register_callback_query_handler(male_question,
                                           lambda call: call.data == "next_question_yes")
    dp.register_callback_query_handler(male_answer,
                                       lambda call: call.data == "male(")
    dp.register_callback_query_handler(female_answer,
                                       lambda call: call.data == "female)")
    dp.register_callback_query_handler(programing_question,
                                       lambda call: call.data == "last_question_yes")
    dp.register_callback_query_handler(prog_yes_answer,
                                       lambda call: call.data == "programing_yes")
    dp.register_callback_query_handler(prog_no_answer,
                                       lambda call: call.data == "programing_no")
