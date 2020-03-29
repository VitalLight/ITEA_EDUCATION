import json

def ed_parol_rol():

    with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\parol_rol.json', 'r') as f:
        edit_parol_rol = json.loads(f.read())
    print("\n ПРОГРАМА ДЛЯ РЕДАГУВАННЯ ПАРОЛІВ ТА РОЛЕЙ КОРИСТУВАЧІВ")

    while True:
        print("\nЗІ СПИСКУ НИЖЧЕ ОБЕРІТЬ СВІЙ НАМІР ЩОДО РЕДАГУВАННЯ")
        action = {'ДОДАТИ/ЗАМІНИТИ': 'НАТИСНИ - 1', 'ВИДАЛИТИ': 'НАТИСНИ - 2', 'ВИХІД': 'НАТИСНИ - 0'}
        for i in action:
            print(f"\t{i} - {action.get(i)}")
        check_action = input("\n ОБЕРІТЬ НАМІР \t")
        #  ДОДАТИ/ЗАМІНИТИ
        if check_action == "1":
            print("\nПЕРЕЛІК НАЯВНИХ ВСІХ ПАРОЛІВ ТА РОЛЕЙ КОРИСТУВАЧІВ")
            print("ПАРОЛЬ - РОЛЬ")
            for i in edit_parol_rol:
                print(f"\t{i} - {edit_parol_rol.get(i)}")
            parol = input("ВВЕДІТЬ НОВИЙ ПАРОЛЬ\t")
            print("ОБЕРІТЬ ДЛЯ КОРИСТУВАЧА РОЛЬ\t\t\t")
            dic_constumers = {'ADMIN':'НАТИСНИ - 1 ','EDITOR':'\tНАТИСНИ - 2','USER':'\tНАТИСНИ - 3'}
            for i in dic_constumers:
                print(f"\t{i} - {dic_constumers.get(i)}")

            while True:
                constumers = input("ЗРОБІТЬ СВІЙ ВИБІР\t")
                if constumers == "1":
                    edit_parol_rol.update({parol: "ADMIN"})
                    break
                elif constumers == "2":
                    edit_parol_rol.update({parol: "EDITOR"})
                    break
                elif constumers == "3":
                    edit_parol_rol.update({parol: "USER"})
                    break
                elif constumers != "1" and constumers != "2" and constumers != "3":
                    print("ОБЕРІТЬ РОЛЬ КОРИСТУВЧУ ІЗ ЗАПРОПОНОВАНОГО")
                    continue
            #  запис оновленого доступу у файл
            with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\parol_rol.json', 'w') as f:
                json.dump(edit_parol_rol, f)

            ans = input("ПРОДОВЖИТИ ? +/-\t")
            if ans == "-":
                print("\n ВИ ВИЙШИ З ПРОГРАМИ РЕДАГУВАННЯ")
                break
        #  ВИДАЛИТИ
        elif check_action == "2":
            with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\parol_rol.json', 'r') as f:
                edit_parol_rol = json.loads(f.read())
            print("\nПЕРЕЛІК НАЯВНИХ ВСІХ ПАРОЛІВ ТА РОЛЕЙ КОРИСТУВАЧІВ")


            while True:
                print("ПАРОЛЬ - РОЛЬ")
                for i in edit_parol_rol:
                    print(f"\t{i} - {edit_parol_rol.get(i)}")
                del_el = input(" ВКАЖІТЬ ПОШУКОВИЙ НОМЕР(ПАРОЛЬ) ФАЙЛУ, АБО ENTER - ДЛЯ ВИХОДУ \t")

                if del_el == "":
                    print("\n ВИХІД")
                    break
                elif del_el not in edit_parol_rol.keys():
                    print(edit_parol_rol.keys())
                    print("\n ВКАЗАНИЙ КЛЮЧ НЕ ІСНУЄ. ПОВТОРІТЬ СПРОБУ")
                    continue
                else:
                    del edit_parol_rol[del_el]
                edit_parol_rol.update()
                with open('D:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\parol_rol.json', 'w') as f:
                    json.dump(edit_parol_rol, f)
        #  ВИХІД
        elif check_action != "1" and check_action != "2":
            print("\n ВИ ВИЙШИ З ПРОГРАМИ РЕДАГУВАННЯ")
            break


# ed_parol_rol()