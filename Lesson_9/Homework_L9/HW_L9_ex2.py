""""
Змінити логіку зберігання паролів у файлі у завданні з попереднього домашнього завдання.
Зберігати дані у форматі json.

"""
import json


key = input("Для доступу до програми ВВЕДІТЬ КОРИСТУВАЧА, щоб отриамти пароль ")
    # функція виводить в основну програму вміст прочитаного файлу як словник
def inner_json_file():
    #  щоб програма працювала потрібно аби у файлі на самому початку був порожній словник
    with open('d:\\Python_ITed\\Lesson_9\\Homework_L9\\key_pasw_L9ex2_.json', 'r') as f:
        result_open = json.loads(f.read())  # прочитаний вміст файлу (обєкту) розкодовується як словник
    return result_open

dict_key_pas = inner_json_file()  # пайтон бачить  як словник


def _n_key():
    new_key = input(" НОВИЙ КЛЮЧ\t\t\t")
    pasword = input(" НОВИЙ ПАРОЛЬ\t\t")
    dict_key_pas.update({new_key: pasword})
    with open('d:\\Python_ITed\\Lesson_9\\Homework_L9\\key_pasw_L9ex2_.json', 'w') as f:
        json.dump(dict_key_pas, f)  # словник записуєтсья як обєкт у файл
        print("ПЕРЕЗАПУСТІТЬ ПРОГРАМУ ТА ОТРИМАЙТЕ ДО НЕЇ ДОСТУП")
        exit()
try:
    key in dict_key_pas
    print(f"OK. WELCOME. Your pasword {dict_key_pas[key]}")
# pas = input("new enter pas   ")
except KeyError as e:
    print(" Введений користувач відсутній у базі даних. Створіть свого користувача та пароль")
    answer = input(" ВВЕСТИ ІНШОГО КОРИСТУВАЧА ---1, СТВОРИТИ НОВОГО КОРИСТВУВАЧА --- 2 \t\t\t")
    if answer == "1":
        print("ПЕРЕЗАПУСТІТЬ ПРОГРАМУ ТА ВВЕДІТЬ ІНШОГО КОРИСТУВАЧА")
        exit()
    elif answer == "2":
        _n_key()












#
#
# e_ = input(" \nДля отримання доступу в систему створити НОВИЙ пароль НАТИСНИ---1--- чи "
#            "використати ЗБЕРЕЖЕНИЙ --- будь-який інший символ?    ")
#
# if e_ != "1":
#     key = input("ВВЕДДІТЬ СВІЙ КЛЮЧ доступу до паролю   ")
#     l_key = len(key)
#     with open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\packeg_for_working with file\\passw_key.txt','r') as f:
#         text = f.readlines()  #  створює масив елементом якого є рядок
#         passw = 0
#         for i in range(len(text)):
#             if key in text[i]:
#                 g = text[i]
#                 l_g = len(g)
#                 passw = g[(l_key+3):]  # зріз рядка
#                 if key not in text[i]:
#                     print("\nКлюч не знайдено. Cтворіть свій пароль та ключ")
#                     exit()
#         print("\nВаш пароль = %s" % passw)
#
# elif e_ == "1":
#     from Lesson_8.Homework_L8.to_password_packedg.passw import shufr  #  сама запускається !???
#     # shufr(key)
#     n_key, n_parol = shufr()
#     print("ВАШ ПАРОЛЬ ---  %s --- ТА КЛЮЧ  --- %s --- " %(n_parol, n_key))
#     with open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\packeg_for_working with file\\passw_key.txt','a+') as f:
#         text = f.readlines()  #  створює масив елементом якого є рядок
#         f.write("\n"+n_key + " - " + n_parol)
#
