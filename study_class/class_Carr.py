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
class Dimension():
    def __init__(self, lenght, width, height, mass):
        self.lenght = lenght
        self.width = width
        self.height = height
        self.wheelbase = random.randit(1501, 2100)
        self.mass = mass

    # ??? коли обовязково це писати??? воно буде виводити лише стрічки???
    def __str__(self):
        return S

    def square(self):
        S = self.lenght * self.width
        print(f"Square your Car is {S}")


class Characteristic(Car, Dimension):
# ??? чи можна його обявити через super().__init__і як це зробити????
    def __init__(self, model, year, color, seat, price, lenght, width, height, mass):
        Car.__init__(self, model, year, color, seat, price)
        Dimension.__init__(self, lenght, width, height, mass)

    def __str__(self):
        return
# ??? ЯК РОЗДРУКУВАТИ ВСІ ХАРАТЕРИТИКИ ОДРАЗУ З КЛАСУ Characteristic ???
    def param():
        print(Characteristic, self.height)


class Speed():
    speed = random.randint(100, 200)

    def __str__(self):
        return f"{speed}"

    @staticmethod # ??? не розумію чому змінну speed ця функція не бачить ???
    def speedy():
        if speed > 150:
            print("WAU. Your car is very fast")
        else:
            print("HA-HA, Your car is slow")

        print(f"Speed your avto is {speed} km/h")  # ??? як цей прінт повязаний з функцією def __str__(self): вище???


# ??? ЯК Speed ВКЛАСТИ В Pilot?
class Pilot(Speed, Characteristic):

    def __init__(self):
        super().__init__(self, model, year, color, seat, price, lenght, width, height, mass, name)
        self.name = input("Enter your name\t\t\t")

    def __str__(self):
        return # ??? що буде виводити отакий запис?

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

"""

