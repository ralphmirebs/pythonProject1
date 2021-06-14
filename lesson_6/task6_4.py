# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name}  goes')

    def stop(self):
        print(f'Car {self.name}  stoped')

    def turn(self, direction):
        print(f'Car {self.name}  turned to {direction}')

    def show_speed(self):
        print(f'Car {self.name}  now is  {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Speed above 60! Slow down!")
        else:
            print(f'Car {self.name}  now is  {self.speed}')


class SportCar(Car):
    def show_speed(self):
        if self.speed < 210:
            print("You are slow like a turtle")
        else:
            print(f'Car {self.name} is ready to race')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Speed above 40! Slow down!")
        else:
            print(f'Car {self.name}  now is  {self.speed}')


class PoliceCar(Car):
    def police_sound(self):
        if self.is_police:
            print("WaaaaaWaaaaaWaaaa!")
        else:
            print("engine sounds only")


toyota = TownCar(30, "Green", "TownAce", False)
ferrari = SportCar(240, "Red", "Testarossa", False)
tractor = WorkCar(80, "Yellow", "DT-75", False)
ford = PoliceCar(180, "Black", "Continental", True)

toyota.go()
toyota.turn("left")
toyota.show_speed()
toyota.stop()

tractor.go()
tractor.turn("back")
tractor.show_speed()
tractor.stop()

ferrari.show_speed()
ford.police_sound()






