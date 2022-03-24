
#Считываем часы
def check_time(str):
    StartTime = str.split('-')[0]
    EndTime = str.split('-')[1]
    check_minute(StartTime)
    print('---------------')
    print(StartTime)
    print('\n' + EndTime)
#Выделяем минуты и часы
def check_minute(str):
    if (':' in str):
        hour = str.split(':')[0]
        minute = str.split(':')[1]
        print(hour)
        print('\n' +  minute)