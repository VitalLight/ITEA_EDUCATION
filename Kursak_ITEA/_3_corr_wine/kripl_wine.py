from Kursak_ITEA.help_func import dani_micnocti_, add_alc, clear_pokaznuk


def main_kripl():

    while True:
        print("\nВХІДНІ ДАНІ. НЕОБХІДНО СТВОРИТИ КРІПЛЕНЕ ВИНО:")
        try:
            v_kripl_wine = float(input("ОБЄМОМ, л\t\t\t").replace(',', '.'))
            micnist_kripl_wine = float(input("МІЦНІСТЮ, %\t\t\t").replace(',', '.'))
            alc_for_kripl = float(input("\nВВЕДІТЬ % ЕТИЛОВОГО СПИРТУ В РОЗЧИНІ ДЛЯ КРІПЛЕННЯ \t\t\t").replace(',', '.'))
            product = input("\nВВЕДІТЬ НАЗВУ БАЗОВОГО ПРОДУКТУ З ЯКОГО БУДЕМО СТВОРЮВАТИ КРІПЛЕНЕ ВИНО \t\t\t")
            print(" ВКАЖІТЬ ЙОГО ХАРАКТЕРИСТИКИ")
            micnist, sugar, acid = dani_micnocti_()
            if micnist_kripl_wine < micnist:
                print("!!!!!!!ПОМИЛКА ПРИ ВВЕДЕННІ ДАНИХ. "
                      "МІЦНІСТЬ КРІПЛЕНОГО ВИНА ПОВИННА БУТИ БІЛЬШЕ НІЖ НАЯВНА!!!!!!!")
                continue
            else:
                break
        except ValueError:
            print("ПРАВИЛЬНО ВВЕДІТЬ ДАНІ")

    v_clear_alc, v_osn_wine = add_alc(micnist_kripl_wine, micnist, alc_for_kripl, v_kripl_wine)

    #  функція знаходить вміст цукрів та кислот у кріпленому вині
    koncentrac_sugar_kripl_w, koncentrac_acid_kripl_w = clear_pokaznuk(sugar, acid, v_osn_wine, v_kripl_wine)
    print(f"\nДЛЯ ПРИГОТУВАННЯ {v_kripl_wine} л КРІПЛЕНОГО ВИНА ПОТРІБНО ВИКОРИСТАТИ:\n"
          f" {v_clear_alc} л  {alc_for_kripl}% СПИРТОВОГО РОЗЧИНУ,\n"
           f" {v_osn_wine} л БАЗОВОГО ПРОДУКТУ {product}. \n"
           f"ВМІСТ ЦУКРУ У КРІПЛЕНОМУ ВИНІ БУДЕ СТАНОВИТИ  {koncentrac_sugar_kripl_w}%, А КИСЛОТ {koncentrac_acid_kripl_w}%")

# main_kripl()