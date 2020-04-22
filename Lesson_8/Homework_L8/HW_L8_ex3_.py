""""
Після того як користувач завершив роботу з програмою, попросити в нього ввести цифру або слово.
 Перед закриттям зашиффрувати увесь текст за шифром Віженера, де ключом виступає введене значення.
 Перед зчитуванянм інформації у файлі попросити користувача ввести ключове слово або цифру
 і розшифорувати інформацію у файлі за введеним ключем.
 Після цього пропонувати створити новий пароль або отримати існуючий.
"""
import re

from Lesson_8.Homework_L8.to_password_packedg.hw_L8_ex_3.passw_L8_ex3 import shufr
from Lesson_8.Homework_L8.to_password_packedg.hw_L8_ex_3.unpassw_L8_ex3 import unshufr


path_to_f = "d:\\Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3\\password_to_file.txt"
#  початок роботи- відкрити файл
name_file = input("Вкажіть назву файлу, що знаходиться в \n"
                  "Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3   без розширення  .txt ")
f = open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3\\' + name_file + '.txt', 'r+')
text = f.read()
f.close()

while True:
    print(f"\nЩО РОБИТИ З ФАЙЛОМ {name_file}?")
    answ = input("\nПОКАЗАТИ --- 1---, \nЗАШИФРУВАТИ --- 2---, \nРОЗШИФРУВАТИ --- 3---,\nВИХІД З ПРОГРАМИ "
                 "ЩОБ ОБРАТИ ІНШИЙ ФАЙЛ ДЛЯ РОБОТИ ---БУДЬ-ЯКИЙ ІНШИЙ СИМВОЛ   ")
    if answ == "1":
        print(text)

    elif answ == "2":
        #  запуск функції шифрування
        key, shufr_text = shufr(text)

        #  збереження зашифрованої інформації у новий файл
        name_sekr_file = input("Вкажіть назву файлу для зберігання зашифров. інформації   ")
        new_w_f = open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3\\'
                       + name_sekr_file + '.txt', 'a+')
        new_w_f.write(shufr_text)
        new_w_f.close()

        # збереження ключа у файл
        key_file = open(path_to_f, 'a+')
        dostup = key + " - " + name_sekr_file
        key_file.write("\n" + dostup)  # перенесе запис на іншу стрічку
        key_file.close()

    elif answ == "3":
        #  відкриття файлу для читання та перевірки чи є КЛЮЧ в файлі збереженими ключами
        key_f = open(path_to_f, 'r')
        find_key_to_file = key_f.read()

        key = input("Вкажіть КЛЮЧ   ")
        #  визначення наявності пари КЛЮЧ-НАЗВА ФАЙЛУ
        find_key_name_file = bool(''.join(re.findall(key + " - " + name_file, find_key_to_file)))

        if find_key_name_file:
            #  викликається функція з модуля по розшифруванню
            unshufr_text, key = unshufr(text, key)

            #  збереження розашифрованої інформації у файл
            name_unsekr_file = input("Вкажіть назву файлу для зберігання розашифров. інформації   ")
            new_w_f = open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3\\'
                           + name_unsekr_file + '.txt', 'a+')
            new_text = new_w_f.write(unshufr_text)

            #  ЗАПИТАТИ ЧИ ПОТРІБНО СТВОРИТИ НОВИЙ ПАРОЛЬ ДЛЯ ЦЬОГО ФАЙЛУ
            print("\n СТВОРИТИ НОВИЙ ПАРОЛЬ ДЛЯ ЦЬОГО ФАЙЛУ?")
            ans2 = input("\nТАК --- 1,\n НІ ---2     ")
            if ans2 == "1":
                print("\nПЕРЕЗАПУСТІТЬ ПРОГРАМУ ТА ВИБЕРІТЬ ПОЗИЦІЮ ---2---")
            elif ans2 == "2":
                pass
            new_w_f.close()
        else:
            print("Вказаний вами КЛЮЧ до цього файлу відсутній у базі даних.\n Файл розшифрувати НЕМОЖЛИВО")
    else:
        exit()
