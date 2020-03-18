""""
Реалізувати шифр Віженера.
"""
from string import ascii_letters
"""
Шифрування abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
52 символи
"""
while True:
    sms = input("\nВведіть ПОВІДОМЛЕННЯ для шифрування:   ")
    key = input("Введіть КЛЮЧ (к-ть символів як у повідомленні:  ")
    if len(sms) != len(key) or sms.isalpha() == False or key.isalpha() == False:
        print("\nКількість символів повідомлення та ключа має бути однаковою та містити лише АНГ.букви")
        continue
    else:
        break

list_sms = list(sms)
list_key = list(key)

# присвоєння ord символів повідомленю та ключу- Для шифррування
def ord_ (iteral):
    a = []
    for i in iteral:
        if i in ascii_letters:
            a.append(ord(i))
        else:
            a.append(0)
    return a

sms_ord = ord_(list_sms)  # виводить ord символи з list_sms в змінну- це числовий масив
key_ord = ord_(list_key) # виводить ord символи з list_key в змінну - це числовий масив

#  функція для визначення секретних символів
def secrchar_(sms_ord, key_ord):
    sec_char = []
    for i in range(len(sms)):
        schar = sms_ord[i] + key_ord[i]
        sec_char.append(schar)
    return sec_char


secrsms = secrchar_(sms_ord, key_ord)  # масив з числами секретного повідомлення
print(" secrsms = %s" %secrsms)

# присвоєння chr символів секретному повідомленю
def chr_(iter):
    sec_chr = []
    for i in range(len(iter)):  # ітерація по масиву кількості елем iter
       d = iter[i]
        while d > 122:  # обчислення індекса для букви зашифрованого повідомлення
            num = 65 + d - 122
            d = num
            if 97 > num > 90:
                num = num + 7
        for j in ascii_letters:  # ітерація по основних символах шифррування
                        #print("j = first %s -%s" % (j, ord(j)))
                        # num2 = ord(j)
            if ord(j) == num:
                sec_chr.append(j)  # МАСИВ з буквеним шиформ коду
                # print("j =  %s" % ord(j))
                break
            else:
                continue
    #sec_chr.append(j)
    return sec_chr

chr_(secrsms)
sec_chr = chr_(secrsms) #  масив букв зашифорованого повідомлення
print(" Зашифроване повідомлення  %s" %sec_chr)  #  масив букв зашифорованого повідомлення
print(''.join(sec_chr)) #  Текст зашифорованого повідомлення

