# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его
# нарушении выводить соответствующее сообщение и завершать скрипт.
import time
class TrafficLight:
    __color = ""

    def __init__(self):
        self.__color = "red"
        print(self.__color)

    def turn_red(self):
        self.__color = "red"
        print("Now is RED")
        time.sleep(7)

    def turn_yellow(self):
        self.__color = "yellow"
        print("Now is YELLOW")
        time.sleep(2)

    def turn_green(self):
        self.__color = "green"
        print("Now is GREEN")
        time.sleep(7)

    def running(self):
        self.turn_red()
        self.turn_yellow()
        self.turn_green()


tr = TrafficLight()
tr.running()


