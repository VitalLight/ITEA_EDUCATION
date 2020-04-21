"""
ПОГРАМА МАЄ ВИВЕСТИ ВИПАДКОВИЙ АВТОМОБІЛЬ ПРИ ЗАДАННІ ПЕВНИХ ХАРАКТЕРИСТИК
 І ЧЕРЕЗ 5 СЕКУНД ЗАПИТАТИ ЧИ ПРОДОВЖИТИ. ЯКЩО НЕ ВСТИГНУТИ ЗРОБИТИ ВИБІР АВТОМТИІНИЙ ВИХІД З ПРОГРАМИ.
"""
import random

import time


"""
мені не зрозуміло як створювати обєкт в самих класах, тобто в класі Dimension створити обєкт класу Car
"""
class Car():
    def __init__(self, model, year, color, seat, price):
        self. model = model
        self.year = year
        self.color = color
        self.seats = seat
        self.price = price

# не знаю чи буде щось друкувати чи ні
    def __str__(self):
        return main_vehicle1

# ??? ЯКЩО В ДУЖКАХ ПРОПИСАТИ self, ТО ВИБИВАЄ ПОМИЛКУ, ЧОМУ? ???
"""
Тому що тут ми вказуємо, від якого класу або класів цей клас наслідується, і коли пишете тут self,
то пайтон починає шукати змінну self, не знаходить її, і вибиває помилку
"""
class Dimension():
    def __init__(self, lenght, width, height, mass):
        self.lenght = lenght
        self.width = width
        self.height = height
        self.wheelbase = random.randint(1501, 2100)
        self.mass = mass

    # ??? коли обовязково це писати??? воно буде виводити лише стрічки???
    """
    тут немає такого, чи обовязково це писати, чи ні. цей метод означає, що повинно видрукуватися, коли
    ми конвертуємо обєкт типу Car у строку
    тобто якщо напишемо 
    d = Dimension(5, 4, 2, 2000)
    s = str(d)
    print(s)
    то на екран виведеться те, що ви вкажете в цьому методі

    Спробуйте запустити код вище, але поміняйте метод __str__ на ось такий

    def __str__(self):
        dimension = f"{self.width}x{self.height}, {self.mass} kg"

    """
    def __str__(self):
        return S

    def square(self):
        S = self.lenght * self.width
        print(f"Square your Car is {S}")


class Characteristic(Car, Dimension):
    # ??? чи можна його обявити через super().__init__і як це зробити????
    """
    Якщо ваш клас наслідується від декількох одночасно, то краще робити так, як ви вже зробили
    можна ось так
    super(Car, self).__init__(model, year, color, seat, price)
    super(Dimension, self).__init__(length, width, height, mass)
    """
    def __init__(self, model, year, color, seat, price, lenght, width, height, mass):
        
        Car.__init__(self, model, year, color, seat, price)
        Dimension.__init__(self, lenght, width, height, mass)

    def __str__(self):
        return
    # ??? ЯК РОЗДРУКУВАТИ ВСІ ХАРАТЕРИТИКИ ОДРАЗУ З КЛАСУ Characteristic ???
    """
    Не забувайте, що кожен метод має приймати аргумент self
    зробити це можна ось так

    def param(self):
        print(self.model, self.height, self.color, self.width, self.mass)
    """
    def param(self):
        print(Characteristic, self.height)


class Speed():
    speed = random.randint(100, 200)

    def __str__(self):
        return f"This is value from __str__ method in Speed class, {self.speed}"

    # ??? не розумію чому змінну speed ця функція не бачить ???
    """
    Тому що до неї також треба звертатися через self
    Спробуйте запустити ось це
    def speedy(self):
        if self.speed > 150:
            print("WAU. Your car is very fast")
        else:
            print("HA-HA, Your car is slow")

        print(f"Speed your avto is {self.speed} km/h")
        print(f"Speed your avto is {self} km/h")
    """
    @staticmethod 
    def speedy():
        if speed > 150:
            print("WAU. Your car is very fast")
        else:
            print("HA-HA, Your car is slow")

        print(f"Speed your avto is {speed} km/h")  # ??? як цей прінт повязаний з функцією def __str__(self): вище??? --- Ні, тому що видруковуєте поле обєкта, а не сам обєкт


# ??? ЯК Speed ВКЛАСТИ В Pilot?
"""
ви все зробили правильно
тільки в методі __init__ треба зробити так само, як зробили в класі Characteristic в методі ініт. Тобто треба викликати ініт 
двічі для обох класів, від яких наслідуєтеся
"""

class Pilot(Speed, Characteristic):

    def __init__(self):
        super().__init__(self, model, year, color, seat, price, lenght, width, height, mass, name)
        self.name = input("Enter your name\t\t\t")

    def __str__(self):
        return # ??? що буде виводити отакий запис? --- Нічого, None

    def order(self):
        print("всі характеристики з конструктора, але яка функція мене зрозуміє???")


year = input("Enter car year\t\t\t")
color = input("Enter car color\t\t\t")
seat = input("Enter car seat\t\t\t")
price = input("Enter car price\t\t\t")
model = random.choice(['Renault', 'VW', 'Mercedes-Benz', 'Audi', 'Alfa-Romeo', 'BMW'])
lenght = random.randint(4150, 5520)
width = random.randint(1550, 1810)
height = random.randint(900, 1520)


main_vehicle1 = Car(model, year, color, seat, price)

#  call static method in class Speed
Speed.speedy()

own_car = Pilot()
"""
як викликати методи в самому класі для обєкта, що в цьому ж класі(а не за ним) створений. чи таке можливо?
так, можливо, якщо я правильно зрозумів питання
уявіть що в класі Pilot у вас є 2 ось таких методи

    def order(self):
        print("всі характеристики з конструктора, але яка функція мене зрозуміє???")

    def say_hello(self):
        print("Зараз викличемо метод order")
        self.order()

коли запустите метод say_hello, то всередині нього викличеться метод order, який також знаходиться
всередині цього класу
"""