import json
from Kursak_ITEA.help_func import create_list

class Fruite_add:

    def __init__(self, name, sugar, acid, outjuice):
        self.name = input("ВКАЖІТЬ НАЗВУ ФРУКТУ\t\t\t")
        self.sugar = input("ВКАЖІТЬ ВМІСТ ЦУКРІВ, %\t\t\t")
        self.acid = input("ВКАЖІТЬ ВМІСТ ТИТРОВАНИХ КИСЛОТ, %\t\t\t")
        self.outjuice = input("ВКАЖІТЬ ВИХІД СОКУ ІЗ СВІЖИХ ФРУКТІВ, %\t\t\t")

    def add_to_file(self):
        #  відкриваєм json файл для читанння
        with open(r'D:\\Python_ITed\\Kursak_ITEA\\_2_calculation\\charact_fruits.json', 'r') as f:
            json_dict_text = json.loads(f.read())
        key = str(len(json_dict_text) + 1)
        new_frukt = {key: f"{(self.name).upper()}\t/ вміст цукру в соці {self.sugar}, кислотність {self.acid}, "
                          f" вихід соку зі свіжих плодів {self.outjuice}%"
                     }
         # запис в json файл для запису
        json_dict_text.update(new_frukt)
        with open(r'D:\\Python_ITed\\Kursak_ITEA\\_2_calculation\\charact_fruits.json', 'w') as f:
            json.dump(json_dict_text, f)
        print(json_dict_text)

        # відкриваємо txt файл для читання
        with open(r'D:\\Python_ITed\\Kursak_ITEA\\_1_klasificacia_wine\\charact_prod.txt', 'r') as f:
            txt_text = f.read()
        new_txt_text = f"{(self.name).capitalize()}\t\t\t/\t\t{self.sugar}\t\t/\t\t{self.acid}\t\t/\t\t{self.outjuice}\t\t/\n" \
                       f"-----------------------------------------------------------------------------/\n"
        # відкриваємо txt файл для запису
        with open(r'D:\\Python_ITed\\Kursak_ITEA\\_1_klasificacia_wine\\charact_prod.txt', 'a+') as f:
            f.write(new_txt_text)


class Del_Fruits(Fruite_add):

    def __init__(self, key):
        self.key = input("ВВЕДІТЬ КЛЮЧ ФРУКТУ\t\t\t")

    def del_from_file(self):
        #  видалення зі словника елементу та присвоєння значення цього словника  змінній name_fruit
        name_fruit = json_dict_text.get(self.key).split("/")[0].capitalize()

         #  json_dict_text.pop(self.key)
        del json_dict_text[self.key]
        new_dict = {}
        #  цикл для переприсвоєння номерів ключів у послідовність
        i = 1
        for j in list(json_dict_text):
            new_dict[str(i)] = json_dict_text.pop(j)
            i += 1
            new_dict.update(new_dict)

        #  запис в json файл
        with open(r'D:\\Python_ITed\\Kursak_ITEA\\_2_calculation\\charact_fruits.json', 'w') as f:
            json.dump(new_dict, f)
        print(create_list(new_dict))

        # відкрити на прочитання тхт файл . знайти в ньому ключове слово  фрукта
        with open(r'D:\\Python_ITed\\Kursak_ITEA\\_1_klasificacia_wine\\charact_prod.txt', 'r') as f:
            del_txt_text = f.readlines()
            k = 0
            #  пошук по елементах масиву пошукового слова
            for el_mas in del_txt_text:
                if name_fruit in str(el_mas):
                    row = k
                    del del_txt_text[row + 1]
                    del del_txt_text[row]
                k += 1
        with open(r'D:\\Python_ITed\\Kursak_ITEA\\_1_klasificacia_wine\\charact_prod.txt', 'w') as f:
            f.writelines(del_txt_text)


#  початок основої програми
while True:
    print("\n МЕНЮ")
    dict_action = {"1": "ДОДАТИ ФРУКТ ТА ЙОГО ХАРАКТЕРИСТИКИ",
                   "2": "ВИДАЛИТИ ФРУКТ ТА ЙОГО ХАРАКТЕРИСТИКИ",
                   "0": "ВИХІД"
                   }
    print(create_list(dict_action))
    answer = input("\nОБЕРІТЬ, ЩО ПОТРІБНО ЗРОБИТИ З МЕНЮ ВИЩЕ\t")
    if answer == '1':
        print("ВНЕСЕННЯ ФРУКТУ ТА ЙОГО ОСНОВНИХ ХАРАКТЕРИСТИК")
        fruit_n = Fruite_add(name="", sugar="", acid="", outjuice="")
        fruit_n.add_to_file()
    elif answer == '2':
        print("ВИДАЛЕННЯ ФРУКТУ ТА ЙОГО ОСНОВНИХ ХАРАКТЕРИСТИК")
        with open(r'D:\\Python_ITed\\Kursak_ITEA\\_2_calculation\\charact_fruits.json', 'r') as f:
            json_dict_text = json.loads(f.read())
        print(f"\n {create_list(json_dict_text)}")
        fruit_remove = Del_Fruits(key="")
        fruit_remove.del_from_file()
    elif answer == '0':
        exit()
    else:
        print("ЗРОБІТЬ СВІЙ ВИБІР")

