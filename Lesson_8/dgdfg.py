# a = '       '
# print(len(a))
# print(list(a))
# print(ord(a[4]))

# a = 'gorod'
# b = a[:2:]
# print(b)

sumbs = "'_ .,:;1234567890АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯабвгґдеєжзиіїйклмнопрстуфхцчшщьюя" \
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
l_s = list(sumbs)

sms = input("\nВведіть ПОВІДОМЛЕННЯ для генерації паролю:   ")
list_sms = list(sms)
def ind_(iteral):
    a = []
    for i in iteral:
        for j in l_s:
            if j == i:
                print (i)
                # print(i, j, l_s.index(j))
                a.append(l_s.index(j))
                continue
            else:
                pass
    return a

sms_ind = ind_(list_sms)

print(sms_ind)
print(len(sms_ind))