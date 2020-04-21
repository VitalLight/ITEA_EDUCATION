import json


def enter():
    passw = input("ДЛЯ ВХОДУ ВВЕДІТЬ СВЙ ПАРОЛЬ\t\t\t")
    with open(r'enter_in_prog\\pasw_for_enter.json', 'r') as f:
        text_pas = json.loads(f.read())
        if passw in text_pas:
            print("ВАШ СТАТУС ---ADMIN---. ВИ МОЖЕТЕ РЕДАГУВАТИ ФАЙЛИ")
            password = "admin"
            return password
        else:
            print("ВАШ СТАТУС ---USER---. ВИ МОЖЕТЕ ЛИШЕ ЧИТАТИ ФАЙЛИ")
