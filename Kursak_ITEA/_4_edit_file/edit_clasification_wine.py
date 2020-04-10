from Kursak_ITEA.help_func import create_list


def edit_clasif_wine():
    while True:
        print("\nКЛАСИФІКАЦІЯ ВИН")
        menu = {"1": "ДОБАВИТИ ІНФОРМАЦІЮ",
                "2": "ВИДАЛИТИ ІНФОРМАЦІЮ",
                "3": "ВИХІД В ПОПЕРЕДНЄ МЕНЮ",
                "0": "ВИХІД З ПРОГРАМИ"}
        print(create_list(menu))
        choice = input("ЗРОБІТЬ СВІЙ ВИБІР\t\t\t")
        if choice == "1":
            add_info()
        elif choice == "2":
            del_info()
        elif choice == "3":
            return
        elif choice == "0":
            print("ВИХІД З ПРОГРАМИ ")
            exit()
        else:
            print("ЗРОБІТЬ СВІЙ ВИБІР")


def add_info():
    txt_text, elem = apendix()
    num_row = input("ВКАІЖІТЬ НОМЕР РЯДКУ ЯКИЙ ПОТРІБНО ЗАМІНИТИ, ІНАКШЕ(ENTER) ТЕКСТ ЗАПИШИТЬСЯ В КІНЕЦЬ\t")
    change_text = input("ВВЕДІТЬ ЗМІНИ В ТЕКСТ\n")
    if num_row in elem:
        txt_text[int(num_row)] = f"{change_text}\n"
    else:
        txt_text.append(f"\n{change_text}\n")
    with open(r'D:\\Python_ITed\\Kursak_ITEA\\_1_klasificacia_wine\\kind_wine.txt', 'w') as f:
        f.writelines(txt_text)


def del_info():
    txt_text, elem = apendix()
    while True:
        num_row = input("ВКАІЖІТЬ НОМЕР РЯДКУ ЯКИЙ ПОТРІБНО ВИДАЛИТИ \t")
        if num_row in elem:
            del txt_text[int(num_row)]
            break
        else:
            print("НОМЕРА РЯДКА ВІДСУТНІЙ В СПИСКУ")
    with open(r'D:\\Python_ITed\\Kursak_ITEA\\_1_klasificacia_wine\\kind_wine.txt', 'w') as f:
        f.writelines(txt_text)


def apendix():
    with open(r'D:\\Python_ITed\\Kursak_ITEA\\_1_klasificacia_wine\\kind_wine.txt', 'r') as f:
        txt_text = f.readlines()
        elem = []
        for i in range(len(txt_text)):
            print(f"{i} - {txt_text[i]}")
            elem.append(str(i))
    return txt_text, elem
