from Kursak_ITEA.help_func import dani_micnocti_, zagalni_dani, spurt_in_wine, sugar_in_wine, add_water

def condition_kupag():
    print("ПРОГРАМА РОЗРАХУНКУ КУПАЖУ ЗБРОЖЕНО-СПИРТОВОГО СОКУ ДО УМОВ\n")
    while True:
        print(" ВКАЖІТЬ ХАРАКТЕРИСТИКИ ЯКИМ МАЄ БУТИ ГОТОВЕ КУПАЖНЕ ВИНО")
        try:
            sugar, acid, micnist, v_wine = zagalni_dani()
            procent_spurty = float(input("\n\t\t\t\tВВЕДІТЬ ДОЛЮ ЕТИЛОВОГО СПИРТУ В РОЗЧИНІ, %\t\t\t").replace(',', '.'))
            print(" \nВВЕДІТЬ ХАРАКТЕРИСТИКИ ЗБРОЖЕНО-СПИРТОВОГО СОКУ/ВИНА")

            micnist_juice, sugar_juice, acid_juice = dani_micnocti_()
    # перевірка чи вміст кислоти  у зброженому соці/вині більше запланованого
            if acid > acid_juice:
                print("!!!!!!!КИСЛОТНІСТЬ ПЛАНОВАНОГО ВИНА МАЄ БУТИ"
                      " МЕНШОЮ ЗА КИСЛОТНІСТЬ ЗБРОЖЕНО-СПИРТОВОГО СОКУ/ВИНА!!!!!!!")
                continue
            break
        except ValueError:
            print("КОРЕКТНО ВВЕДІТЬ ДАНІ")

    #  кількість зброжено спитового соку
    v_zbrog_juice = round(((v_wine * acid)/ acid_juice), 2)

    #  розрахунок етилового спирту
    spurt = spurt_in_wine(v_wine, micnist, v_zbrog_juice, micnist_juice, procent_spurty)

    #   розхід бурякового цукру
    v_sugar_wine, sugar_wine = sugar_in_wine(v_wine, sugar, v_zbrog_juice, sugar_juice)

    #   розхід води
    water = add_water(v_wine, acid, v_zbrog_juice, acid_juice, spurt, v_sugar_wine)

    print(f"'\n ДЛЯ ВИГОТОВЛЕННЯ {v_wine}л ВИНА, ПОТРІБНО:\n"
          f" {v_zbrog_juice}літрів ЗБРОЖЕНО-СПИРТОВОГО СОКУ \n"
          f" \t{spurt}літрів {procent_spurty}% РОЗЧИНУ СПИРТУ \n"
          f" \t\t{sugar_wine}кг ЦУКРУ,\n"
          f" \t\t\t{ water}літрів ВОДИ\n")



condition_kupag()


