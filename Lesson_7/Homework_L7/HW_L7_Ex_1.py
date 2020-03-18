""""
Користувач вводить рядок. Вивести на екран довжину найдовшого підрядка з даного рядка,
 в якому всі символи унікальні(тобто не повторюються).
 Наприклад: abcabcbb - Результат: 3 (“abc” - найдовший підрядок)
ccagrtfsdc - Результат: 8
aaa - Результат: 1

"""

riadok = input("\n Введіть рядок: ")

def sort (a):
    arr = list(a)
    l_arr = len (a)
    bar = []
    # Створення масиву введено рядка в коді Юнікода
    for i in a:
        bar.append(ord(i))
    bar.sort()

    # Сорування коду Юнікода в унікальну послідовність
    bar2 = []
    d = 0
    for j in range(len(bar)):
        c = bar[j] /2
        if c > d:
            d = c
            bar2.append(chr(bar[j]))
    unic_sent  = ''.join(bar2)
    return unic_sent

unic_sent = sort(riadok)
print("ДОВЖИНА УНІКАЛЬНОГО РЯДКА --- %s --- символи --- %s "%(len(unic_sent), unic_sent))

#  запуск функції функції по сортуванню та
sort(riadok)
