
import json


def decor_only_read(only_read):
    print("\n ПЕРЕЛІК СТАТЕЙ ДЛЯ ЧИТАННЯ")
    list_art = only_read()
    number = input("\nВКАЖІТЬ НОМЕР СТАТТІ\t")
    def wrapper():
        with open('d:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\artical\\' + list_art.get(number) + '.txt',
                'r') as f:
            article = f.read()
            print(f"\n {article}")
    return wrapper


@decor_only_read
def only_read():
    with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\list_articals.json','r') as f:
        list_art = json.loads(f.read())
        for i in list_art:
            print(f"{i} - {list_art.get(i)}")
        return list_art
only_read()
