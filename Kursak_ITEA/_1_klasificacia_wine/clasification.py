from Kursak_ITEA.help_func import create_list, choice_for_reed



def main_wine_f():
    print("\nОБЕРІТЬ ЩО ВАС ЦІКАВИТЬ:")
    while True:
        kind_wine = {'1':'КЛАСИФІКАЦІЯ ВИН','2':'ХАРАКТЕРИСТИКИ ФРУКТОВИХ СОКІВ',
                     '3': 'ВИХІД В ПОПЕРЕДНЄ МЕНЮ','0':'ВИХІД З ПРОГРАМИ'}
        create_list(kind_wine)
        ans = input("\tВАШ ВИБІР ......    ")
        print("\n")
        if ans == "1":
            choice_for_reed('kind_wine')
        elif ans == "2":
            choice_for_reed('charact_prod')
        elif ans == "3":
            print("Exit in previosly menu не працюэ")

            # break

        if ans == "0":
            print("ВИХІД З ПРОГРАМИ")
            exit()
        else:
            print("ЗРОБІТЬ СВІЙ ВИБІР")

# main_wine_f()