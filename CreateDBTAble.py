from pickle import TRUE
import sqlite3
import datetime

#Преобразует дату в миллисекунды
def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

#Преобразует из миллисекунд в дату
def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

#Создает таблицу в бд с заданными параметрами 
def createTable():
    
      
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """CREATE TABLE IF NOT EXISTS tasks(
            user_id,
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
        cursor.execute(' INSERT INTO tasks (user_id, task_id, task_status, deadline, date, countTask) VALUES('+str(id_us)+', 0, 0 , 0, 0, ''); ')
        print('Мы тут')
        db.commit  

#передаем объект класса task
def createTask(tsk):
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        cursor.execute()  
