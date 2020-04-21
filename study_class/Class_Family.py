import random
import time
from PIL import Image



class Family():
    while True:
        try:
            age = int(input(" Enter your age \t\t\t"))
            break
        except ValueError:
            print("Enter your age in number format !!!")
            continue


    def drive(self):
        if self.age > 18:
            print("OK. You have a drive license")
        else:
            print("You are very young )")


    def eat(self):
        size = (180, 2000)
        with Image.load("index.jpg") as f_im:
        # with Image.open("index.jpg") as f_im:
        # f_im = Image.open("index.jpg")
            f_im.thumbnail(size)
        i = 0
        while i <= 30:
            f_im = Image.open("index.jpg")
            f_im.thumbnail(size)
            f_im.rotate(random.randrange(360)).show()
            time.sleep(0.1)
            f_im.close()
            # f_im.load()
            i += 1


        print("Family can eat")


    def meet(self):
        print("Family can meet")


class Mother(Family):

    def cooking(self):
        print("Mother can cooking")


    def love(self):
        a = random.randrange(50)
        c = a * a
        print("Mother can Love")
        return f"Mother can Love very much rate  = {c}"


    def support(self):
        print("Mother can support")


class Father(Family):

    def strong(self):
        print("Father strong")


    def driver(self):
        print("Father driver")


    def avatar(self):
        print("Father avattar")


class Son(Mother, Father):
    sing = input("Enter your sing\t")

    def ingeener(self):
        print("Son is ingeener")


    def poet(self):
        print("Son is poet")


    def gartenmen(self):
        print("Son is gartmen")


class Dauther(Mother, Father):
    def teacher(self):
        print("Dauter is a teacher")


    def beutifull(self):
        obj = Son()
        # obj.love() #  Виведе на екран те що є лише в методі
        print(obj.love())  #  Виведе на екран те що є в методі і те що є в return

        print("Dauter is beutifull")

    def help(self):
        print("Dauter can help")


# fam_obj = Family()

duter_obj = Dauther()
duter_obj.eat()
# duter_obj.drive()
# duter_obj.beutifull()
# if duter_obj.drive() is True:
#     duter_obj.eat()
# s_obj = Son()

