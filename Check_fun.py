from keyboards import Task
import datetime
from datetime import datetime, timedelta, time, date
#Считываем часы
def check_time(str, tsk: Task, ):
    StartTime = str.split('-')[0]
    print('________')
    print(StartTime)
    EndTime = str.split('-')[1]
    
    print('________')
    beginTime = check_minute(StartTime)
    deadlineTime = check_minute(EndTime)
    print('---------------')
    print(beginTime)
    print('\n')
    print(deadlineTime)
    tsk.time = datetime.combine(tsk.deadlineDate,tsk.time) + beginTime
    tsk.deadlineTime = datetime.combine(tsk.deadlineDate,tsk.deadlineTime) + deadlineTime
    print(tsk.time)
    print(tsk.deadlineTime)
    
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
            