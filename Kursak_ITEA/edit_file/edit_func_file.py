import json
from Kursak_ITEA.help_func import create_list

charact_fruits = 'calculation\\charact_fruits.json'
charact_prod = 'klasificacia_wine\\charact_prod.txt'


class Fruiteadd:

    def __init__(self):
        self.name = input("ВКАЖІТЬ НАЗВУ ФРУКТУ\t\t\t")
        self.sugar = input("ВКАЖІТЬ ВМІСТ ЦУКРІВ, %\t\t\t")
        self.acid = input("ВКАЖІТЬ ВМІСТ ТИТРОВАНИХ КИСЛОТ, %\t\t\t")
        self.outjuice = input("ВКАЖІТЬ ВИХІД СОКУ ІЗ СВІЖИХ ФРУКТІВ, %\t\t\t")

    def add_to_file(self):
        # Відкриваєм json файл для читанння
        with open(charact_fruits, 'r') as f:
            json_dict_text = json.loads(f.read())
        key = str(len(json_dict_text) + 1)
        new_frukt = {key: f"{self.name.upper()}\t/ вміст цукру в соці {self.sugar}, кислотність {self.acid}, "
                          f" вихід соку зі свіжих плодів {self.outjuice}%"}

        # Запис в json файл для запису
        json_dict_text.update(new_frukt)
        with open(charact_fruits, 'w') as f:
            json.dump(json_dict_text, f)
        create_list(json_dict_text)

        # Створюємо нову інформацію та відкриваємо txt файл для її запису
        new_txt_text = f"{self.name.capitalize()}\t\t\t/\t\t{self.sugar}\t\t/\t\t{self.acid}\t\t/" \
                       f"\t\t{self.outjuice}\t\t/\n" \
                       f"-----------------------------------------------------------------------------/\n"
        with open(charact_prod, 'a+') as f:
            f.write(new_txt_text)


class DelFruits:

    def __init__(self):
        self.key = input("\nВВЕДІТЬ НОМЕР ФРУКТУ\t\t\t")

    def del_from_file(self):
        with open(charact_fruits, 'r') as f:
            json_dict_text = json.loads(f.read())
            if self.key not in json_dict_text.keys():
                print("ВИХІД У ПОТОЧНЕ МЕНЮ, ОСКІЛЬКИ НЕ ВКАЗАНО ЖОДНОГО НАЯВНОГО КЛЮЧА")
                return

        # Видалення зі словника елементу та присвоєння значення цього словника  змінній name_fruit
        name_fruit = json_dict_text.get(self.key).split("/")[0].capitalize()
        del json_dict_text[self.key]
        new_dict = {}

        # Цикл для переприсвоєння номерів ключів у послідовність
        i = 1
        for j in list(json_dict_text):
            new_dict[str(i)] = json_dict_text.pop(j)
            i += 1
            new_dict.update(new_dict)

        #  Запис в json файл
        with open(charact_fruits, 'w') as f:
            json.dump(new_dict, f)
        create_list(new_dict)

        # Відкрити на прочитання тхт файл . знайти в ньому ключове слово  фрукта
        with open(charact_prod, 'r') as f:
            del_txt_text = f.readlines()

            # Пошук по елементах масиву пошукового слова
            k = 0
            for el_mas in del_txt_text:
                if name_fruit in str(el_mas):
                    row = k
                    del del_txt_text[row + 1]
                    del del_txt_text[row]
                k += 1
        #  Запис в txt файл
        with open(charact_prod, 'w') as f:
            f.writelines(del_txt_text)


# Початок основої програми
def start_edit():
    while True:
        print("\n МЕНЮ --- ДОДАВАННЯ/ ВИДАЛЕННЯ ФРУКТІВ ТА ХАРАКТРИСТИК ЇХ СОКІВ ---")
        dict_action = {'1': 'ДОДАТИ ФРУКТ ТА ЙОГО ХАРАКТЕРИСТИКИ',
                       '2': 'ВИДАЛИТИ ФРУКТ ТА ЙОГО ХАРАКТЕРИСТИКИ',
                       '3': 'ВИХІД В ПОПЕРЕДНЄ МЕНЮ',
                       '0': 'ВИХІД'}
        create_list(dict_action)
        answer = input("\nОБЕРІТЬ, ЩО ПОТРІБНО ЗРОБИТИ З МЕНЮ ВИЩЕ\t")
        if answer == '1':
            print("ВНЕСЕННЯ ФРУКТУ ТА ЙОГО ОСНОВНИХ ХАРАКТЕРИСТИК")
            fruit_n = Fruiteadd()
            fruit_n.add_to_file()
        elif answer == '2':
            print("ВИДАЛЕННЯ ФРУКТУ ТА ЙОГО ОСНОВНИХ ХАРАКТЕРИСТИК")
            with open(charact_fruits, 'r') as f:
                create_list(json.loads(f.read()))
            fruit_remove = DelFruits()
            fruit_remove.del_from_file()
        elif answer == '3':
            print("ВИХІД В ПОПЕРЕДНЄ МЕНЮ")
            return
        elif answer == '0':
            print("ВИХІД З ПРОГРАМИ")
            exit()
        else:
            print("ЗРОБІТЬ СВІЙ ВИБІР")
