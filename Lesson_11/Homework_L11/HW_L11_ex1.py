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


class Person:
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


    def __str__(self):
        return f"Імя контакту {self.name}, Мобільний номер контакту: {self.phone}"


class Notebok:
    def __init__(self):
        # В даній змінній ми будемо зберігати список об'єктів(не словників) контактів(імя, номер і тд)
        self.list_of_contacts = list()
    
    def add_new_contact(self):
        """
        Тут ми будемо створювати нові контакти. 
        1. Попросимо в користувача дані
        2. Створимо об'єкт Contact
        3. Додамо його до списку наших контактів
        4. Запишемо це у файл
        """
        f_name = input("enter first name     ")
        l_name = input("enter last name     ")
        mail = input("enter number mail    ")
        n_phone = input("enter number phone    ")
        streete = input("enter street           ")
        n_house = input("enter number house    ")
        touwn = input("enter touwn    ")

        # Створюємо новий об'єкт
        cont = Contact(f_name, l_name, mail, n_phone, streete, n_house, touwn)
        # додамо його до списку існуючих контактів
        self.list_of_contacts.append(cont) # повертаєтсья сюди після read_contact
        # запишемо контакти у файл (за допомогою self ми викликаємо іншу функцію в цьому класі, це як допоміжне слово щоб нас зрозуміли що ми хочемо)
        self.write_contacts_to_file()

    def read_contact(self):
        """
        В Даному методі ми відкриємо наш json файл, і зчитаємо звідти всі контакти, які вже були створені раніше
        На кожній ітерації, ми будемо створювати новий об'єкт Contact для кожного контакту
        і створимо масив таких об'єктів
        """
        with open(r'test.json', 'r') as f: # ???? якщо прописуємо шлях до файлу коротко, то то він буде знаходитись у папці де основний файл?
            masiv_contact = json.loads(f.read())  # з файлу записується рядок
            print(masiv_contact)
        # masiv_contact - це буде список словників{} контактів
        for contact_dict in masiv_contact: # ??? як розуміти. Назва слоника одна, а словників до цієї назви декілька
            # Отримуємо всі дані зі словника назва словника  ----  ???contact_dict(чи це назва елемента в списку словників) назву ми ніде не обявляли!!!!
            name = contact_dict["name"]
            prizv = contact_dict["prizv"]
            email = contact_dict["email"]
            phone = contact_dict["phone"]
            house = contact_dict["house"]
            misto = contact_dict["misto"]
            streete = contact_dict["streete"]
            # Створюємо новий об'єкт Contact
            new_contact = Contact(name, prizv, email, phone, house, misto, streete) # ??? для чого його тут створювати? а змінну masiv_contact одразу не можна роздрукувати?
            print(new_contact)
            # Додаємо його до списку контактів до об'єкта Notebok
            self.list_of_contacts.append(new_contact)

    def write_contacts_to_file(self):
        mas_dict = list()
        """
        В даному методі ми будемо записувати список контактів у json файл
        Як ми будемо записувати дані у файл: У нас є список об'єктів Contact.
        Вони зберігаються у змінній self.list_of_contacts
        У файл нам треба записати масив словників
        Значить треба запустити ітерацію по нашому списку контактів
        далі створити словник із об'єкту Contact (???той що є в зміній self.list_of_contacts?)
        Додати цей словник до масиву, який ми будемо записувати у файл
        і далі записати цей масив у файл
        """
        for contact in self.list_of_contacts: #  він з методу add_new_contact цього класу
            # Ось так ми створюємо словник, який потім будемо додавати до масиву і записувати далі у файл
            dict_contact = {  # ??? як цей словник розуміє, що змінні це є ключі? Що означає contact.хххххх (як його читати)?
                "name": contact.name,
                "email": contact.email,
                "prizv": contact.prizv,
                "phone": contact.phone,
                "misto": contact.misto,
                "house": contact.house,
                "streete": contact.streete 
            }
            mas_dict.append(dict_contact)

        with open(r'test.json', 'w') as f:
            json.dump(mas_dict, f)

notebook = Notebok()
notebook.read_contact()
notebook.add_new_contact()
print(notebook.list_of_contacts[])

