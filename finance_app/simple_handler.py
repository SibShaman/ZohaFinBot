import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, types, executor
from config import MY_API_KEY


# Подключение к боту
logging.basicConfig(level=logging.INFO)
bot = Bot(token=MY_API_KEY)

# временное хранилище, только до перезапуска состояния бота (до state.finish(),
# после этого память обнуляется)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class FSMBase(StatesGroup):
    """ Класс определяет состояние в котором находится бот
    и принимает соответствуюшие значения в словарь который передается дальше по логике"""
    # определяет доход или расход
    balance = State()
    # сумма которая будет заносится в базу данных
    amount = State()
    # описание (в дальнейшем отсюда будет парсится статья расходов или доходов)
    description = State()
    # название проекта по которому будет проходить соответствующая сумма
    project = State()


# функция вывода первого сообщения (приветствия и выбора операции)
@dp.message_handler(commands='start', state=None)
async def start_bot(message: types.Message):
    """ some func"""
    await FSMBase.balance.set()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add('Доход', 'Расход')
    await message.reply('Какую операцию вы хотите совершить', reply_markup=markup)
    # добавить проверку в каком состоянии находится бот в момент запуска


# передача значения во временную память, сохранение результата в balance
@dp.message_handler(state=FSMBase.balance)
async def load_balance(message: types.Message, state: FSMContext):
    """ some func"""
    async with state.proxy() as data:
        data['balance'] = message.text
    await FSMBase.next()            # переключаемся на следующее состояние amount
    await message.answer ('Введи сумму', reply_markup=types.ReplyKeyboardRemove())
    # добавить проверку на числовое значение этого поля


# добавление  и сохранение значения amount (сумма) в словарь
@dp.message_handler(state=FSMBase.amount)
async def load_amount(message: types.Message, state: FSMContext):
    """ some func"""
    async with state.proxy() as data:
        data['amount'] = message.text
    await FSMBase.next()
    await message.answer('Введи описание')


# добавление  и сохранение значения descriptioin (описание) в словарь
@dp.message_handler(state=FSMBase.description)
async def load_description(message: types.Message, state: FSMContext):
    """ some func"""
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMBase.next()
    await message.answer('Сейчас введи название проекта')


# добавление  и сохранение значения project (проект) в словарь
@dp.message_handler(state=FSMBase.project)
async def load_project(message: types.Message, state: FSMContext):
    """ some func"""
    async with state.proxy() as data:
        data['project'] = message.text
    async with state.proxy() as data:
        # дописать сохранение в словарь который передается в соответствующий класс,
        # в зависимости от нажатой кнопки
        await message.answer(str(data))
    await state.finish()
    # добавить проверку что такой проект существует



def run_bot():
    """ run bot"""
    executor.start_polling(dp, skip_updates=True)
