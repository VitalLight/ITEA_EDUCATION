#  write dictinary with parol and role in file json
import json

def parol_rol():
    with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\parol_rol.json', 'r') as f:
        result_open = json.loads(f.read())  # прочитаний вміст файлу (обєкту) розкодовується як словник
    return result_open
# parol_rol()


# parol_login = {}

def new_parol_rol_():
    parol = input(" НОВИЙ ПАРОЛЬ\t\t\t")
    rol = input(" ВВЕСТИ КОРИСТУВАЧА ADMIN, USER, EDITOR \t\t")
    parol_login.update({parol: rol})


# new_parol_rol_()