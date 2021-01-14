# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_instruction(name, surname, birth, city, email, phone_number):
    """
    Печать информации о пользоватете одной строкой
    :param name(str): имя
    :param surname(str): фамилия
    :param birth(int): год рождения
    :param city(str): город проживания
    :param email(str): электронная почта
    :param phone_number(int): номер телефона
    :return: none
    """
    print(f'Меня зовут {name} {surname}, я родился в {birth} году. Ныне проживаю в городе {city}. Мне можно '
          f'написать на {email} или позвонить по номеру {phone_number}')


user_instruction("Ralph", "Mirebs", 2246, "Йокогама", "r@rinet.ru", 2191746)

