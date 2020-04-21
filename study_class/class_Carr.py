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


class Dimension():
    def __init__(self, lenght, width, height, mass):
        self.lenght = lenght
        self.width = width
        self.height = height
        self.wheelbase = random.randint(1501, 2100)

        self.mass = mass #  input("Enter mass Avto\t\t\t")





    def __str__(self):

        dimension = f"{self.width}x{self.height}, {self.mass} kg"
        return f"{dimension}"

    def square(self):
        s = self.lenght * self.width
        print(f"Square your Car is {s}")



class Characteristic(Car, Dimension):
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
    a = 10 * random.randrange(0, 125, 5)

    def __str__(self):
        return f"hello - Vital_ {self.speed} random number {self.a}"

    def speedy(self):
        if self.speed > 150:
            print("WAU. Your car is very fast")
        else:
            print("HA-HA, Your car is slow")
        print(f"Speed your avto is {self.speed} km/h")
        print(f"Speed your avto is {self} km/h - second print")  #  ось тут є різниця між попереднім прінтом-  в self
                                                                 # вкладується все, що після return


class Pilot(Speed, Characteristic):

    def __init__(self, model, year, color, seat, price, lenght, width, height, mass, speed):
        Characteristic.__init__(self, model, year, color, seat, price, lenght, width, height, mass)
        Speed.__init__(self)  # тут не передається жоден параметр, бо він не має жодного параметру - він має лише самого себе
        self.name = input("Enter your name\t\t\t")

    def order(self):
        print(f"{self.name}, you have avto marka = {self.model}, year= {self.year}, color = {self.color}, speed = {self.speed} ")


year = input("Enter car year\t\t\t")
color = input("Enter car color\t\t\t")
seat = input("Enter car seat\t\t\t")
price = input("Enter car price\t\t\t")
model = random.choice(['Renault', 'VW', 'Mercedes-Benz', 'Audi', 'Alfa-Romeo', 'BMW'])
lenght = random.randint(4150, 5520)
width = random.randint(1550, 1810)
height = random.randint(900, 1520)
mass = random.randint(400, 1500)

main_vehicle1 = Car(model, year, color, seat, price)

#  call static method in class Speed
max_sp = Speed()
max_sp.speedy()


print(f"time = {time.time()}")
own_car = Pilot(model, year, color, seat, price, lenght, width, height, mass=0, speed=0)
own_car.order()

dim = Dimension(lenght, width, height, mass)
dim.square()

print(f"your car have seat = {seat}")
i = 0
while 10 >= i:
    time.sleep(1)
    print(f"time for end {10 - i}")
    i += 1






