# # создание класса Vehicle
# class Vehicle:
#     def print_details(self):
#         print("Это родительский метод из класса Vehicle")
#
#
# # создание класса, который наследует Vehicle
# class Car(Vehicle):
#     def print_details(self):
#         print("Это дочерний метод из класса Car")
#
#
# # создание класса Cycle, который наследует Vehicle
# class Cycle(Vehicle):
#     def print_details(self):
#         print("Это дочерний метод из класса Cycle")
#
#
# car_a = Vehicle()
# car_b = Car()
# car_c = Cycle()
#
# car_a.print_details()
# car_b.print_details()
# car_c.print_details()

# создаем класс Car
class Car:

    # создаем конструктор класса Car
    def __init__(self, model):
        # Инициализация свойств.
        self.model = model

    # создаем свойство модели.
    @property
    def model(self):
        return self.__model

    # Сеттер для создания свойств.
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2018:
            self.__model = 2018
        else:
            self.__model = model

    def getCarModel(self):
        return "Год выпуска модели " + str(self.model)


carA = Car(2088)
print(carA.getCarModel())