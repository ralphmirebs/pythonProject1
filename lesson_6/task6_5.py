# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки, использовали {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой, использовали {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом, использовали {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером, использовали {self.title}")


st = Stationery("хобот")
pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")

st.draw()
pen.draw()
pencil.draw()
handle.draw()