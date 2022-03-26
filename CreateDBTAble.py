from pickle import TRUE
import sqlite3
import datetime

def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()


def createTable():
    
      
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """CREATE TABLE IF NOT EXISTS tasks(
            user_id,
            task_id INTEGER,
            task_status INTEGER,
            deadline INTEGER,
            date INTEGER
        )"""
        cursor.execute(query)
        db.commit  

def checkUser(id_us):
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query ="""SELECT user_id FROM tasks"""
        cursor.execute(query)
        for res in cursor:
            if (res[1] == id_us):
                return TRUE
        else:
            print('Имя пользователя не было найдено в БД. Пользватель добавлен') 
            createNewUser(id_us)
            
            

def createNewUser(id_us):
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        cursor.execute(' INSERT INTO tasks (user_id, task_id, task_status, deadline, date) VALUES('+str(id_us)+', 0, 0 , 0, 0); ')
        print('Мы тут')
        db.commit  

