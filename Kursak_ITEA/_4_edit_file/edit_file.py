import json
from Kursak_ITEA._4_edit_file.edit_func_file import create_list


def edit_file():
    while True:
        print("МЕНЮ --- РЕДАГУВАННЯ ФАЙЛІВ --- ")
        edit_menu = {'1': 'КЛАСИФІКАЦІЯ ВИН',
                     '2': 'ХАРАКТРИСТИКИ СОКІВ ФРУКТІВ',
                     '0': 'ВИХІД З ПРОГРАМИ'
}
        create_list(edit_menu)
        a = input("\t\t\t\t\t\tВАШ ВИБІР----- ")
        if a == '1':
            print(" РОЗДІЛ В РОЗРОБЦІ")
        elif a == '2':
            pass
        elif a == '0':
            print("ВИХІД З ПРОГРАМИ ")
            exit()
        else:
            print("ЗРОБІТЬ СВІЙ ВИБІР ")
