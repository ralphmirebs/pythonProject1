#  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#  Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#  Выполнить подсчет средней величины дохода сотрудников.
line_data = []
with open("t5_3.txt", "w") as f_obj:
    while True:
        temp = input("Введите через пробел фамилию и зарплату: (пустая строка выход) ")
        if temp != "":
            line_data.append(temp+'\n')       # создаем список строк
        else:
            f_obj.writelines(line_data)       # записываем  целиком для сокращения обращений к накопителю
            break

line_data = []
with open("t5_3.txt", "r") as f_obj:
    line_data = f_obj.readlines()  # считали все в список

# элементы разобрать по пробелам и получить список пар (фамилия - зп)
ns_data = []
for i in range(len(line_data)):
    ns_data.append(line_data[i].split())

summa = 0
for i in range(len(ns_data)):
    if int(ns_data[i][1]) < 20000:
        print(f'{ns_data[i][0]} ')
        summa = summa + int(ns_data[i][1])

print(f'Средняя зп: {float(summa/len(ns_data))}')
