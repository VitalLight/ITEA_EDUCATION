""""
Розшифрування шрифта Віженера.
"""
def unshufr (text, key):
    #  символи для шифрування
    sumbs = "_' .,:;-+1234567890АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя" \
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    l_s = list(sumbs)

    l_key = list(key)
        #  автоматично коректує довжину ключа

    if len(text) >= len(key):
        c_key = len(text)//len(key)
        ost_key = len(text) % len(key)
        key1 = key*c_key + key[:ost_key:]

    if len(text) < len(key):
        key1 = key[:len(text):]

    list_sms = list(text)
    list_key = list(key1)

# ФУНКЦІЯ присвоєння індексів повідомленю та ключу відносно зміної sumbs
    def ind_ (iteral):
        a = []
        for i in iteral:
            for j in l_s:
                if i == j:
                    a.append(l_s.index(j))
                    continue
                else:
                     pass
        return a

    sms_ind = ind_(list_sms)  # виводить  символи з list_sms в змінну- це числовий масив
    key_ind = ind_(list_key)  # виводить  символи з list_key в змінну - це числовий масив

    # функція що створює масив з індексами для букв(символів) РОЗШИФРОВАНОГО повідомлення
    def unsecrchar_(sms_ind, key_ind):
        unsec_char = []
        for i in range(len(text)):
            if (sms_ind[i] - key_ind[i]) <= 0:
                unschar = sms_ind[i] - key_ind[i] + len(sumbs)
            elif 0 < (sms_ind[i] - key_ind[i]) <= len(l_s):
                unschar = sms_ind[i] - key_ind[i]
            unsec_char.append(unschar)
        return unsec_char

    unsecrsms = unsecrchar_(sms_ind, key_ind)  # масив з індексами для букв(символів) розсекреченого повідомлення

#   створення самого(розсекреченого) повідомлення- це будуть самі букви(символи)
    def unsecr_povid_(a,b):
        unsec_povidomlenia = []
        for i in range(len(a)):  # ітерація по масиву кількості елем iter(це довжина повідомлення)
            for j in range(len(b)):  # ітерація по масиву кількості l_s
               if int(a[i]) == int(b.index(b[j])):  #  виведений елемент індекс для розшифр повідом прирівн до індексу
                                                    # елементу в масиві l_s
                    unsec_povidomlenia.append(b[j])
        return unsec_povidomlenia

    unsecr_povid_(unsecrsms, l_s)
    unsec_chr = unsecr_povid_(unsecrsms,l_s) #  масив букв зашифорованого повідомлення
    unssms = ''.join(unsec_chr)

    return unssms, key





