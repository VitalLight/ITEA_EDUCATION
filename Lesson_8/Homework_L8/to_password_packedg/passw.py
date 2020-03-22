""""
Реалізувати шифр Віженера.
"""
def shufr ():
    #  символи для шифрування
    sumbs = "'., :;\/1234567890АБВГҐДЕЄЖЗИІЇЙКЛМОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмопрстуфхцчшщьюя" \
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    l_s = list(sumbs)
    # print(len(sumbs))

    sms = input("\nВведіть ПОВІДОМЛЕННЯ для генерації паролю:   ")

    key = input("Введіть КЛЮЧ:  ")
    l_key = list(key)


#  автоматично коректує довжину ключа

    if len(sms) >= len(key):
        c_key = len(sms)//len(key)
        ost_key = len(sms) % len(key)
        key1 = key*c_key + key[:ost_key:]
        # print(" \nВаш СКОРЕКТОВАНИЙ КЛЮЧ  --- %s" % key1)

    if len(sms) < len(key):
        key1 = key[:len(sms):]
        # print(" \nВаш СКОРЕКТОВАНИЙ КЛЮЧ --- %s" % key1)

    list_sms = list(sms)
    list_key = list(key1)

# ФУНКЦІЯ присвоєння індексів повідомленю та ключу відносно зміної sumbs
    def ind_ (iteral):
        a = []
        for i in iteral:
            for j in l_s:
                if j == i:
                    # print(i, j)
                    a.append(l_s.index(j))
                    continue
                else:
                     pass
        return a

    sms_ind = ind_(list_sms)  # виводить  символи з list_sms в змінну- це числовий масив
    key_ind = ind_(list_key)  # виводить  символи з list_key в змінну - це числовий масив
    # print(sms_ind, key_ind)

    # функція що створює масив з індексами для букв(символів) секретного повідомлення
    def secrchar_(sms_ind, key_ind):
        sec_char = []
        for i in range(len(sms)):
            schar = sms_ind[i] + key_ind[i]
            sec_char.append(schar)
        return sec_char


    secrsms = secrchar_(sms_ind, key_ind)  # масив з індексами для букв(символів) секретного повідомлення
    # print(secrsms)

#   створення секретного(зашифрованого) повідомлення- це будуть самі букви
    k = 0
    def secr_povid_(a,b):
        sec_povidomlenia = []
        for i in range(len(a)):  # ітерація по масиву кількості елем iter(це довжина повідомлення чи паролю)
            for j in range(len(b)):
                if int(a[i]) >= int(len(b)):
                    k = int(a[i]) % int(len(b))
            sec_povidomlenia.append(b[k])
        return sec_povidomlenia

    secr_povid_(secrsms, l_s)
    sec_chr = secr_povid_(secrsms,l_s) #  масив букв зашифорованого повідомлення
    parol = ''.join(sec_chr)

    # print("\n ВАШ ПАРОЛЬ     %s  " % parol)
    return key, parol





