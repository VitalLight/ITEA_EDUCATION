""""
Користувач вводить два числа. Додати ці числа як строки. Після цього перевести утворене число-строку в тип int.
Знайти корінь цього числа та результат вивести на екран.
"""
n1 = input("Введіть Перше число:   ")
n2 = input("Введіть Друге число:   ")

try:
    n1_ = float(n1)
    n2_ = float(n2)
    if n1_ <= 0 or n2_ <= 0:
        print ("\nВВедені числа мають бути більше нуля")
        exit()
except ValueError:
    print("\nВВеденно не числове значення. Повторіть спочатку ")
    exit()

c = int(n1 + n2)
print(" Квадрат  числа {} становить --- {} ---,"
      "\t а Квадратний корінь --- {}---".format (c, c**2, round(c**(1/2),5)))
