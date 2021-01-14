# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def safe_division(a, b):
    """
    Безопасное деление
    :param a(float): делимое
    :param b(float): делитель
    :return: либо частное, либо none None + сообщение
    """
    try:
        a/b  # пытаемся поделить
    except ZeroDivisionError:  # не нашелся (выпало исключение)
        print("Error")
        return
    else:
        return a/b



a = float(input("Делимое ? "))
b = float(input("Делитель ? "))
print(f'Ответ: {safe_division(a,b)}')


