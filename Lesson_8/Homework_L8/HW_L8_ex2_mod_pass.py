""""
Password storage. Модифікувати програму генерування паролів, яку ви робили на 6 уроці.
Після запуску програми, запистати корисувача, що він хоче зробити: створити новий чи отримати пароль,
 який він вводив раніше. Всі паролі зберігати в якомусь файлі. Отримати пароль можна за допомогою ключвого слова,
 яке вказує користувач при  створенні нового пароля.

Наприклад: Користувач запускає програму і хоче отримати пароль, який вводив раніше.
Для цьго він водить ключове слово за яким введеться пошщук у файлі і отримується пароль.
Коли корисувач хоче створити новий пароль, то використати код програми з 6 уроку, після генерувавння пароля попровисти
корисувача ввести ключове слово, і дану пару ключ-значення записати у файл.
"""

from Lesson_8.Homework_L8.to_password_packedg.passw import shufr


path_to_file_with_parol = "D:\\Python_ITed\\Lesson_8\\Homework_L8\\packeg_for_working with file\\passw_key.txt"
e_ = input(" \nДля отримання доступу в систему оберіть:\n\t 1 - створити НОВИЙ пароль \n"
           "\t2 - використати ЗБЕРЕЖЕНИЙ   \n")

if e_ != "1":
    key = input("ВВЕДДІТЬ СВІЙ КЛЮЧ доступу до паролю   ")
    l_key = len(key)
    with open(path_to_file_with_parol, 'r') as f:
        text = f.readlines()  # Створює масив елементом якого є рядок
        passw = 0
        for i in range(len(text)):
            if key in text[i]:
                g = text[i]
                l_g = len(g)
                passw = g[(l_key+3):]  # зріз рядка
                if key not in text[i]:
                    print("\nКлюч не знайдено. Cтворіть свій пароль та ключ")
                    exit()
        print("\nВаш пароль = %s" % passw)

elif e_ == "1":
    n_key, n_parol = shufr()
    print("ВАШ ПАРОЛЬ ---  %s --- ТА КЛЮЧ  --- %s --- " %(n_parol, n_key))
    with open(path_to_file_with_parol, 'a+') as f:
        text = f.readlines()  # Створює масив елементом якого є рядок
        f.write("\n"+n_key + " - " + n_parol)


# для L8_ex_3
def find_key():
    key = input("ВВЕДДІТЬ СВІЙ КЛЮЧ доступу до паролю   ")
    l_key = len(key)
    with open(r'Homework_L8\\to_password_packedg\\hw_L8_ex_3\\password_to_file.txt', 'r') as f:
        text = f.readlines()  # створює масив елементом якого є рядок
    passw = 0
    for i in range(len(text)):
        if key in text[i]:
            g = text[i]
            l_g = len(g)
            passw = g[(l_key + 3):]  # зріз рядка вказано початкові координати
            print("\nВаш пароль = %s" % passw)
        elif key not in text[i]:
            print("\nКлюч не знайдено. Cтворіть свій пароль та ключ")
            exit()
    return key
