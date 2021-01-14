#  Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
#  название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json
line_data = []
with open("t5_7.txt", "w", encoding="UTF-8") as f_obj:
    while True:
        temp = input("Через пробелы введите название, тип, выручка, издержки ")
        if temp != "":
            line_data.append(temp+'\n')       # создаем список строк
        else:
            f_obj.writelines(line_data)       # записываем  целиком для сокращения обращений к накопителю
            break

def convert(in_temp):
    """
    преобразование считанной строки в спискок
    :param in_temp: входная строка
    :return: список
    """
    name, typ, income, outcome = in_temp.split() # разбили по пробелам
    data_list = [name, typ, income, outcome]     # сделали список
    return data_list

with open("t5_7.txt", "r", encoding="UTF-8") as f_in_obj:
    dct = dict()
    while True:
        temp = f_in_obj.readline()     # прочитали строку
        if temp != "":                 # если не пустая (eof)
            data_list = convert(temp)      # вызвали функцию, она вернула список (название,тип,выручка,издержки)
            dct[data_list[0]] = int(data_list[2]) - int(data_list[3])   # формирование прибыли в первый элемент словаря
        else:
                          # в итоге, имеем словарь пар "нзвание-прибыль"
            summa = 0     # для суммы
            counter = 0   # для числа прибыльных фирм
            i_temp = list(dct.values())   # получаем список прибылей, из него надо проссумировать те, что положительные
            for i in i_temp:
                if i > 0:
                    summa += i
                    counter += 1
            temp = dict()              # cловарь для средней прибыли
            temp['average_profit'] = float(summa/counter)   # формирование словаря
            final_list = []            # результирующий список
            final_list.append(dct)
            final_list.append(temp)
            print(final_list)
            with open("t5_7_OUT.txt", "w", encoding="UTF-8") as f_obj:
                f_obj.write(json.dumps(final_list))
            break