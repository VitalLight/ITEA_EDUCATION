from Kursak_ITEA.help_func import create_list


path_to_file_kind_wine = 'klasificacia_wine\\kind_wine.txt'

def edit_clasif_wine():
    while True:
        print("\n\tМЕНЮ --- КЛАСИФІКАЦІЯ ВИН")
        menu = {"1": "ПРОЧИТАТИ",
                "2": "ДОБАВИТИ ІНФОРМАЦІЮ",
                "3": "ВИДАЛИТИ ІНФОРМАЦІЮ",
                "4": "ВИХІД В ПОПЕРЕДНЄ МЕНЮ",
                "0": "ВИХІД З ПРОГРАМИ"}
        create_list(menu)
        choice = input("\t\t\tЗРОБІТЬ СВІЙ ВИБІР\t\t\t")
        if choice == "1":
            with open(path_to_file_kind_wine, 'r') as f:
                print(f.read())
        elif choice == "2":
            add_info()
        elif choice == "3":
            del_info()
        elif choice == "4":
            return
        elif choice == "0":
            print("\t\t\t\t\tВИХІД З ПРОГРАМИ ")
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
    with open(path_to_file_kind_wine, 'w') as f:
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
    with open(path_to_file_kind_wine, 'w') as f:
        f.writelines(txt_text)


def apendix():
    with open(path_to_file_kind_wine, 'r') as f:
        txt_text = f.readlines()
        elem = []
        for i in range(len(txt_text)):
            print(f"{i} - {txt_text[i]}")
            elem.append(str(i))
    return txt_text, elem
