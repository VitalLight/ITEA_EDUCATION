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

class Person():
    def __init__(self, f_name, l_name, mail, n_phone):
        self.name = f_name
        self.prizv = l_name
        self.email = mail
        self.phone = n_phone

class Address:
    def __init__(self, streete, n_house, touwn):
        self.streete = streete
        self.house = n_house
        self.misto = touwn


class Contact(Person, Address):
    def __init__(self, f_name, l_name, mail, n_phone, streete, n_house, touwn):
        Person.__init__(self, f_name, l_name, mail, n_phone)
        Address.__init__(self, streete, n_house, touwn)

    def read_contact(self):
        with open(r'D:\\Python_ITed\\Lesson_11\\Homework_L11\\dict_contact.json', 'r') as f:
            masiv_contact = json.loads(f.read())  # з файлу записується рядок

            contacts = list()
            for i in range (len(masiv_contact)):
                new_contact = new_cont
                print(new_contact)
                contacts.append(new_contact)

class Notebok:
    def __init__(self):
        pass


    # def add_new_contact(self, new_cont):
    #     with open(r'D:\\Python_ITed\\Lesson_11\\Homework_L11\\dict_contact.json', 'r') as f:
    #         masiv_contact = json.loads(f.read())
    #
    #         dict_contact.update(new_cont)
    #
    #         with open(r'D:\\Python_ITed\\Lesson_11\\Homework_L11\\dict_contact.json', 'w') as f:
    #             json.dump(dict_contact, f)
    #         # print(dict_contact)
    #         return dict_contact




#  додає нові контакти
# dict_contact  = {}
while True:
    f_name = input("enter first name     ")
    l_name = input("enter last name     ")
    mail = input("enter number mail    ")
    n_phone = input ("enter number phone    ")
    streete = input("enter street           ")
    n_house = input("enter number house    ")
    touwn = input("enter touwn    ")
    break

#  dinamic object
new_cont = Contact(f_name, l_name, mail, n_phone, streete, n_house, touwn)
new_cont.read_contact()


# new_cont.add_new_contact(new_cont)
