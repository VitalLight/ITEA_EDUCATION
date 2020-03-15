""""
Написати програму, що буде генеруватиме пароль. Пароль генеруєтсья рандомно та може включати букви нижнього та
верхнього регістру. Користувач може вказати довжину пароля. Якщо пароль не сподобався, то перегенерувати його.
Програму розбити на функції.
"""
import random
import string  # модуль містить алфавіт

len_parol = int(input("Введіть дожину паролю числом "))
try:
    len_ = int(len_parol)
except ValueError:
    print("Потрібно ввести числом. Повторіть спробу ще раз  ")
    exit()


#  функція для генерації паролю
def parol(a):
    passw = []
    for i in range (a):
        passw.append(random.choice(list(string.ascii_letters)))
        password = ''.join(passw)
        return password


#  функція по генерації паролю
e = parol(len_parol)
print(e)

ans = input("Чи влаштовує пароль? Якщо так, то натисність 1, якщо ні, будь який інший символ   ")
if ans == "1":
    print("Ваш пароль %s" % e)

# Якщо пароль не влаштовує
while ans != "1":
    w = parol(len_parol)
    print(w)
    ans = input("Чи влаштовує пароль? Якщо так, то натисність 1, якщо ні, будь який інший символ   ")
    if ans == "1":
        print("Ваш пароль %s" % w)