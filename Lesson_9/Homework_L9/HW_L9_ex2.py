""""
Змінити логіку зберігання паролів у файлі у завданні з попереднього домашнього завдання.
Зберігати дані у форматі json.

"""
import json
#  функція по створеню новго ключа та паролю
def _n_key():
    while True:
        new_key = input(" НОВИЙ КЛЮЧ\t\t\t")
        if new_key not in dict_key_pas:
            pasword = input(" НОВИЙ ПАРОЛЬ\t\t")
            break
        else:
            print("ВВЕДЕНИЙ КЛЮЧ ВЖЕ Є У БАЗІ. ЗМІНІТЬ КЛЮЧА")
            continue
    dict_key_pas.update({new_key: pasword})
    with open('d:\\Python_ITed\\Lesson_9\\Homework_L9\\key_pasw_L9ex2_.json', 'w') as f:
        json.dump(dict_key_pas, f)  # словник записуєтсья як обєкт у файл
        print("ПЕРЕЗАПУСТІТЬ ПРОГРАМУ ТА ОТРИМАЙТЕ ДО НЕЇ ДОСТУП")
        exit()

key = input("Для доступу до програми ВВЕДІТЬ КОРИСТУВАЧА, щоб отриамти пароль ")
    # функція виводить в основну програму вміст прочитаного файлу як словник


def inner_json_file():
    #  щоб програма працювала потрібно аби у файлі на самому початку був порожній словник
    with open('d:\\Python_ITed\\Lesson_9\\Homework_L9\\key_pasw_L9ex2_.json', 'r') as f:
        result_open = json.loads(f.read())  # прочитаний вміст файлу (обєкту) розкодовується як словник
    return result_open

dict_key_pas = inner_json_file()  # пайтон бачить  як словник

try:
    if key in dict_key_pas:
        print(f"OK. WELCOME. Your pasword {dict_key_pas[key]}")
except KeyError as e:
    print(" Введений користувач відсутній у базі даних. Створіть свого користувача та пароль")
    answer = input(" ВВЕСТИ ІНШОГО КОРИСТУВАЧА ---1, СТВОРИТИ НОВОГО КОРИСТВУВАЧА --- 2 \t\t\t")
    if answer == "1":
        print("ПЕРЕЗАПУСТІТЬ ПРОГРАМУ ТА ВВЕДІТЬ ІНШОГО КОРИСТУВАЧА")
        exit()
    elif answer == "2":
        _n_key()
    else:
        print("ВВЕДІТЬ ЧИСЛА, ЩО ПРОПОНУЮТЬСЯ")
