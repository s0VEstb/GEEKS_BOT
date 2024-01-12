from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire !",
        callback_data="start_questionnaire"
    )
    markup.add(questionnaire_button)
    return markup


async def human_answers():
    markup = InlineKeyboardMarkup()
    human_yes_button = InlineKeyboardButton(
        "Yes i am.",
        callback_data="human_yes"
    )
    human_no_button = InlineKeyboardButton(
        "No i am a monkey!",
        callback_data="human_no"
    )
    markup.add(human_yes_button)
    markup.add(human_no_button)
    return markup

async def second_question():
    markup = InlineKeyboardMarkup()
    second_question_button = InlineKeyboardButton(
        "Next Question",
        callback_data="next_question_yes"
    )
    markup.add(second_question_button)
    return markup


async def male_answers():
    markup = InlineKeyboardMarkup()
    male_button = InlineKeyboardButton(
        "i am a male >:(",
        callback_data="male("
    )
    female_button = InlineKeyboardButton(
        "i am a female <:)",
        callback_data="female)"
    )
    markup.add(male_button)
    markup.add(female_button)
    return markup


async def third_question():
    markup = InlineKeyboardMarkup()
    third_question_button = InlineKeyboardButton(
        "Last Question",
        callback_data="last_question_yes"
    )
    markup.add(third_question_button)
    return markup


async def last_answers():
    markup = InlineKeyboardMarkup()
    programing_yes_button = InlineKeyboardButton(
        "Yes i do",
        callback_data="programing_yes"
    )
    programing_no_button = InlineKeyboardButton(
        "No, i hate it",
        callback_data="programing_no"
    )
    markup.add(programing_yes_button)
    markup.add(programing_no_button)
    return markup