from Kursak_ITEA._0_enter_in_prog.enter_password import enter
from Kursak_ITEA._1_klasificacia_wine.clasification import main_wine_f
from Kursak_ITEA._2_calculation.calc import all_func_calc_wine
from Kursak_ITEA._3_corr_wine.repear_wine import repear_wine
from Kursak_ITEA._4_edit_file.edit_file import edit_file
from Kursak_ITEA.help_func import create_list


def main_pro():
    while True:
        print("\nПРОГРАМА РОЗРАХУНКУ БУДЕ КОРИСНА ТИМ У КОГО Є БАЖАННЯ ТА СИРОВИНА ДЛЯ ВИГОТОВЛЕННЯ ДОМАШНЬОГО ВИНА\n"
              "ВОНА Є КОРИСНУЮ ДЛЯ РОЗРАХУНКІВ ЙОГО ОСНОВНИХ СКЛАДОВИХ")
        while True:
            print("\nГОЛОВНЕ МЕНЮ\n")
            zmist = {'1': 'ЗАГАЛЬНЕ',
                     '2': 'РОЗРАХУНКИ ДЛЯ ВИНА',
                     '3': 'ВИПРАВЛЕННЯ ВИНА(КУПАЖ, ЗМІЦНЕННЯ)',
                     '4': 'РЕДАГУВАННЯ ІНФОРМАЦІЙНИХ ФАЙЛІВ (ЛИШЕ АДМІНІСТРАТОР)',
                     '0': 'ВИХІД З ПРОГРАМИ'
            }
            create_list(zmist)
            a = input("\t\t\t\t\t\tВАШ ВИБІР----- ")
            if a == '1':
                print("ЗАГАЛЬНЕ")
                main_wine_f()
            elif a == '2':
                print("РОЗРАХУНКИ ДЛЯ ВИНА")
                all_func_calc_wine()
            elif a == '3':
                print("ВИПРАВЛЕННЯ ВИНА(КУПАЖ, ЗМІЦНЕННЯ)")
                repear_wine()
            elif a == '4':
                print("РЕДАГУВАННЯ ІНФОРМАЦІЙНИХ ФАЙЛІВ (ЛИШЕ АДМІНІСТРАТОР)")
                if password == "admin":
                    print("ВАШ СТАТУС ---ADMIN---. ВИ МОЖЕТЕ РЕДАГУВАТИ ФАЙЛИ")
                    edit_file()
                else:
                    print("ВАШ СТАТУС ---USER---. ВИ МОЖЕТЕ ЛИШЕ ЧИТАТИ ФАЙЛИ")
            else:
                print("ВИХІД З ПРОГРАМИ ")
                exit()


password = enter()
main_pro()

