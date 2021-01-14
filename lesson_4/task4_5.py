# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
new_list = [i for i in range(100, 1001) if i % 2 == 0]  # формирование списка
print(new_list)

def multiply_all (prev_el, el):
    return prev_el * el

print (reduce(multiply_all, new_list))



