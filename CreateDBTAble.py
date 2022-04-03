from pickle import TRUE
import sqlite3
import datetime
from keyboards import Task
import time
from datetime import date, timedelta
from datetime import  date, time

text = ['Тестовое сообщение',
'Посомтрим как работает'
]

#Преобразует дату в миллисекунды
def get_timestamp(date_time):
    return datetime.datetime.timestamp(date_time)

#Преобразует из миллисекунд в дату
def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp)

#Создает таблицу в бд с заданными столбцами 
def createTable():
    
      
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query = """CREATE TABLE IF NOT EXISTS tasks(
            user_id INTEGER,
            task_id INTEGER,
            task_status INTEGER,
            deadline INTEGER,
            date INTEGER,
            countTask INTEGER,
            notes TEXT
        )"""
        cursor.execute(query)
        db.commit  

#бесполезная херь
def checkUser(id_us):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query ="""SELECT user_id FROM tasks"""
        cursor.execute(query)
        for res in cursor:
            if (res[0] == id_us):
                print('Нашел')
                return TRUE
        else:
            print('Имя пользователя не было найдено в БД') 
            #createNewUser(id_us)
            
            
#бесполезная херь
def createNewUser(id_us):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute(' INSERT INTO tasks (user_id, task_id, task_status, deadline, date, countTask, note) VALUES('+str(id_us)+', 0, 0 , 0, 0,0, ''); ')
        print('Мы тут')
        db.commit()  

def check_numberTask(id_us):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        query ="""SELECT user_id FROM tasks"""
        cursor.execute(query)
        cnt = 0
        for res in cursor:
            if (res[0] == id_us):
                cnt= cnt+1
        return cnt        

#передаем объект класса task
def createTask(tsk: Task, us_id):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        #-------создаем уникальное id для задачи. В id пользователя дописываем количество его задач в целом------
        countTask = check_numberTask(us_id)
        #Узнаем количество цифр в количествве задач
        n = len(str(countTask))
        task_id = us_id * (10**n) + countTask
        cursor.execute('INSERT INTO tasks (user_id, task_id, task_status, deadline, date, countTask, notes) VALUES('+str(us_id)+','+str(task_id)+',0, '+str(get_timestamp(tsk.deadlineTime))+','+str(get_timestamp(tsk.time))+','+str(countTask)+',\''+tsk.note+'\')')
        print('Запись добавлена')
        db.commit()
        return True


def show_curreny_task(number,user_id):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        #query = 'SELECT deadline, date, notes FROM tasks WHERE date < '+str(get_timestamp(datetime.datetime.now() + timedelta(number))),' AND user_id ='+ str(user_id)+'\''
        #datetime.combine(date.today() + timedelta(number),time(0,0))
        # WHERE date < '+str(get_timestamp(datetime.datetime.now() + timedelta(number))),' AND user_id ='+ str(user_id)+'\'
        
        cursor.execute('SELECT deadline, date, notes, task_id FROM tasks WHERE user_id ='+ str(user_id)+' AND  date <' + str(get_timestamp(datetime.datetime.now() + timedelta(days= number)))+ ' AND date > ' + str(get_timestamp(datetime.datetime.today())) + ' AND task_status == 0')
        card= []
        id_tasks = []
        for res in cursor:
            card.append (f'План на день:{get_date(res[1]).date()}\n'
                         f'Время выполния: {get_date(res[1]).time()} - {get_date(res[0]).time()}\n'
                         f'Дела: {res[2]}' )
            id_tasks.append(res[3])
        return(card, id_tasks)            


def task_complete(id_task):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute(f'UPDATE tasks SET task_status = 1 WHERE task_id = {id_task}')
        db.commit()

def defer_task(id_task, ms):
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        new_date_time = 0
        new_deadline_time =0
        cursor.execute(f'SELECT date, deadline FROM tasks WHERE task_id = {id_task}')
        for res in cursor:
            new_date_time = int(res[0]) + int(ms)
            new_deadline_time = int(res[1]) + int(ms)
        cursor.execute(f'UPDATE tasks SET date = {new_date_time} WHERE task_id = {id_task}')
        cursor.execute(f'UPDATE tasks SET deadline = {new_deadline_time} WHERE task_id = {id_task}')
        db.commit()

def check_for_notifiection():
    now_in_sec = get_timestamp(datetime.datetime.now())
    
    with sqlite3.connect('database.db') as db:
        cursor = db.cursor()
        cursor.execute(f'SELECT date, deadline, notes, task_id, user_id FROM tasks WHERE task_status = 0')
        tasks = []
        for res in cursor:
            if ((res[0] - now_in_sec < 60) and (res[0] - now_in_sec) > 0):
                tasks.append(res)
                print(res )
        return tasks

