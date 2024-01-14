from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config('TOKEN')
MEDIA_DEST = config('MEDIA_DEST')
GROUP_ID = config('GROUP_ID')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)