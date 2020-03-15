""""
Написати програму, що буде генеруватиме пароль. Пароль генеруєтсья рандомно та може включати букви нижнього та
верхнього регістру. Користувач може вказати довжину пароля. Якщо пароль не сподобався, то перегенерувати його.
Програму розбити на функції.
"""
import random
import string  # модуль містить алфавіт

#  функція визначення довжини паролю

def len_par ():
    while True:
        try:
            len_parol = int(input("Введіть дожину паролю числом "))
            return len_parol
            break
        except ValueError:
            print("Потрібно ввести числом. Повторіть спробу ще раз  ")
            continue
a = len_par()

#  функція для генерації паролю
def parol(len_par):

    passw = []
    for i in range(a):
        passw.append(random.choice(list(string.ascii_letters)))
        password = ''.join(passw)
    return password


#  функція по генерації паролю
e = parol(len_par)
print("\n Ваш пароль ---%s---. Він влаштовує Вас?" % e)

ans = input(" Якщо так, то натисність +, якщо ні, будь який інший символ   ")
if ans == "+":
    print("\n Ваш пароль --- %s---" % e)
# Якщо пароль не влаштовує
while ans != "+":
    w = parol(len_par)
    print("Ваш пароль ---%s---. Він влаштовує Вас?" %w)
    ans = input(" Якщо так, то натисність +, якщо ні, будь який інший символ   ")
    if ans == "+":
        print("\n Ваш пароль --- %s --- " %w)