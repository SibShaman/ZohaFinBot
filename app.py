from flask import Flask
import logging
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '5589747357:AAEiA78ZprfPUZ_dSar5SVB_Nr6FRfgExyI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)




@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons =  ['Доход', 'Расход']
    keyboard.add(*buttons)
    await message.reply('Какую операцию вы хотите совершить', reply_markup=keyboard)




@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)