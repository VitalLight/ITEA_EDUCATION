
import json


def decor_only_write(only_read):
    print("\n ПЕРЕЛІК СТАТЕЙ ДЛЯ РЕДАГУВАННЯ (ДОЗАПИСУ)")
    list_art = only_read()
    number = input("\nВКАЖІТЬ НОМЕР СТАТТІ\t")
    def wrapper():
        with open('d:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\artical\\' + list_art.get(number) + '.txt',
                'a+') as f:
            sms = input("ВВЕДІТЬ, ІНФОРМАЦІЮ ЯКУ ПОТРІБНО ЗАПИСАТИ У ФАЙЛ\n")
            article = f.write("\n"+sms)
            print(f"\n {article}")
        a = input("ПЕРЕДИВИТИСЬ ФАЙЛ У ЯКИЙ ДОБАВИЛИ ІНФОРМАКЦІЮ? +/ - \t")
        if a == "+":
            with open('d:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\artical\\' + list_art.get(number) + '.txt',
              'r') as f:
                print(f.read())
    return wrapper

@decor_only_write
def only_read():
    with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\list_articals.json','r') as f:
        list_art = json.loads(f.read())
        for i in list_art:
            print(f"{i} - {list_art.get(i)}")
        return list_art
only_read()
