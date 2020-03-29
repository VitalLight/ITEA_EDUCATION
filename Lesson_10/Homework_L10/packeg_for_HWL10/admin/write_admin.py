
import json

def perev(file):
    a = input("ПЕРЕДИВИТИСЬ ФАЙЛ У ЯКИЙ ДОБАВИЛИ ІНФОРМАКЦІЮ? +/ - \t")
    if a == "+":
        with open('d:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\artical\\' + file + '.txt','r+') as f:
            text = f.read()
            print(text)


def add_new_file_to_jsonfile(f_name):
    with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\list_articals.json', 'r') as f:
        list_art = json.loads(f.read())
        for i in list_art:
            print(f"{i} - {list_art.get(i)}")
        key = input("ВВВЕДІТЬ ВІЛЬНИЙ ПОШУКОВИЙ НОМЕР ФАЙЛУ\t")
        list_art.update({key:f_name})
        with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\list_articals.json', 'w') as f:
            json.dump(list_art, f)


def decor_only_write(only_read):
    print("\n ПЕРЕЛІК СТАТЕЙ ДЛЯ РЕДАГУВАННЯ (ЗАТЕРИТИ СТАРИЙ ТЕКСТ/ДОЗАПИСУ)")
    list_art = only_read()
    number = input("\nВКАЖІТЬ НОМЕР СТАТТІ( ЯКЩО ТАКА Є), ІНАКШЕ ВКАЖІТЬ - 0(НУЛЬ)\t")
    regim_info = """\t\t\t РЕЖИМИ ЗАПИСУ ФАЙЛУ
                    1---:'w-витре все у файлі, якщо такий існує ',
                    2---:'a+ дозапис інформації в кінці файлу',
                    3---:'x- створить новий файл для запису, якщо такий відстуній, інакше виключеня"""
    print(regim_info)
    regim = {'1': 'w', '2': 'a+', '3': 'x'}
    w_regim = input("ВИБЕРІТЬ РЕЖИМ ЗАПИСУ ФАЙЛУ(ВКАЖІТЬ ЦИФРУ)\t")


    def wrapper():
        if number != '0' and w_regim != '3':
            with open('d:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\artical\\' +
                      list_art.get(number) + '.txt', regim.get(w_regim)) as f:
                sms = input("ВВЕДІТЬ, ІНФОРМАЦІЮ ЯКУ ПОТРІБНО ЗАПИСАТИ/ДОПИСАТИ У ФАЙЛ\n")
                article = f.write("\n"+sms)
                print(f"\n {article}")
        elif number == '0' and w_regim == '3':
            f_name = input("ВКАЖІТЬ НАЗВУ ФАЙЛУ БЕЗ РОЗШИРЕННЯ\t")
            with open('d:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\artical\\'+
                      f_name+'.txt', regim.get(w_regim)) as f:
                sms = input("ВВЕДІТЬ, ІНФОРМАЦІЮ ЯКУ ПОТРІБНО ЗАПИСАТИ У ФАЙЛ\n")
                article = f.write("\n"+sms)
                print(f"\n {article}")
        elif number != '0' and w_regim == '3':
            print("ПРИ ОБРАНИХ УМОВАХ РЕДАГУВАННЯ ФАЙЛУ НЕ МОЖЛИВЕ")
            #  функція, що перепитує чи є потреба переглянути файл після редагування
        if number != '0' and w_regim != '3':
            perev(list_art.get(number))
        elif number == '0' and w_regim == '3':
            perev(f_name)
        #  функція що записує новий файл в словник з переліком усіх статей
        add_new_file_to_jsonfile(f_name)

    return wrapper


@decor_only_write
def only_read():
    with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\list_articals.json','r') as f:
        list_art = json.loads(f.read())
        for i in list_art:
            print(f"{i} - {list_art.get(i)}")
        return list_art
only_read()

