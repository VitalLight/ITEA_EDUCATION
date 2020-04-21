from Kursak_ITEA.help_func import sum_pokaznuk_na_obiem, midl_value, zagalni_dani


def repag_wine_and_juice():
    print(" \nВИ МОЖЕТЕ ВВЕСТИ ДО 10 ОДИНИЦЬ ВИН")
    sum_dobutky_sugar_v_juice = 0
    sum_dobutky_acid_v_juice = 0
    sum_dobutky_micnist_v_juice = 0
    sum_v_juice = 0
    kil = 0
    prod = list()
    while kil <= 10:
        try:
            product = input("\nВВЕДІТЬ НАЗВУ ОСНОВНОГО ПРОДУКТУ\t\t\t")
            sugar, acid, micnist, v_juice = zagalni_dani()

            # Добутки показника на обєм
            sum_dobutky_sugar_v_juice = sum_pokaznuk_na_obiem(sugar, v_juice,  sum_dobutky_sugar_v_juice)
            sum_dobutky_acid_v_juice = sum_pokaznuk_na_obiem(acid, v_juice, sum_dobutky_acid_v_juice)
            sum_dobutky_micnist_v_juice = sum_pokaznuk_na_obiem(micnist, v_juice, sum_dobutky_micnist_v_juice)
            sum_v_juice = v_juice + sum_v_juice

            # Масив із назвами продуктів
            prod.append(product)
            kil = kil + 1
            print(f"ЗАЛИШИЛОСЬ  {10 - kil}  ВНЕСЕНЬ ДО АВТОМАТИЧНОГО ВИХОДУ\n")
            answer = input("ПРОДОВЖИТИ ВНЕСЕННЯ ОДИНИЦЬ ПРОДУКЦІЇ ?   + / -   ")
            if answer == "+":
                continue
            else:
                break
        except ValueError:
            print("\nВСІ ПОЛЯ ПОВИННІ МАТИ ЧИСЛОВІ ЗНАЧЕННЯ. ПОВТОРІТЬ ВСЕ СПОЧАТКУ ДЛЯ ОСТАНЬОГО ВВЕДЕНОГО ПРОДУКТУ ")
    return sum_dobutky_sugar_v_juice, sum_dobutky_acid_v_juice, sum_dobutky_micnist_v_juice, sum_v_juice, prod


# Значення після купажу
def after_kypag(a, b, c, d):
    sugar_midl = midl_value(a, d)
    acid_midl = midl_value(b, d)
    micnist_midl = midl_value(c, d)
    return sugar_midl, acid_midl, micnist_midl


def main_kypag():
    sum_dobutky_sugar_v_juice, sum_dobutky_acid_v_juice, sum_dobutky_micnist_v_juice, sum_v_juice, prod \
        = repag_wine_and_juice()
    sugar_midl, acid_midl, micnist_midl = after_kypag(sum_dobutky_sugar_v_juice, sum_dobutky_acid_v_juice,
                                                      sum_dobutky_micnist_v_juice, sum_v_juice)
    print(f"СКУПАЖОВАНЕ З {prod} ПРОДУКТІВ ВИНО БУДЕ МАТИ:\n"
          f"\t\t\tМІЦНОСТІ --- {micnist_midl}%\n"
          f"\t\t\tЦУКРИСТОСТІ --- {sugar_midl}%\n"
          f"\t\t\tКИСЛОТНОСТІ --- {acid_midl}%\n"
          f"\t\t\tЗАГАЛЬНИЙ ОБЄМ --- {sum_v_juice} літрів\n")
