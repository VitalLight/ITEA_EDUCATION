""""
Реалізувати шифр Віженера.
"""
def shufr(text):
    #  символи для шифрування
    sumbs = "_' .,:;-+1234567890АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя" \
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    l_s = list(sumbs)

     key = input("Введіть КЛЮЧ:  ")
    l_key = list(key)

#  автоматично коректує довжину ключа
    if len(text) >= len(key):
        c_key = len(text)//len(key)
        ost_key = len(text) % len(key)
        key1 = key*c_key + key[:int(ost_key):]
    if len(text) < len(key1):
        key1 = key[:len(text):]

    list_sms = list(text)
    list_key = list(key1)

# ФУНКЦІЯ присвоєння індексів повідомленю та ключу відносно зміної sumbs
    def ind_(iteral):
        a = []
        for i in iteral:
            for j in l_s:
                if j == i:
                    a.append(l_s.index(j))
                    continue
                else:
                     pass
        return a

    sms_ind = ind_(list_sms)  # виводить  символи з list_sms в змінну- це числовий масив
    key_ind = ind_(list_key)  # виводить  символи з list_key в змінну - це числовий масив

    # функція що створює масив з індексами для букв(символів) секретного повідомлення
    def secrchar_(sms_ind, key_ind):
        sec_char = []
        for i in range(len(text)):
            schar = sms_ind[i] + key_ind[i]
            sec_char.append(schar)
        return sec_char

    secrsms = secrchar_(sms_ind, key_ind)  # масив з індексами для букв(символів) секретного повідомлення

#   створення секретного(зашифрованого) повідомлення- це будуть самі букви/символи
    def secr_povid_(a,b):
        k = 0
        sec_povidomlenia = []
        for i in range(len(a)):  # ітерація по довжині секретного повідомлення
            for j in range(len(b)):  # ітерація по масиву кількості елем iter(це довжина повідомлення чи паролю)
                if int(a[i]) >= int(len(b)):  #  порівнюється числове значення a[i] з довжиною повдіомлення len(b)

                    c = int(a[i]) // int(len(b))  # k
                    k = int(a[i]) - c*int(len(b))  # new
                elif 0 <= int(a[i]) < int(len(b)):
                    k = int(a[i])  # new
            sec_povidomlenia.append(b[k])
        return sec_povidomlenia
    secr_povid_(secrsms, l_s)
    sec_chr = secr_povid_(secrsms,l_s) #  масив букв зашифорованого повідомлення
    parol = ''.join(sec_chr)
    return key, parol





