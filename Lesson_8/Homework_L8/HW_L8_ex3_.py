""""
Після того як користувач завершив роботу з програмою, попросити в нього ввести цифру або слово.
 Перед закриттям зашиффрувати увесь текст за шифром Віженера, де ключом виступає введене значення.
 Перед зчитуванянм інформації у файлі попросити користувача ввести ключове слово або цифру
 і розшифорувати інформацію у файлі за введеним ключем.
 Після цього пропонувати створити новий пароль або отримати існуючий.
"""
import re

#  початок роботи- відкрити файл
name_file = input("Вкажіть назву файлу, що знаходиться в \n"
                  "Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3   без розширення  .txt ")
f = open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3\\' + name_file + '.txt', 'r+')
text = f.read()
f.close()
i = 0
while i < 1:
    print("\nЩо зробити з файлом ?")
    answ = input("ПОКАЗАТИ --- 1---, ЗАШИФРУВАТИ --- 2---, РОЗШИФРУВАТИ --- 3---,ІНШЕ - ВИХІД З ПРОГРАМИ    \n")
    if answ == "1":
        print(text)

    elif answ == "2":
            #  запуск функції шифрування
        from Lesson_8.Homework_L8.to_password_packedg.hw_L8_ex_3.passw_L8_ex3 import shufr
        key, shufr_text = shufr(text)

            #  збереження зашифрованої інформації у новий файл
        name_sekr_file = input("Вкажіть назву файлу для зберігання зашифров. інформації   ")
        new_w_f = open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3\\'
                       + name_sekr_file + '.txt','a+')
        new_w_f.write(shufr_text)
        new_w_f.close()

        # збереження ключа у файл
        key_file = open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3\\'
                             r'password_to_file.txt','a+')
        dostup = key + " - " + name_sekr_file  #  input("Введіть ")
        key_file.write("\n"+ dostup)  # перенесе запис на іншу стрічку
        key_file.close()

    elif answ == "3":
        #  відкриття файлу для читання та перевірки чи є КЛЮЧ в файлі збереженими ключами
        key_f = open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3\\'
                          r'password_to_file.txt', 'r')
        find_key_to_file = key_f.read()

        key = input("Вкажіть КЛЮЧ   ")
        #  визначення наявності пари КЛЮЧ-НАЗВА ФАЙЛУ
        find_key_name_file = bool(''.join(re.findall(key + " - " + name_file, find_key_to_file)))

        if find_key_name_file:
            #  викликається функція з модуля по розшифруванню
            from Lesson_8.Homework_L8.to_password_packedg.hw_L8_ex_3.unpassw_L8_ex3 import unshufr
            unshufr_text, key = unshufr(text, key)

            #  збереження зашифрованої інформації у файл
            name_unsekr_file = input("Вкажіть назву файлу для зберігання зашифров. інформації   ")
            new_w_f = open(r'd:\\Python_ITed\\Lesson_8\\Homework_L8\\to_password_packedg\\hw_L8_ex_3\\'
                           + name_unsekr_file + '.txt', 'a+')
            new_text = new_w_f.write(unshufr_text)
            new_w_f.close()
        else:
            print("Вказаний вами КЛЮЧ до цього файлу відсутній у базі даних.\n Файл розшифрувати НЕМОЖЛИВО")
    else:
        exit()
    i += 1
f.close()
