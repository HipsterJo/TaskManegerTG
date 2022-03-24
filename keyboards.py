from tkinter.ttk import Button
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, ReplyKeyboardMarkup    
from datetime import datetime, date, time
from aiogram_calendar import simple_cal_callback, SimpleCalendar, dialog_cal_callback, DialogCalendar
from numpy import meshgrid

today = datetime.now()

#Класс "Задача"
class Task(object):
    
     def __init__(self):
         self.date = today.date()
         self.time = time(0,0)
         self.deadlineDate = date(2022,1,1)
         self.deadlineTime = time(0,0)
     def complete(self):
          self.complete = True    

#клавиатуры          
class Keyboards:
    def get_main_keyboard():
    #Главная клавиатура
        main_keybord = ReplyKeyboardMarkup(resize_keyboard= True)
        button_create_task = KeyboardButton('Создать запись')
        button_list_of_tasks = KeyboardButton('Посмотреть записи')
        main_keybord.add(button_create_task).add(button_list_of_tasks)
        
        return main_keybord
    def get_changeDate_keyboard():
        changeDate_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button_chageDate = KeyboardButton('Изменить дату задачи')
        button_changeTime = KeyboardButton('Изменить временной отрезок')
        changeDate_keyboard.add(button_chageDate).add(button_changeTime)
        
        return changeDate_keyboard
    #Клавиатура с часами
#    def get_time_keyboard():
#        time_keyboard  = InlineKeyboardMarkup()
#        creating_time_keyboard(time_keyboard)
#        return time_keyboard

    #Клавиатура с минутами
#    def get_minute_keyboard():
#        minute_keyboard = InlineKeyboardMarkup()
#        return minute_keyboard
         

#cоздание клавиатуры с часами        
#def creating_time_keyboard(time_keyboard):
#    start_number = 1
#    buttons = []
#    number= 0
#    
#    for i in range(6):
#        for j in range(4):
#            buttons.append(InlineKeyboardButton(str(number)+':00',callback_data= 'hour_'+ str(number)))
#            number = number + 1
#        time_keyboard.row(*buttons)
#        buttons = []
#    buttonRight = InlineKeyboardButton('➡', callback_data= 'right')
#    buttonLeft = InlineKeyboardButton('⬅', callback_data= 'left')
#    buttonCancel = InlineKeyboardButton('Обратно', callback_data='cancel')
#    time_keyboard.row(buttonLeft,buttonCancel,buttonRight)
   
#Создание клавиатуры с минутами
#def creating_minute_keyboard(minute_keyboard: types.InlineKeyboardMarkup, hour):
#    button00 = InlineKeyboardButton(hour + ':00', callback_data='minute_00')
#    button15 = InlineKeyboardButton(hour + ':15', callback_data='minute_15')
#    button30 = InlineKeyboardButton(hour + ':30', callback_data='minute_30')
#    minute_keyboard.row(button00, button15, button30, button45)
#    buttonRight = InlineKeyboardButton('➡', callback_data= 'right')
#    buttonLeft = InlineKeyboardButton('⬅', callback_data= 'left')
#    buttonCancel = InlineKeyboardButton('Обратно', callback_data='cancel')
#    minute_keyboard.row(buttonLeft,buttonCancel,buttonRight)



    

    