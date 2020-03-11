""""
Написати функцію. Дана функція приймає один аргумент - число. Процес обробки як в презентації
"""
a = input(" Enter a number:   ")
try:
    k = int(a)
except ValueError:
    print("Введене не числове значення")
    exit()

def suma_masiva (y):
    b = list(a)
    c = len(b)
    s= 0
    for i in range(c):
        s = s + int(b[i])
    return s

print(suma_masiva (a))
