""""
Написати контактний довідник. Має бути реалізовано такі класи: Person, Address, Contact, Notebook.
Клас Contact повинен одночасно наслідуватися від класу Address та Person.
Після запуску програми користувач повинен мати змогу додавати нові контакти, переглядати існуючі, робити пошук по імені.
 Всі ці методи пошуку, додавання, перегляду мають бути розміщені у класі Notebook.
 Контактну інформацію зберігати у файлі у довільному форматі.
 При запуску програми із файлу зчитувати всі контактні дані.
Для кожного контакту створювати динамічно об’єкт типу Contact і додавати його до масиву всіх контактів.
Масив контактів зберігати як поле contacts всередині класу Notebook.
"""
import json
print("КОНТАКТНИЙ ДОВІДНИК")

class Notebok:
    def __init__(self,  name, contact):
        self.name = name
        self.number = contact

    def view_contact(self, name):
        pass
    def create_contact(self, name, contact):
        pass

    def add_new_contact(self, name, contact):
        with open(r'D:\\Python_ITed\\Lesson_11\\Homework_L11\\dict_contact.json','r') as f:
            dict_contact = json.loads(f.read())
            dict_contact.update({name: contact})

            with open(r'D:\\Python_ITed\\Lesson_11\\Homework_L11\\dict_contact.json', 'w') as f:
                json.dump(dict_contact, f)
            # print(dict_contact)
            return dict_contact

class Person(Notebok):
    def __init__(self, name):
        super().__init__(name)


class Address:
    def __init__(self, adr):
        self.adress = adr

class Contact(Notebok):
    def __init__(self):
        with open(r'D:\\Python_ITed\\Lesson_11\\Homework_L11\\dict_contact.json', 'r') as f:
            dict_contact = json.loads(f.read())
            for i in dict_contact:
                k = (f"{(i)} - {dict_contact.get(i)}")
                print(str(k))
        # pass
    def dim_mas_cont(self):
        pass



        # super().__init__(name, contact)
        # return
        # mas_cont = []

#  додає нові контакти
# dict_contact  = {}
# while True:
    # name = input("enter name     ")
    # contact = input("enter number     ")
    # n_cont = Notebok(name, contact)
    # # print(n_cont.number)
    # n_cont.add_new_contact(name, contact)
    # break

#  dinamic object
cont = Contact()
# c = cont.dim_mas_cont()

# print(f'має бути перелік контактів {cont.dim_mas_cont()}')
