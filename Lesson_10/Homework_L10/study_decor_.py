import random

def firs_decor(my_func):
    print("Hello I am your decor function")
    def wrapper():
        print("It is wrapper")
        b, d = my_func()  #  при такому записі змінні виведуться в основну програму після декоратора
        print("end wrapper")
        return b, d  #  при такому записі змінні виведуться в основну програму після декоратора
    return wrapper


@firs_decor
def my_func():
    a = int(input("Enter a number   "))
    d = pow(a,3)
    b = random.randrange(54)/d
    print(f" d = {d} and b= {b}")
    return b, d
b, d = my_func()  #  при такому записі змінні виведуться в основну програму після декоратора
print(f"b= main program = {b} and d = {d}")

""""
дві функції в декоратор вкласти не можна, бо це викликає помилку
"""