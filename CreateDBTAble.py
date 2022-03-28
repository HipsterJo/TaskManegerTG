from pickle import TRUE
import sqlite3
import datetime
from keyboards import Task
#Преобразует дату в миллисекунды
def get_timestamp(date_time):
    return datetime.datetime.timestamp(date_time)

#Преобразует из миллисекунд в дату
def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

#Создает таблицу в бд с заданными параметрами 
def createTable():
    
      
    with sqlite3.connect('db/database.db') as db:
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
    with sqlite3.connect('db/database.db') as db:
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
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        cursor.execute(' INSERT INTO tasks (user_id, task_id, task_status, deadline, date, countTask, note) VALUES('+str(id_us)+', 0, 0 , 0, 0,0, ''); ')
        print('Мы тут')
        db.commit  

def check_numberTask(id_us):
    with sqlite3.connect('db/database.db') as db:
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
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        #-------создаем уникальное id для задачи. В id пользователя дописываем количество его задач в целом------
        countTask = check_numberTask(us_id)
        #Узнаем количество цифр в количествве задач
        n = len(str(countTask))
        task_id = us_id * (10**n) + countTask
        cursor.execute('INSERT INTO tasks (user_id, task_id, task_status, deadline, date, countTask, notes) VALUES('+str(us_id)+','+str(task_id)+',0, '+str(get_timestamp(tsk.deadlineTime))+','+str(get_timestamp(tsk.time))+','+str(countTask)+',\''+tsk.note+'\')')
        print('Запись добавлена')