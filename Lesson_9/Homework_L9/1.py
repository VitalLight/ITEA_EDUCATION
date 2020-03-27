import json
d = {}
# функція виводить в основну програму вміст прочитаного файлу як словник
def inner_json_file():
    #  щоб програма працювала потрібно аби у файлі на самому початку був порожній словник
    with open('d:\\Python_ITed\\Lesson_9\\Homework_L9\\key_pasw_L9exTest.json', 'r') as f:
        result_open = json.loads(f.read())  # прочитаний вміст файлу (обєкту) розкодовуєтсья як словник
    return result_open


d = inner_json_file()  # пайтон бачить d як словник
# print(type(d))
# print(d)

key = input("new enter key   ")
pas = input("new enter pas   ")
d.update({key: pas})

with open('d:\\Python_ITed\\Lesson_9\\Homework_L9\\key_pasw_L9exTest.json', 'w') as f:
    # i = input("Enter a key   ")
    # del d[i]
    json.dump(d, f)  #  словник записуєтсья як обєкт у файл

print(d)