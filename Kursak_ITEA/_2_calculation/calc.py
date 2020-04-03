import string
from Kursak_ITEA.help_func import create_list, zagalni_dani

def fruit_inform():
    fruit = {1:'ЯБЛУКО', 2:'ГРУША', 3:'СЛИВА', 4: 'ВИШНЯ',
             5: 'АГРУС', 6: 'СМОРОДИНА', 7:'МАЛИНА КУЛЬТУРНА', 8: 'СУНИЦЯ'
    }
    print("\n")
    create_list(fruit)
    fruit_characteristic = {
                1: '\t\t\t вміст цукру в соці (7-20)%, кислотність (0,4-2,5)%, вихід соку зі свіжих плодів (50-65)%',
                2: '\t\t\t вміст цукру в соці (5-16)%, кислотність (0-1,3)%, вихід соку зі свіжих плодів 60%',
                3: '\t\t\t вміст цукру в соці (5-16)%, кислотність (0,25-2)%, вихід соку зі свіжих плодів 45%',
                4: '\t\t\t вміст цукру в соці (6-15)%, кислотність (0-2,4)%, вихід соку зі свіжих плодів 70%',
                5: '\t\t\t вміст цукру в соці 8,2%, кислотність 1,4%, вихід соку зі свіжих плодів 60%',
                6: '\t\t\t вміст цукру в соці (5-15)%, кислотність (1,0-3)%, вихід соку зі свіжих плодів 50%',
                7: '\t\t\t вміст цукру в соці (5-14)%, кислотність (0,5-1,5)%, вихід соку зі свіжих плодів (55-65)%',
                8: '\t\t\t вміст цукру в соці (3-13)%, кислотність (0,5-1,0)%, вихід соку зі свіжих плодів 65%'
    }
    while True:
        try:
            kil = input("ВВЕДІТЬ НОМЕРА ФРУКТІВ МАЙБУТНЬОГО ВИНА У ФОРМАТІ Х/Х/Х/   ")
            kil_fruktiv = kil.split("/")
            break
        except ValueError:
            print("ВВЕДІТЬ ДАНІ У ВКАЗАНОМУ ФОРМАТІ")

    # цикл перевіряє чи правильно введені числові значення та перетворює їх у формат int
    try:
        b = []
        for i in range(len(kil_fruktiv)):
            if kil_fruktiv[i] != "" and int(kil_fruktiv[i]) <= int(len(fruit)):
                b.append(int(kil_fruktiv[i]))
    except ValueError:
        print("ВИ НЕ ОБРАЛИ ЖОДНОГО ФРУКТУ АБО ОБРАЛИ ФРУКТИ ВІДСУТНІ У НАДАНОМУ СПИСКУ. РОБОТУ ПРОГРАМИ ЗАКІНЧЕНО.")
        exit()


    arr_fruit = []
    # створюється масив даних з введених фруктів
    # ВВОДЯТЬСЯ ДАНІ ЩОДО ЦУКРИСТОСТІ, КИСЛОТНОСТІ ТА ОБЄМУ СОКУ КОЖНОГО ФРУКТУ
    sum_acid = 0
    sum_sugar = 0
    sum_v_juice = 0
    sum_micnist_j = 0
    for i in b:
        print(f"\nВВЕДІТЬ ВХІДНІ ДАНІ В СОЦІ АБО ЗБРОЖЕНО-СПИРТОВОМУ СОЦІ --- {fruit[i]}")
        print(f'\n {fruit[i]},  {fruit_characteristic[i]}')
        while True:
            try:
                sugar, acid2, micnist_j, v_juice = zagalni_dani()
                break
            except ValueError:
                print("\nВСІ ПОЛЯ ПОВИННІ МАТИ ЧИСЛОВІ ЗНАЧЕННЯ. ПОВТОРІТЬ ВСЕ СПОЧАТКУ ")
        sum_acid = round(sum_acid + (acid2 * v_juice), 2)
        sum_sugar = round(sum_sugar + (sugar * v_juice), 2)
        sum_v_juice = round((sum_v_juice + v_juice), 2)
        sum_micnist_j = round(sum_micnist_j + (micnist_j * v_juice), 2)
        arr_fruit.append(fruit[i])
    k_acid = round((sum_acid/sum_v_juice), 2)
    k_sugar = round((sum_sugar/sum_v_juice), 2)
    k_micnist_j = round((sum_micnist_j/ sum_v_juice), 2)
    print(f"\n ВИНО БУДЕ З НАСТУПНИХ ФРУКТІВ {arr_fruit}")
    print(f"\n СУМІШ СОКІВ ЦИХ ФРУКТІВ МАЄ У СВОЄМУ СКЛАДІ \n"
          f"\t -ТИТРОВАНИХ КИСЛОТ - {k_acid}% \n"
          f"\t - ЦУКРУ - {k_sugar}% \n"
          f"\t - МІЦНОСТІ - {k_micnist_j}% \n"
          f"\t - ЗАГАЛЬНИЙ ОБЄМ СОКУ {sum_v_juice} \n")
    return k_acid, k_sugar, sum_v_juice, k_micnist_j


