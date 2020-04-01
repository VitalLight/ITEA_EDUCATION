import string
from Kursak_ITEA.help_func import create_list

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
    kil = input("ВВЕДІТЬ НОМЕРА ФРУКТІВ МАЙБУТНЬОГО ВИНА У ФОРМАТІ Х/Х/Х/   ")
    kil_fruktiv = kil.split("/")

    # цикл перевіряє чи правильно введені числові значення та перетворює їх у формат int
    b = []
    for i in range(len(kil_fruktiv)):
        if kil_fruktiv[i] != "" and int(kil_fruktiv[i]) <= int(len(fruit)):
            b.append(int(kil_fruktiv[i]))
        else:
            print("ВИ НЕ ОБРАЛИ ЖОДНОГО ФРУКТУ. РОБОТУ ПРОГРАМИ ЗАКІНЧЕНО.")
            exit()

    arr_fruit = []
    # створюється масив даних з введених фруктів
    # ВВОДЯТЬСЯ ДАНІ ЩОДО ЦУКРИСТОСТІ, КИСЛОТНОСТІ ТА ОБЄМУ СОКУ КОЖНОГО ФРУКТУ
    sum_acid = 0
    sum_sugar = 0
    sum_v_juice = 0
    for i in b:
        print(f'\n {fruit[i]},  {fruit_characteristic[i]}')
        while True:
            try:
                sufar = float(input("\n\t\t\tВВЕДІТЬ ВМІСТ ЦУКРУ У СОЦІ, %  \t\t\t\t\t\t").replace(',','.'))
                acid2 = float(input("\t\t\t\tВВЕДІТЬ КІЛЬКІСТЬ ТИТРОВАНИХ КИСЛОТ У СОЦІ, %\t\t\t").replace(',','.'))
                v_juice = float(input("\t\t\t\t\tВВЕДІЬ ОТРИМАНИЙ ОБЄМ СОКУ, л\t\t\t\t").replace(',','.'))
                break
            except ValueError:
                print("\nВСІ ПОЛЯ ПОВИННІ МАТИ ЧИСЛОВІ ЗНАЧЕННЯ. ПОВТОРІТЬ ВСЕ СПОЧАТКУ ")
        sum_acid = round(sum_acid + (acid2*v_juice), 2)
        sum_sugar = round(sum_sugar + (sufar * v_juice), 2)
        sum_v_juice = round((sum_v_juice + v_juice), 2)
        arr_fruit.append(fruit[i])
    k_acid = round((sum_acid/sum_v_juice), 2)
    k_sugar = round((sum_sugar/sum_v_juice), 2)
    print(f"\n ВИНО БУДЕ З НАСТУПНИХ ФРУКТІВ {arr_fruit}")
    print(f"\n СУМІШ СОКІВ ЦИХ ФРУКТІВ МАЄ У СВОЄМУ СКЛАДІ \n"
          f"\t -ТИТРОВАНИХ КИСЛОТ - {k_acid}% \n"
          f"\t - ЦУКРУ - {k_sugar}% \n"
          f"\t - ЗАГАЛЬНИЙ ОБЄМ СОКУ {sum_v_juice} \n")
    return k_acid, k_sugar, sum_v_juice


def main_exec_():
    print("ЯКИМ ПОВИННЕ БУТИ ГОТОВЕ ВИНО ПО:")
    acid_wine = float(input("\t КИСЛОТНОСТІ, %\t\t\t").replace(',', '.'))
    shugar = float(input("\t ЦУКРИСТОСТІ, %\t\t\t\t\t").replace(',','.'))
    while True:
        micnist = float(input("\t МІЦНОСТІ, % \t\t\t\t\t").replace(',', '.'))
        if micnist <= 15:
            break
        else:
            print(f"ВКАЗАНА МІЦНІСТЬ ---{micnist}%---, ЩО БІЛЬШЕ МАКСИМАЛЬНОГО 15%. ЗМЕНШІТЬ МІЦНІСТЬ")
    return acid_wine, micnist


#  функція визначає скільки потрібно добавити ВОДИ до соку/сусла, щоб отримати необхідну кислотність
def corr_acid(k_acid, acid_wine, sum_v_juice):
    water = round(((k_acid / acid_wine) - 1),2)
    v_all_water = round((water * sum_v_juice),2)
    v_water_juice = (v_all_water + sum_v_juice)
    if k_acid >= acid_wine:
        print(f"\n ЩОБ ОТРИМАТИ ВИНО КИСЛОТНОСТЮ {acid_wine}%  ДО СОКУ ПОТРБІНО ДОБАВИТИ {v_all_water} літрів ВОДИ")
    else:
        pass
    return v_water_juice


  #  рахується кількість цукру що потрібно добавити до сусла аби отримати заявлену міцність
def sugar(micnist, shugar, v_water_juice,sum_v_juice,k_acid, acid_wine,):
    mas_sug = (micnist - (shugar/2))*2*10*v_water_juice
    v_sug = (mas_sug*0.6)/1000
    mas_v_sug = v_sug *(micnist - (shugar/2))*2*10
    all_mas_sug = round((mas_sug + mas_v_sug),2)
    if k_acid >= acid_wine:
        v_wine_end = round((v_water_juice + v_sug),2)
    else:
        v_wine_end = sum_v_juice
    print(f"ЩОБ ОТРИМАТИ ВИНО МІЦНОСТЮ {micnist}% ПОТРІБНО ДОДАТКОВО ВИКОРИСТАТИ {all_mas_sug} грам ЦУКРУ ")
    print(f"ОБЄМ ГОТОВОГО ВИНА СТАНОВИТИМЕ ПРИБЛИЗНО {v_wine_end} літрів")
    return all_mas_sug, v_wine_end


#  функція для знаходження кількості кислоти для підкислення вина
def add_acid(k_acid, acid_wine,v_wine_end):
    if k_acid < acid_wine:
        plus_acid = v_wine_end * (acid_wine - k_acid)
        print(f"ЩОБ ОТРИМАТИ ВИНО КИСЛОТНОСТЮ { acid_wine} ПОТРІБНО ДО НЬОГО ДОДАТИ {plus_acid}грам ЛИМОННОЇ КИСЛОТИ\n"
              f"ПРИ ЦЬОМУ ОБЄМ ВИНА ЗБІЛЬШИТЬСЯ НА {0.6*plus_acid/1000} літрів")
    else:
        plus_acid = 0
    return plus_acid


def all_func_calc_wine():
    k_acid, k_sugar, sum_v_juice = fruit_inform()
    acid_wine, micnist  = main_exec_()
    v_water_juice = corr_acid(k_acid, acid_wine, sum_v_juice)
    all_mas_sug, v_wine_end = sugar(micnist, k_sugar, v_water_juice, sum_v_juice, k_acid, acid_wine,)
    plus_acid = add_acid(k_acid, acid_wine, v_wine_end)
    # return all_func_calc_wine

# all_func_calc_wine()