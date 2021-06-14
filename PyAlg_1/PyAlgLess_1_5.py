#  Пользователь вводит две буквы.
#  Определить их порядковый номер в алфавите и рассчитать число букв между ними.

abet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Введите первую букву ")
letter_1 = str(input())
print("Введите вторую букву ")
letter_2 = str(input())


num1 = abet.index(letter_1)+1
num2 = abet.index(letter_2)+1
delta_num = abs(num2 - num1)

print(num1, num2, delta_num)






