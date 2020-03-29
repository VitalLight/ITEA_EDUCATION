import  json

def add_del_file_json_list():
    add_del = {'ДОДАТИ':'НАТИСНИ - 1','ВИДАЛИТИ':'НАТИСНИ - 2'}
    for i in add_del:
        print(f"{i} - {add_del.get(i)}")
    a = input("ОБЕРІТЬ ДІЮ\t")
    if a == "1":
        with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\list_articals.json', 'r') as f:
            list_art = json.loads(f.read())
            while True:
                for i in list_art:
                    print(f"{i} - {list_art.get(i)}")
                add_el = input(" ВКАЖІТЬ ПОШУКОВИЙ НОМЕР ФАЙЛУ\t")
                add_name_file = input(" ВКАЖІТЬ НАЗВУ ФАЙЛУ БЕЗ РОЗШИРЕННЯ \t")
                list_art.update({add_el:add_name_file})
                with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\list_articals.json', 'w') as f:
                    json.dump(list_art, f)
                a = input(" ПРОДОВЖИТИ ? +/-\t")
                if a == "-":
                    break
                else:
                    continue

    elif a == "2":
        with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\list_articals.json', 'r') as f:
            list_art = json.loads(f.read())
            while True:
                for i in list_art:
                    print(f"{i} - {list_art.get(i)}")
                del_el = input(" ВКАЖІТЬ ПОШУКОВИЙ НОМЕР ФАЙЛУ \t")
                if del_el not in list_art.keys():
                    print("\n ВКАЗАНИЙ КЛЮЧ НЕ ІСНУЄ. ВИХІД З ПРОГРАМИ")
                    break
                else:
                    del list_art[del_el]
                list_art.update()
                with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\list_articals.json', 'w') as f:
                    json.dump(list_art, f)
                    a = input(" ПРОДОВЖИТИ ? +/-\t")
                    if a == "-":
                        break
                    else:
                        continue