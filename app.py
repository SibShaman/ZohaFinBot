# from flask import Flask
import logging
from aiogram import Bot, Dispatcher, executor, types

# from flask_sqlalchemy import SQLAlchemy


# API бота моего
API_TOKEN = '5589747357:AAEiA78ZprfPUZ_dSar5SVB_Nr6FRfgExyI'


# подключение бота
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# функция вывода первого сообщения (приветствия и выбора операции)
@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons =  ['Доход', 'Расход']
    keyboard.add(*buttons)
    await message.reply('Какую операцию вы хотите совершить', reply_markup=keyboard)
     



@dp.message_handler(lambda message: message.text == 'Доход')
async def echo(message: types.Message):
   
   await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())



@dp.message_handler(lambda message: message.text == 'Расход')
async def echo(message: types.Message):
   await message.reply("Не завидую", reply_markup=types.ReplyKeyboardRemove())



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)