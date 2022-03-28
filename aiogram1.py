from cgitb import text
import sqlite3
from ctypes import resize
from datetime import date
from email import message
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ReplyKeyboardMarkup    
from datetime import datetime, time, timedelta
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
from keyboards import Task, Keyboards
from States import Test
from Check_fun import check_time
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from CreateDBTAble import createTable,checkUser, createNewUser


Token = '1952198904:AAFC6hGtWaNDF8uMrZJwoVkQMZz-EVa6NbQ'

today = datetime.now()



bot = Bot(token=Token)
dp = Dispatcher(bot, storage=MemoryStorage())
new_task = Task() 
createTable()


main_keyboard = Keyboards.get_main_keyboard()
changeDate_keyboard = Keyboards.get_changeDate_keyboard()
#time_keyboard = Keyboards.get_time_keyboard()
#minute_keyboard = Keyboards.get_minute_keyboard()

#Старт программы
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):    
    await message.reply("Начинаем!", reply_markup=main_keyboard)
    us_id = int(message.from_user.id)
    checkUser(us_id)
   
#Создаем запись
@dp.message_handler(Text(equals = ('Создать запись')))
async def nav_cal_handler(message: Message):
    await message.answer("Please select a date: ", reply_markup=await SimpleCalendar().start_calendar())


# simple calendar usage
@dp.callback_query_handler(simple_cal_callback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
       
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await callback_query.message.edit_text(
            f'You selected {date.strftime("%d/%m/%Y")}'  
        )
        await callback_query.message.answer('Введите временной промежуток:')
        await Test.timing.set()
        new_task.deadlineDate = date
        print(date)
        
@dp.message_handler(state=Test.timing)
async def answer_q1(message:types.Message,state: FSMContext):
    check_time(message.text, new_task)
    print('--------------------')
    print(message.text)

#@dp.callback_query_handler(Text(startswith=('hour')))
#async def hour(call: types.CallbackQuery):
#    action = call.data.split("_")[1]
#    new_task.time = timedelta(hours=int(action), minutes= 0)
#    creating_minute_keyboard(minute_keyboard, action)
#    await call.message.delete_reply_markup()
#    await call.message.answer('Часы установлено', reply_markup=minute_keyboard)
   
#@dp.callback_query_handler(Text(startswith=('minute')))
#async def hour(call: types.CallbackQuery):
#    action = call.data.split("_")[1]
#    if (action.isdigit()):
#        temp = timedelta(minutes=int(action), hours=0)
#        new_task.time = new_task.time + temp
#        print(new_task.time)


     

if __name__ == '__main__':
    executor.start_polling(dp) 
    