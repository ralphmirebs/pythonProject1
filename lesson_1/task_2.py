# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс
# Используйте форматирование строк.

total = int(input("Введите количество секунд "))
time_hour = total//3600           # целое количество часов
temp = total - (time_hour*3600)   # остаток в секундах (минуты+секунды)
time_min = temp//60               # целое количество минут
time_sec = temp - (time_min*60)   # целое количество секунд (только секунды)

if time_hour < 10:                # добавление нулей
    time_hour = '0'+str(time_hour)

if time_min < 10:
    time_min = '0'+str(time_min)

if time_sec < 10:
    time_sec = '0'+str(time_sec)

print(f'{time_hour} : {time_min} : {time_sec}')