from Kursak_ITEA.help_func import create_list
from Kursak_ITEA._3_corr_wine.kypag import main_kypag
from Kursak_ITEA._3_corr_wine.kripl_wine import main_kripl
from Kursak_ITEA._3_corr_wine.acid_less_juice import main_less_acid_juice


def repear_wine():
    print("\nОБЕРІТЬ ТЕ ЩО ВАМ ПОТРІБНО:")
    menu = {'\t\t\t1':'КУПАЖ ВИН АБО СОКІВ',
            '\t\t\t2':'КУПАЖ ЗБРОЖЕНО-СПИРТОВОГО СОКУ/ВИНА ДО ЗАДАНИХ УМОВ СПИРТОВИМ РОЗЧИНОМ',
            '\t\t\t3':'КРІПЛЕННЯ ВИНА СПИРТОВИМ РОЗЧИНОМ',
            '\t\t\t4':'ЗМЕНШЕННЯ КИСЛОТНОСТІ ОСНОВНОГО СОКУ СОКОМ З МЕНШОЮ КИСЛОТНІСТЮ/ВОДОЮ',
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
            main_less_acid_juice()
            break
        elif answer == '5':
            return
        elif answer == '0':
            print("ВИХІД З ПРОГРАМИ")
            exit()
# main_corr()