def main_exec_():
    print("ЯКИМ ПОВИННЕ БУТИ ГОТОВЕ ВИНО ПО:")
    acid_wine = float(input("\t КИСЛОТНОСТІ, %\t\t\t").replace(',', '.'))
    shugar_w = float(input("\t ЦУКРИСТОСТІ, %\t\t\t\t\t").replace(',','.'))
    while True:
        micnist = float(input("\t МІЦНОСТІ, % \t\t\t\t\t").replace(',', '.'))
        if micnist <= 15:
            break
        else:
            print(f"!!!!!!!ВКАЗАНА МІЦНІСТЬ ---{micnist}%---, ЩО БІЛЬШЕ МАКСИМАЛЬНОГО 15%. ЗМЕНШІТЬ МІЦНІСТЬ!!!!!!!")
    return acid_wine, micnist, shugar_w


#  функція визначає скільки потрібно добавити ВОДИ до соку/сусла, щоб отримати необхідну кислотність
def corr_acid(k_acid, acid_wine, sum_v_juice):
    while True:
        try:
            water = round(((k_acid / acid_wine) - 1), 2)
            if water < 0:
                water = 0
            v_all_water = round((water * sum_v_juice), 2)
            v_water_juice = (v_all_water + sum_v_juice)
            return v_water_juice, v_all_water
        except ZeroDivisionError:
            acid_wine = float(input("КИСЛОТНІСТЬ ВИНА МАЄ БУТИ БІЛЬШЕ НУЛЯ. СКОРЕКТУЙТЕ ЗНАЧЕННЯ, %\t\t\t").replace(',', '.'))
            continue

  #  рахується кількість цукру яку потрібно добавити до сусла аби отримати заявлену міцність
def sugar(shugar_w, micnist, k_sugar, sum_v_juice, k_micnist, k_acid, acid_wine, v_water_juice):
    sugar_to_micnosti = ((micnist) - (k_sugar/2) - k_micnist) * 20
    mas_sug = round(((sugar_to_micnosti + shugar_w * 10) * v_water_juice), 2)
    v_sug = (mas_sug * 0.62) / 1000
    if k_acid >= acid_wine:
        v_wine_end = round((v_water_juice + v_sug), 2)
    else:
        v_wine_end = sum_v_juice
    return mas_sug, v_wine_end


#  функція для знаходження кількості кислоти для підкислення вина
def add_acid(k_acid, acid_wine,v_wine_end):
    if k_acid < acid_wine:
        plus_acid = v_wine_end * (acid_wine - k_acid)
        print(f"ЩОБ ОТРИМАТИ ВИНО КИСЛОТНОСТЮ { acid_wine}% ПОТРІБНО ДО НЬОГО ДОДАТИ {plus_acid}грам ЛИМОННОЇ КИСЛОТИ\n"
              f"ПРИ ЦЬОМУ РОЗРАХОВАНИЙ ОБЄМ ВИНА ЗБІЛЬШИТЬСЯ НА {round((0.6*plus_acid/1000), 2)} літрів")
    else:
        plus_acid = 0
    return plus_acid


def all_func_calc_wine():
    k_acid, k_sugar, sum_v_juice, k_micnist_j = fruit_inform()
    acid_wine, micnist, shugar_w = main_exec_()
    v_water_juice, v_all_water = corr_acid(k_acid, acid_wine, sum_v_juice)
    mas_sug, v_wine_end = sugar(shugar_w, micnist, k_sugar, sum_v_juice, k_micnist_j, k_acid, acid_wine, v_water_juice)
    plus_acid = add_acid(k_acid, acid_wine, v_wine_end)
    print(f"ЩОБ ОТРИМАТИ ВИНО МІЦНОСТЮ {micnist}% ТА {acid_wine}% КИСЛОТНІСТЮ ПОТРІБНО ДОДАТКОВО ВИКОРИСТАТИ:\n"
          f" {mas_sug} грам ЦУКРУ ТА ДОБАВИТИ {v_all_water} літрів ВОДИ \n"
          f"ОБЄМ ГОТОВОГО ВИНА СТАНОВИТИМЕ ПРИБЛИЗНО {v_wine_end} літрів")

all_func_calc_wine()