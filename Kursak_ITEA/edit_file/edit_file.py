

from Kursak_ITEA.edit_file.edit_func_file import start_edit
from Kursak_ITEA.help_func import create_list
from Kursak_ITEA.edit_file.edit_clasification_wine import edit_clasif_wine


def edit_file():
    while True:
        print("\nМЕНЮ --- РЕДАГУВАННЯ ФАЙЛІВ --- ")
        edit_menu = {'1': 'КЛАСИФІКАЦІЯ ВИН',
                     '2': 'ДОДАВАННЯ/ ВИДАЛЕННЯ ФРУКТІВ ТА ХАРАКТРИСТИК ЇХ СОКІВ',
                     '3': 'ВИХІД В ПОПЕРЕДНЄ МЕНЮ',
                     '0': 'ВИХІД З ПРОГРАМИ'}
        create_list(edit_menu)
        a = input("\t\t\t\t\t\tВАШ ВИБІР----- ")
        if a == '1':
            edit_clasif_wine()
        elif a == '2':
            print("ДОДАВАННЯ/ ВИДАЛЕННЯ ФРУКТІВ ТА ХАРАКТРИСТИК ЇХ СОКІВ")
            start_edit()
        elif a == '3':
            print("ВИХІД В ПОПЕРЕДНЄ МЕНЮ")
            return
        elif a == '0':
            print("ВИХІД З ПРОГРАМИ ")
            exit()
        else:
            print("ЗРОБІТЬ СВІЙ ВИБІР ")
