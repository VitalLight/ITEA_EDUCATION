""""
Написати програму для обчислення площі трикутника за трьома сторонами. Результати вивести на екран.
"""
try:
    a = float(input("Введіть довжину 1-ї сторони трикутника a:  "))
    b = float(input("Введіть довжину 2-ї сторони трикутника b:  "))
    c = float(input("Введіть довжину 3-ї сторони трикутника c:  "))
except ValueError:
    print("\n ВВедене значення котроїсь зі сторонін трикутника НЕ числове значення")
    exit()
# площа трикутника становить s = a * (h/2)
p = (a + b + c)/2
s = (p * (p - a) * (p - b) * (p - c))**(1/2)
print("\n Площа трикутника становить {}".task_2_ex_3.pyformat(s))