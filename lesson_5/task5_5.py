#  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random
data_list = []
with open("t5_5.txt", "w") as f_out_obj:
    for i in range(10):
        f_out_obj.write(str(random.randint(1, 100)))  # запись посимвольно, в итоге одна строка, в конце пробел
        f_out_obj.write(" ")

with open("t5_5.txt", "r") as f_in_obj:
    temp = f_in_obj.readline()

data_list = temp.split()   # удаляем пробелы
summa = 0
for i in range(len(data_list)):
    summa = summa + int(data_list[i])

print(f'Сумма: {summa}')
