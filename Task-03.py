# Третьяков Роман Викторович
# Факультет Geek University Python-разработки. Основы языка Python
# Урок 6. Задание 3:
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
# position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на
# словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker():

    def __init__(self, lname, fname, position, wage, bonus):
        self.lname = lname
        self.fname = fname
        self.position = position

        # Здесь могу ошибаться, не до конца понял суть задания про последний атрибут
        # Реализовал так: bonus задается в процентах от оклада, а в словарь записываю расчитанную сумму премии
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus':  self.wage * self.bonus / 100}

class Position(Worker):

    def get_full_name(self):
        return self.lname + ' ' + self.fname

    def get_total_income(self):
        return self._income.get('wage') +  self._income.get('bonus')

w1 = Position('Иванов', 'Иван', 'электромонтер', 1000, 25)
print('Фамилия', w1.lname)
print('Имя', w1.fname)
print('Должность', w1.position)
print('Полное имя', w1.get_full_name())
print('Оклад, руб.', w1.wage)
print('Размер премии, %', w1.bonus)
print('Размер дохода, руб.', w1.get_total_income())

w2 = Position('Петров', 'Петр', 'мастер', 1200, 30)
print(w2.lname)
print(w2.fname)
print(w2.position)
print(w2.get_full_name())
print(w2.get_total_income())
