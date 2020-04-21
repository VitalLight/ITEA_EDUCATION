import string
import json

from Kursak_ITEA.help_func import create_list, zagalni_dani


def fruit_inform():

    # Показати список фруктів
    with open(r'D:\\Python_ITed\\Kursak_ITEA\\_2_calculation\\charact_fruits.json', 'r') as f:
        fruit_characteristic = json.loads(f.read())
        for key in fruit_characteristic.keys():
            slice_fruit = ((fruit_characteristic.get(key)).split("/"))[slice(1)]
            # Роздруковуються фрукти
            print(key + " - " + str(slice_fruit))
    while True:
        try:
            k = ""
            kil = input("\nВВЕДІТЬ НОМЕРА ФРУКТІВ МАЙБУТНЬОГО ВИНА У ФОРМАТІ Х/Х/Х/ ( 0 - ВИХІД З ПРОГРАМИ)\t\t\t")
            if kil == "0":
                print("ВИХІД З ПРОГРАМИ")
                exit()
            kil_fruktiv = kil.split("/")
            for i in kil_fruktiv:
                if i not in fruit_characteristic.keys():
                    k = k + i + ', '
            if k != "":
                print(f"НОМЕР(А) ФРУКТУ(ІВ) --- {k} --- ВІДСУТНІ(Й) В НАДАНОМУ ПЕРЕЛІКУ АБО ЗАПИС НЕ ВІДПОВІДАЄ ФОРМАТУ."
                      f"ВВЕДІТЬ ДАНІ У ВІДПОВІДНОСТІ З ПЕРЕЛІКОМ ")
                continue
            else:
                break
        except AttributeError:
            print("ВВЕДІТЬ ДАНІ У ВКАЗАНОМУ ФОРМАТІ")
        return k

    arr_fruit = []
    # Вводяться дані щодо цукристості, кислотності та обєму соку кожного фрукту
    sum_acid = 0
    sum_sugar = 0
    sum_v_juice = 0
    sum_micnist_j = 0
    for key in kil_fruktiv:
        print(f"\nВВЕДІТЬ ВХІДНІ ДАНІ В СОЦІ / ЗБРОЖЕНО-СПИРТОВОМУ СОЦІ --- " + str((fruit_characteristic.get(key)).split("/")[slice(1)]))
        print(f'ХАРАКТЕРИСТИКА СОКУ  -----  {((fruit_characteristic.get(key)).split("/"))[slice(1, 2)]}')
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
        arr_fruit.append(str((fruit_characteristic.get(key)).split("/")[slice(1)]))
    k_acid = round((sum_acid/sum_v_juice), 2)
    k_sugar = round((sum_sugar/sum_v_juice), 2)
    k_micnist_j = round((sum_micnist_j/ sum_v_juice), 2)
    print(f"\n ВИНО БУДЕ З НАСТУПНИХ ФРУКТІВ {''.join(arr_fruit)}")
    print(f"\n СУМІШ СОКІВ ЦИХ ФРУКТІВ МАЄ У СВОЄМУ СКЛАДІ:\n"
          f"\t -ТИТРОВАНИХ КИСЛОТ - {k_acid}% \n"
          f"\t - ЦУКРИСТІСТЬ - {k_sugar}% \n"
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


# Функція визначає скільки потрібно добавити ВОДИ до соку/сусла, щоб отримати необхідну кислотність
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

#  Рахується кількість цукру яку потрібно добавити до сусла аби отримати заявлену міцність
def sugar(shugar_w, micnist, k_sugar, sum_v_juice, k_micnist, k_acid, acid_wine, v_water_juice):
    sugar_to_micnosti = ((micnist) - (k_sugar/2) - k_micnist) * 20
    mas_sug = round(((sugar_to_micnosti + shugar_w * 10) * v_water_juice), 2)
    v_sug = (mas_sug * 0.62) / 1000
    if k_acid >= acid_wine:
        v_wine_end = round((v_water_juice + v_sug), 2)
    else:
        v_wine_end = sum_v_juice
    return mas_sug, v_wine_end


#  Функція для знаходження кількості кислоти для підкислення вина
def add_acid(k_acid, acid_wine,v_wine_end):
    if k_acid < acid_wine:
        plus_acid = v_wine_end * (acid_wine - k_acid)
        print(f"ЩОБ ОТРИМАТИ ВИНО КИСЛОТНОСТЮ { acid_wine}% ПОТРІБНО ДО НЬОГО ДОДАТИ {round(plus_acid,2)}грам ЛИМОННОЇ КИСЛОТИ\n"
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


