#  Найти сумму и произведение цифр введённого пользователем трехзначного числа.

total = int(input("Введите трехзначное число "))
total_pos_1 = total // 100               # целые сотни
left = total % 100                       # остаток от деления на сто
total_pos_2 = left // 10                 # целые десятки
total_pos_3 = left % 10                  # целые единицы

summa = total_pos_1 + total_pos_2 + total_pos_3
mul = total_pos_1 * total_pos_2 * total_pos_3
print(f'Сумма {summa}, а произведение {mul}')

2