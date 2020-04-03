from Kursak_ITEA._1_klasificacia_wine.clasification import main_wine_f
from Kursak_ITEA.help_func import create_list
from Kursak_ITEA._2_calculation.calc import all_func_calc_wine
from Kursak_ITEA._3_corr_wine.repear_wine import repear_wine


def main_pro():
    while True:
        print("\nПРОГРАМА РОЗРАХУНКУ БУДЕ КОРИСНА ТИМ У КОГО Є БАЖАННЯ ТА СИРОВИНА ДЛЯ ВИГОТОВЛЕННЯ ДОМАШНЬОГО ВИНА\n")
        print("ПРОГРАМА РОЗРАХУНКУ ОСНОВНИХ СКЛАДОВИХ ДЛЯ ПРИГОТУВАННЯ ДОМАШНЬОГО ВИНА\n")
        while True:
            print("ГОЛОВНЕ МЕНЮ\n")
            zmist = {'1':'ЗАГАЛЬНЕ',
                     '2':'РОЗРАХУНКИ ДЛЯ ВИНА',
                     '3':'ВИПРАВЛЕННЯ ВИНА(КУПАЖ, ЗМІЦНЕННЯ)',
                     '0':'ВИХІД З ПРОГРАМИ'
            }
            create_list(zmist)
            a = input("\t\t\t\t\t\tВАШ ВИБІР----- ")
            if a == '1':
                main_wine_f()
            elif a == '2':
                all_func_calc_wine()
            elif a == '3':
                repear_wine()
            else:
                print("ВИХІД З ПРОГРАМИ ")
                exit()

main_pro()

