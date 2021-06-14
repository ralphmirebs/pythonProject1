#  Реализовать проект расчета суммарного расхода ткани на производство одежды.
#  Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#  К типам одежды в этом проекте относятся пальто и костюм.
#  У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#  Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate_fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        if v < 1:
            self.__v = 1
        else:
            self.__v = v

    def calculate_fabric(self):
        return self.__v/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 1:
            self.__h = 1
            return
        if h > 210:
            self.__h = 210
            return
        self.__h = h

    def calculate_fabric(self):
        return 2 * self.__h + 0.3


c = Coat(8)
print(c.v)
print(c.calculate_fabric())

c2 = Coat(-8)
print(c2.v)
print(c2.calculate_fabric())

s = Suit(167)
print(s.h)
print(s.calculate_fabric())

s2 = Suit(-5)
print(s2.h)
print(s2.calculate_fabric())

s3 = Suit(500)
print(s3.h)
print(s3.calculate_fabric())

