import logging
from aiogram import Bot, Dispatcher, types, executor
from config import MY_API_KEY


# Подключение к боту    
logging.basicConfig(level=logging.INFO)
bot = Bot(token=MY_API_KEY)
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
   await message.answer("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())
# @dp.callback_query_handler(lambda c: c.data, state = StateMach.STATE_VIP)

@dp.message_handler(lambda message: message.text == 'Расход')
async def echo(message: types.Message):
    await message.answer("Не завидую!", reply_markup=types.ReplyKeyboardRemove())
# @dp.callback_query_handler(lambda c: c.data, state = StateMach.STATE_VIP)


# принимает сообщение и просто возвращает его обратно
@dp.message_handler()
async def echo(message: types.Message):    
    await message.answer (f'Вы ввели следующие данные {message.text}')




def start_bot():
    executor.start_polling(dp, skip_updates=True)


