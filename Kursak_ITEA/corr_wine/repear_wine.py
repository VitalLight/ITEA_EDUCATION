from Kursak_ITEA.help_func import create_list
from Kursak_ITEA.corr_wine.kypag import main_kypag
from Kursak_ITEA.corr_wine.kripl_wine import main_kripl
from Kursak_ITEA.corr_wine.acid_less_juice import main_less_acid_juice
from Kursak_ITEA.corr_wine.kypag_condition import condition_kupag


def repear_wine():
    while True:
        print("\nМЕНЮ ВИПРАВЛЕННЯ ВИНА(КУПАЖ, ЗМІЦНЕННЯ)")
        menu = {'\t\t\t1': 'КУПАЖ ВИН АБО СОКІВ',
                '\t\t\t2': 'КУПАЖ ЗБРОЖЕНО-СПИРТОВОГО СОКУ/ВИНА ДО ЗАДАНИХ УМОВ СПИРТОВИМ РОЗЧИНОМ',
                '\t\t\t3': 'КРІПЛЕННЯ ВИНА СПИРТОВИМ РОЗЧИНОМ',
                '\t\t\t4': 'ЗМЕНШЕННЯ КИСЛОТНОСТІ ОСНОВНОГО СОКУ, СОКОМ З МЕНШОЮ КИСЛОТНІСТЮ АБО ВОДОЮ',
                '\t\t\t5': 'ВИХІД В ПОПЕРЕДНЄ МЕНЮ',
                '\t\t\t0': 'ВИХІД З ПРОГРАМИ'}
        create_list(menu)
        answer = input("\t\t\t\t\t\tВАШ ВИБІР ------- ")
        if answer == '1':
            print("\nКУПАЖ ВИН АБО СОКІВ")
            main_kypag()
        elif answer == '2':
            print("\nКУПАЖ ЗБРОЖЕНО-СПИРТОВОГО СОКУ/ВИНА ДО ЗАДАНИХ УМОВ СПИРТОВИМ РОЗЧИНОМ")
            condition_kupag()
        elif answer == '3':
            print("\nКРІПЛЕННЯ ВИНА СПИРТОВИМ РОЗЧИНОМ")
            main_kripl()
        elif answer == '4':
            print("\nЗМЕНШЕННЯ КИСЛОТНОСТІ ОСНОВНОГО СОКУ, СОКОМ З МЕНШОЮ КИСЛОТНІСТЮ АБО ВОДОЮ")
            main_less_acid_juice()
        if answer == '5':
            print("\nВИХІД В ПОПЕРЕДНЄ МЕНЮ")
            return
        elif answer == '0':
            print("\nВИХІД З ПРОГРАМИ")
            exit()
