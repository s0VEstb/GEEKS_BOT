from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, Update, InlineKeyboardMarkup


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire !",
        callback_data="start_questionnaire"
    )
    check_count_button = InlineKeyboardButton(
        "Check Ban-Count",
        callback_data="start_check_ban_count"
    )
    registration_button = InlineKeyboardButton(
        "Registration !",
        callback_data="start_registration"
    )
    profile_button = InlineKeyboardButton(
        "Profile !",
        callback_data="my_profile"
    )
    view_profile_button = InlineKeyboardButton(
        "View Profiles",
        callback_data="view_profiles"
    )
    complaint_button = InlineKeyboardButton(
        "Complaint",
        callback_data="complaint"
    )
    referral_button = InlineKeyboardButton(
        "Referrals",
        callback_data="referral"
    )
    markup.add(questionnaire_button)
    markup.add(check_count_button)
    markup.add(registration_button)
    markup.add(profile_button)
    markup.add(view_profile_button)
    markup.add(complaint_button)
    markup.add(referral_button)
    return markup


async def delete_and_update():
    markup = InlineKeyboardMarkup()
    update_button = InlineKeyboardButton(
        "Update Profile",
        callback_data="update"
    )
    delete_button = InlineKeyboardButton(
        "Delete Profile",
        callback_data="delete"
    )
    markup.add(update_button)
    markup.add(delete_button)
    return markup


async def like_dislike(owner):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "Like 👍",
        callback_data=f"like_{owner}"
    )
    dislike_button = InlineKeyboardButton(
        "Dislike 👎",
        callback_data=f"dis_{owner}"
    )
    markup.add(like_button)
    markup.add(dislike_button)
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

async def balance_and_referral():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Generate Link",
        callback_data="link"
    )
    referral_button = InlineKeyboardButton(
        "Your Referrals",
        callback_data="your_referrals"
    )
    balance_button = InlineKeyboardButton(
        "Balance",
        callback_data="balance"
    )
    markup.add(link_button)
    markup.add(referral_button)
    markup.add(balance_button)
    return markup