# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
# нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class OC:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return  OC(self.cell_count + other.cell_count)

    def __sub__(self, other):
        if self.cell_count - other.cell_count <= 0:
            print("Разность должна быть положительная. Операция проигнорирована, клетка не изменилась")
            return OC(self.cell_count)
        return OC(self.cell_count - other.cell_count)

    def __mul__(self, other):
        return OC(self.cell_count * other.cell_count)

    def __truediv__(self, other):
        return OC(self.cell_count // other.cell_count)   # делим с округлением

    def make_order(self, cell_count_in_row):
        if cell_count_in_row == 0:                         # если число клеток в ряду ноль, то только сообщение
            print("нулевой ряд клеток")
            return
        cell_count_in_row += 1
        i = 1
        k = 1
        while i <= self.cell_count:
            print('*',  end='')
            k += 1
            if k == cell_count_in_row:
                print('\n', end='')
                k = 1
            i += 1
        print('\n')


c1 = OC(2)
c2 = OC(3)
c3 = c1 + c2
c3.make_order(2)

c4 = c3 - c1
c4.make_order(3)

c5 = c4 * c4
c5.make_order(4)

c6 = c5 / c2
c6.make_order(3)





