""""
Вводиться три числа. Перевірити чи сума двох перших чисел більша, ніж третє.
Результат винести як значення bool
"""
try:
    a = float(input("\nВведіть Перше будь-яке число:  "))
    b = float(input("Введіть Друге будь-яке число:  "))
    c = float(input("Введіть Третє будь-яке число:  "))
except ValueError:
    print ("Ви ввели одне з чисел буквами. Повторіть дію ще раз")
    exit ()

print(" Сума a + b > c ---{}---".format((a + b) > c))
