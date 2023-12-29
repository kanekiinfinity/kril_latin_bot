import logging

from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_latin, to_cyrillic

API_TOKEN = '6896619049:AAELk4Pm6QnnTmlh1fVERiRr_A_OkKseGag'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Salom\nKrill Lotin botimizga xush kelibsiz\nMatningizni yuboring.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    await message.answer(javob(msg))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)