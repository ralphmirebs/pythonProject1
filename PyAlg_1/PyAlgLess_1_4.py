# Написать программу, которая генерирует в указанном пользователем диапазоне:
# случайное целое число
# случайное вещественное число
# случайный символ
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Если надо получить случайный символ от 'a' до 'f', вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
print("Выберите режим (int/fl/ch) ")
mode = str(input())
if mode == "int":
    print("from? ")
    start = int(input())
    print("to? ")
    finish = int(input())
    print(random.randint(start, finish))

elif mode == "fl":
    print("from? ")
    start = float(input())
    print("to? ")
    finish = float(input())
    print(random.uniform(start, finish))

elif mode == "ch":
    print("from? ")
    start = ord(str(input()))
    print("to? ")
    finish = ord(str(input()))
    print(chr(random.randint(start, finish)))








