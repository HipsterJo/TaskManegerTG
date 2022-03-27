from tabnanny import check
from keyboards import Task
import datetime
from datetime import datetime, timedelta
#Считываем часы
def check_time(str, tsk):
    StartTime = str.split('-')[0]
    EndTime = str.split('-')[1]
    beginTime = check_minute(StartTime)
    deadlineTime = check_minute(EndTime)
    print('---------------')
    print(beginTime)
    print('\n' + deadlineTime)
    tsk.time = tsk.date + beginTime
    tsk.deadlineTime = tsk.deadlineTime + deadlineTime
    
#Выделяем минуты и часы
def check_minute(str):
    if (':' in str):
        hour = str.split(':')[0]
        minute = str.split(':')[1]
        print(hour)
        print('\n' +  minute)
        return(timedelta(0,0,0,0,int(minute), int(hour)))    
    else:
        return(timedelta(0,0,0,0,0,int(str),0))
            