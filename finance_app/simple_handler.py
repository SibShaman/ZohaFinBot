import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from config import MY_API_KEY


# Подключение к боту    
logging.basicConfig(level=logging.INFO)
bot = Bot(token=MY_API_KEY)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class FSMBase(StatesGroup):   
    """ Класс определяет состояние в котором находится бот для приема соответствуюших значений"""          
    balance = State()                       # определяет доход или расход
    amount = State()                        # сумма которая будет заносится в базу данных
    description = State()                   # описание (в дальнейшем отсюда будет парсится статья расходов или доходов)
    project = State()                       # название проекта по которому будет проходить соответствующая сумма


# функция вывода первого сообщения (приветствия и выбора операции)
@dp.message_handler(commands='start', state=None)
async def start_bot(message: types.Message):
        await FSMBase.balance.set()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
        markup.add('Доход', 'Расход')
        await message.reply('Какую операцию вы хотите совершить', reply_markup=markup)    


@dp.message_handler(state=FSMBase.balance)
async def load_balance(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['balance'] = message.text
    await FSMBase.next()
    await message.answer ('Введи сумму', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=FSMBase.amount)
async def load_amount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = message.text
    await FSMBase.next()
    await message.answer('Введи описание')


@dp.message_handler(state=FSMBase.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMBase.next()
    await message.answer('Сейчас введи название проекта')


@dp.message_handler(state=FSMBase.project)
async def load_project(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['project'] = message.text
    async with state.proxy() as data:
        await message.answer(str(data))             # дописать сохранение в словарь который пережается в соответствующий класс, в зависимости от нажатой кнопки
    await state.finish()




def run_bot():
    executor.start_polling(dp, skip_updates=True)


