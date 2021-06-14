#  По введенным пользователем координатам двух точек
#  вывести уравнение прямой вида y = kx + b, которая проходит через эти точки

print("Первая точка x/y")
x1 = float(input())
y1 = float(input())

print("Вторая точка x/y")
x2 = float(input())
y2 = float(input())


K = (y1-y2) * (x1-x2)
b = y2-(K*x2)

if b >= 0:
    print(f'у={K}x+{b}')
else:
    print(f'у={K}x{b}')









