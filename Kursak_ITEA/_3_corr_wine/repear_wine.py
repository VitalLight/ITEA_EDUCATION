from Kursak_ITEA.help_func import create_list
from Kursak_ITEA._3_corr_wine.kypag import main_kypag
from Kursak_ITEA._3_corr_wine.kripl_wine import main_kripl


def repear_wine():
    print("\nОБЕРІТЬ ТЕ ЩО ВАМ ПОТРІБНО:")
    menu = {'\t\t\t1':'КУПАЖ ВИН АБО СОКІВ',
            '\t\t\t2':'КУПАЖ ВИНА ДО ЗАДАНИХ УМОВ',
            '\t\t\t3':'КРІПЛЕННЯ ВИНА СПИРТОВИМ РОЗЧИНОМ',
            '\t\t\t4':'ЗМЕНШЕННЯ КИСЛОТНОСТІ СОКУ ІНШИМ СОКОМ',
            '\t\t\t5':'ВИХІД В ПОПЕРЕДНЄ МЕНЮ',
            '\t\t\t0':'ВИХІД З ПРОГРАМИ'
            }
    create_list(menu)
    answer = input("\nЗРОБІТЬ СВІЙ ВИБІР\t\t\t")
    while True:
        if answer == '1':
            main_kypag()
            break
        elif answer == '2':
            pass
            break
        elif answer == '3':
            main_kripl()
            break
        elif answer == '4':
            pass
            break
        elif answer == '5':
            pass
            break
        elif answer == '0':
            print("ВИХІД З ПРОГРАМИ")
            exit()
# main_corr()