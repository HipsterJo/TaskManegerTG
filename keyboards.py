
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


today = datetime.now()


def create_buttons(id_tasks):
        Button1 = InlineKeyboardButton('Закончил', callback_data= 'Fin_' + str(id_tasks))
        Button2 = InlineKeyboardButton('Отложить', callback_data= 'Def_' + str(id_tasks))
        return Button1,Button2

def create_buttons_defer(id_tasks):
        Button1 = InlineKeyboardButton('На 30мин', callback_data= 'Che_1800_' + str(id_tasks))
        Button2 = InlineKeyboardButton('На 2часа', callback_data= 'Che_7200_' + str(id_tasks))
        Button3 = InlineKeyboardButton('На 6часов', callback_data= 'Che_21600_' + str(id_tasks))
        Button4 = InlineKeyboardButton('На 1день', callback_data= 'Che_86400_' + str(id_tasks))
        return Button1,Button2, Button3, Button4
#Класс "Задача"
class Task(object):
    
     def __init__(self):
         self.date = today.date()
         self.time = time(0,0)
         self.deadlineDate = date(2022,1,1)
         self.deadlineTime = time(0,0)
         self.note = ''
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
    def get_show_task_keyboard():
        show_task_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button_today = KeyboardButton('На сегодня')
        button_next3 = KeyboardButton('На 3 дня')
        button_next7 = KeyboardButton('На 7 дней')
        button_next30 = KeyboardButton('На 30 дней')
        button_cancel = KeyboardButton('Назад')
        show_task_keyboard.row(button_today, button_next3)
        show_task_keyboard.row(button_next7,button_next30)
        show_task_keyboard.row(button_cancel)
        return show_task_keyboard
    def get_changeDate_keyboard():
        changeDate_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        button_chageDate = KeyboardButton('Изменить дату задачи')
        button_changeTime = KeyboardButton('Изменить временной отрезок')
        changeDate_keyboard.add(button_chageDate).add(button_changeTime)
        
        return changeDate_keyboard

#___________Клавиатуры для ответа на карточки______________________


    def create_answer_keyboard(id_task):
        answer_keyboard = InlineKeyboardMarkup()
        ButtonFinish, ButtonDefer = create_buttons(id_task)
        answer_keyboard.row(ButtonDefer, ButtonFinish)
        return answer_keyboard

    def create_answer_keyboard_defer(id_task):
        answer_keyboard_defer = InlineKeyboardMarkup()
        Button30, Button2, Button6, Button1 = create_buttons_defer(id_task)
        answer_keyboard_defer.row(Button30, Button2)
        answer_keyboard_defer.row(Button6, Button1)
        return answer_keyboard_defer
    



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



    

    