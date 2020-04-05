""""
Написати програмку, яка буде міняти місцями слова зігзагоподібній формі.
Тобто користувач вводить рядок, і вказує довжину стовпчика.
Якщо було введено слово “PAYPALISHIRING” і довжину стовпчика 4, то має утворитися ось такий зігзаг і
новий рядок буде “PINALSIGYAHRPI” (Якщо читати зігзаг по рядку, то утвориться таке слово).
Якщо було для цього рядка вказано довжину стовпчика 3, то має утворитися слово “PAHNAPLSIIGYIR”.
"""
sentense = input("ВВЕДІТЬ СЛОВО ЧИ РЕЧЕННЯ\t\t\t")
s = sentense.split(" ")
sentense_join = "".join(s)
long_coolums = int(input("ВВЕДІТЬ ВКАІЖІТЬ ДОВЖИНУ СТОВПА\t\t\t"))
long_1_zig = long_coolums + long_coolums - 2
#  додаткові пробіли  в кінець введеного виразу
a = ((len(sentense_join)//long_1_zig) + 1) * long_1_zig - len(sentense_join)
cor_sentens_join = sentense_join + a * " "

list_sent = []
for i in cor_sentens_join:
    list_sent.extend(i)
for i in range(long_coolums):
    a = []
    if i == 0:
        for j in range(i, len(list_sent), long_1_zig - i * 2):
            e = list_sent[j]
            space = (long_1_zig - long_coolums - i) * " "
            sum = e + space
            a.extend(sum)
            # c = " ".join(a)
        print(" ".join(a))
    if 0 < i <= long_coolums - 2:
        for j in range(i, len(list_sent), long_1_zig):
            element1 = list_sent[j]
            space1 = (long_1_zig - long_coolums - i) * " "
            c = j + (long_1_zig - 2 * i)
            element2 = list_sent[c]
            space2 = (long_coolums - 2 - 1 - (long_1_zig - long_coolums - i)) * " "
            sum = element1 + space1 + element2 + space2
            a.extend(sum)
        print(" ".join(a))
    if i == long_coolums - 1:
        for j in range(i, len(list_sent), long_1_zig):
            e = list_sent[j]
            space = (long_1_zig - long_coolums) * " "
            sum = e + space
            a.extend(sum)
        print(" ".join(a))
