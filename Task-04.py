# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 6. Задание 4:
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
# name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
# SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При
# значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Выполните вызов методов и также покажите результат.

# Я немного отошел от требования в задании, но требуемый функционал постарался весь охватить
class Car():

    def __init__(self, max_speed, color, name, is_police):
        self.max_speed = max_speed # здесь максимально возможная скорость для автомобиля. Определяю ее именно
                                   # в базовом классе, хотя в другом контексте можно было бы описать и в
                                   # дочерних классах
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Создан новый автомобиль {name}, цвет {color}')

    def show_speed(self, speed):
        # Для сокращения объема кода добавил проверку на превышение максимальной
        # скорости именно здесь, а не в дочерних классах
        self.speed = speed
        print(f'Скорость движения {self.speed} км/ч')
        if self.speed  > self.max_speed and not self.is_police: # здесь можно было бы сделать проверку на
                                                                # max_speed != 0  вместо is_police, так как
                                                                # под это определение могут попасть машины
                                                                # других экстренных служб
            print('Внимание! Превышение допустимой скорости!')

    def go(self):
        print(f'{self.name} начала движение')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это семейный автомобиль')

    def show_speed(self, speed):
        # В данном контексте этот метод не нужен, обработка превышения скорости производится
        # в родительском классе
        self.speed = speed
        super().show_speed(self.speed)


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это спортивный автомобиль')


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это служебный автомобиль')

    def show_speed(self, speed):
        # В данном контексте этот метод здесь не нужен, обработка превышения скорости производится
        # в родительском классе
        self.speed = speed
        super().show_speed(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Это полицейский автомобиль')


my_family_car = TownCar(60, 'черный', 'Honda Stepwgn Spada', False)
my_family_car.go()
my_family_car.show_speed(40)
my_family_car.show_speed(50)
my_family_car.show_speed(60)
my_family_car.turn('направо')
my_family_car.turn('налево')
my_family_car.stop()
print()

my_work_car = WorkCar(60, 'серый', 'Nissan Wingroad', False)
my_work_car.go()
my_work_car.show_speed(40)
my_work_car.stop()
print()

police_car = PoliceCar(0, 'белый', 'Toyota Crown', True)
print()

sport_car = SportCar(60, 'черный', 'Nissan GT-R', False)
sport_car.go()
sport_car.show_speed(60)
sport_car.show_speed(70)
police_car.go()
police_car.show_speed(80)
police_car.turn('налево')
police_car.turn('направо')
police_car.stop()
sport_car.stop()