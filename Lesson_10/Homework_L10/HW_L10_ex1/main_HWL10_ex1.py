# потрібно імпортувати фпйл з словником паролей та ролей
from Lesson_10.Homework_L10.packeg_for_HWL10.parol_rol import parol_rol, new_parol_rol_
from Lesson_10.Homework_L10.packeg_for_HWL10.admin.add_del_file import add_del_file_json_list
from Lesson_10.Homework_L10.packeg_for_HWL10.admin.edit_parol_rol import ed_parol_rol
import random
import json
import re
import string


def dostup():
    print("\n\t\t\t\t\t Перевірка чи ВИ вмієте рахувати")
    digit_kapcha()
    print("\n\t\t\t\t\t Перевірка чи ВИ вмієте писати")
    while True:
        for i in range(3):
            choice_word = word_capcha()
            check_word = input(f"НАПИШІТЬ ВКАЗАНЕ СЛОВО --- {choice_word.lower()} --- = \t")
            if check_word == choice_word.lower():
                print("\n ПЕРЕВІРКА ПРОЙДЕНА. ДОСТУП ДОЗВОЛЕНО")
                break
            if check_word != choice_word.lower():
                print(
                        "\nСЛОВА НЕ СПІВПАДАЮТЬ. ВІДПОВІДЬ ХИБНА.\nВИ НЕ ВМІЄТЕ ПИСАТИ. ВИ НЕДОСТОЙНІ ЧИТАТИ ВМІСТ СТАТЕЙ")
                print(f"У ВАС ЗАЛИШИЛОСЬ {2 - i} СПРОБИ")
        break


#  функція для створенян числової капчі
def digit_kapcha():
    while True:
        for i in range(3):
            a = random.randrange(100)
            y = 10*a
            c = int(input(f"СКІЛЬКИ БУДЕ {a} *10 = "))
            if c == y:
                print("ВІДПОВІДЬ ПРАВИЛЬНА")
                break
            elif c != y:
                print(f"ВІДПОВІДЬ ХИБНА. ВИ МАЄТЕ ЩЕ {2-i} СПРОБИ ДЛЯ ПРАВИЛЬНОЇ ВІДПОВІДІ")
                if i == 2:
                    print("ВИ НЕ ВМІЄТЕ РАХУВАТИ. ВИ НЕДОСТОЙНІ ЧИТАТИ ВМІСТ СТАТЕЙ")
                    exit()

        return c

def word_capcha():
    with open(r'd:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\text_capcha.json','r') as f:
        word = json.loads(f.read())
        filt_word = re.findall(r'\w\w\w\w\w', word)
        choice_word = random.choice(filt_word)
    return choice_word
word_capcha()


def check_parol(parol_login):
    if parol in parol_login:
        if parol_login.get(parol) == "ADMIN":  # value повератає list усіх значень до наявних ключів
                                                #  get перевірка значення по ключу
            dostup()
            dict_check_out = {'1': 'ЧИТАТИ', '2': 'РЕДАГУВАТИ ФАЙЛИ', '3': 'РЕДАГУВАННЯ СПИСКА З ФАЙЛАМИ',
                              '4': 'РЕДАГУВАННЯ ПАРОЛІВ ТА РОЛЕЙ','5': 'ВИХІД'}

            for i in dict_check_out:
                print(f"{i} - {dict_check_out.get(i)}")

        # тут прописати функціонал для адміністрарора читати, редагувати, зінювати та добавляти паролі
            check = input("ВИБЕРІТЬ ПОДАЛЬШІ ДІЇ\t")
            if dict_check_out[check] == "ЧИТАТИ":
                from Lesson_10.Homework_L10.packeg_for_HWL10.user.only_read import decor_only_read
            if dict_check_out[check] == "РЕДАГУВАТИ ФАЙЛИ":
                from Lesson_10.Homework_L10.packeg_for_HWL10.admin.write_admin import decor_only_write
            if dict_check_out[check] == "РЕДАГУВАННЯ СПИСКА З ФАЙЛАМИ":
                add_del_file_json_list()
            if dict_check_out[check] == "РЕДАГУВАННЯ ПАРОЛІВ ТА РОЛЕЙ":
                ed_parol_rol()
            if dict_check_out[check] == "ВИХІД":
                print("\nВИ ВИЙШЛИ ЗІ СВОГО  КОРИСТУВАЧА")

        elif parol_login.get(parol) == "EDITOR":
            dostup()
            dict_check_out = {'1':'ЧИТАТИ','2':'РЕДАГУВАТИ ФАЙЛИ','3':'ВИХІД'}
            print(dict_check_out)
            check = input ("ВИБЕРІТЬ ПОДАЛЬШІ ДІЇ\t")
            if dict_check_out[check] == "ЧИТАТИ":
                from Lesson_10.Homework_L10.packeg_for_HWL10.user.only_read import decor_only_read
            elif dict_check_out[check] == "РЕДАГУВАТИ ФАЙЛИ":
                # вставити функцію про дозапис
                from Lesson_10.Homework_L10.packeg_for_HWL10.editor.only_write import decor_only_write
            else:
                print("\nВИ ВИЙШЛИ ЗІ СВОГО  КОРИСТУВАЧА")
        else: #  це для звичайного користувача
            print("\n\t\t\t\t\t Перевірка чи ВИ вмієте рахувати")
            digit_kapcha()
            print("\n\t\t\t\t\t Перевірка чи ВИ вмієте писати")
            while True:
                for i in range(3):
                    choice_word = word_capcha()
                    check_word = input(f"НАПИШІТЬ ВКАЗАНЕ СЛОВО --- {choice_word.lower()} --- = \t")
                    if check_word == choice_word.lower():
                        print("\n ПЕРЕВІРКА ПРОЙДЕНА. ДОСТУП ДОЗВОЛЕНО")
                        # викликається функція замикання декоратор , щодо можливості читати статі
                        from Lesson_10.Homework_L10.packeg_for_HWL10.user.only_read import decor_only_read
                    else:
                        print("\nСЛОВА НЕ СПІВПАДАЮТЬ. ВІДПОВІДЬ ХИБНА.\nВИ НЕ ВМІЄТЕ ПИСАТИ. ВИ НЕДОСТОЙНІ ЧИТАТИ ВМІСТ СТАТЕЙ")
                        print(f"У ВАС ЗАЛИШИЛОСЬ {2-i} СПРОБИ")
                exit()
    else:
        print("ЗВЕРНІТЬСЯ ДО АДМІНІСТРАТОРА ДЛЯ НАДАННЯ ВАМ ДОСТУПУ")
        exit()

parol = input("ВВЕДІТЬ СВІЙ ПАРОЛЬ\t\t\t\t")
parol_login = parol_rol()
check_parol(parol_login)
