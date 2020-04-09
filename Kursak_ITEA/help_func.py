
def create_list(dict):
    for i in dict:
        print(f"{i} - {dict.get(i)}")


def choice_for_reed(a):
    with open(r'd:\\Python_ITed\\Kursak_ITEA\\_1_klasificacia_wine\\' + a + '.txt','r') as kind_wine:
        text_w = kind_wine.read()
        print(text_w)


def sum_pokaznuk_na_obiem (a, b, c):
    c = c + round((a * b), 2)
    return c


def midl_value (a, b):
    c = round((a / b), 2)
    return c


def zagalni_dani():
    sugar = float(input("\n\t\t\tВВЕДІТЬ ВМІСТ ЦУКРУ, %  \t\t\t\t\t\t").replace(',', '.'))
    acid = float(input("\t\t\t\tВВЕДІТЬ КІЛЬКІСТЬ ТИТРОВАНИХ КИСЛОТ, %\t\t\t").replace(',', '.'))
    micnist = float(input("\t\t\t\tВВЕДІТЬ МІЦНІСТЬ, %\t\t\t").replace(',', '.'))
    v_juice = float(input("\t\t\t\t\tВВЕДІЬ ОБЄМ, л\t\t\t\t").replace(',', '.'))
    return sugar, acid, micnist, v_juice


def dani_micnocti_():
    while True:
        try:
            micnist = float(input("\n\t\t\t\tВВЕДІТЬ МІЦНІСТЬ, %\t\t\t").replace(',', '.'))
            sugar = float(input("\t\t\tВВЕДІТЬ ВМІСТ ЦУКРУ, %  \t\t\t\t\t\t").replace(',', '.'))
            acid = float(input("\t\t\t\tВВЕДІТЬ КІЛЬКІСТЬ ТИТРОВАНИХ КИСЛОТ, %\t\t\t").replace(',', '.'))
            break
        except ValueError:
            print("ПРАВИЛЬНО ВВЕДІТЬ ДАНІ")
    return micnist, sugar, acid


def add_alc(a, b, c, d):
    v_clear_alc = round((d*((a-b)/(c-b))), 2)
    v_osn_wine = round((d-v_clear_alc), 2)
    return v_clear_alc, v_osn_wine


def clear_pokaznuk(sugar, acid, v_osn_wine, v_kripl_wine):
    sugar_pererah = sugar * v_osn_wine
    acid_pererah = acid * v_osn_wine
    koncentrac_sugar_kripl_w = round((sugar_pererah / v_kripl_wine), 2)
    koncentrac_acid_kripl_w = round((acid_pererah / v_kripl_wine), 2)
    return koncentrac_sugar_kripl_w, koncentrac_acid_kripl_w


# Розрахунок етилового спирту
def spurt_in_wine(a, b, c, d, e):
    spurt = round(((a * b - c * d)/e), 2)
    return spurt


# Розхід бурякового цукру
def sugar_in_wine(a, b, c, d):
    sugar_wine = round((((a * b - c * d) / 10.5)/10), 2)
    v_sugar_wine = round((sugar_wine * 0.62), 2)
    return v_sugar_wine, sugar_wine


# Розхід води
def add_water(a, b, c, d, e, w):
    while True:
        if b <= d:
            water = round((a - c - e - w), 2)
            break
        elif b > d:
            water = 0
            break
    return water
