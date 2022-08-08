# Класс общий и для расходов и для доходов
# Принимает сообщение (в двух видах  и текст)
#                   1. В виде текстового сообщения (парсим текст) 
#                   2. В виде голосового сообщения (перевести в текст, далее используем первый метод)

# Принимает инфу к какому классу обратиться чтобы отправить инфу по соответствующей статье (расход или доход)
# парсит его на составляющие 
#               - user
#               - количество денег, 
#               - статья (расходов или доходов)
#               - наименование проекта
#               - текст описание 
#               - дата записи 

# Отправляет сообщение Пользователю об успехе или неудаче 
#               - количество денег, 
#               - статья


from email.message import Message
import logging
from aiogram import Bot, Dispatcher, executor, types
from config import MY_API_KEY
from badget import Badget

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
   await message.reply("Отличный выбор!", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(lambda message: message.text == 'Расход')
async def echo(message: types.Message):
    await message.reply("Не завидую!", reply_markup=types.ReplyKeyboardRemove())


# принимаем сообщение и парсим его в список - пока экспериментальная функция, должна вернуть список значений (число и текст)
@dp.message_handler()
async def add_message(message: types.Message):
    amount = Badget.get_message(message.text)
    await message.answer (amount)

