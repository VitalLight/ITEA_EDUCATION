""""
У введеному рядкові перевірити, чи кількість голосних букв рівна кількості непарних.
"""

riadok = input ("Введіть будь-який вираз:  ")

def filt (b):
    count = 0
    c = b.lower()
    str = list(c)
    golos_byk = ['а', 'о', 'у', 'е', 'и', 'і','я','ю','є','ї']
    for i in str:
        for j in golos_byk:
            if i == j:
                count += 1
    return count

# Kil = filt(riadok)

print(riadok)

if filt(riadok) % 2 == 0:
    print("\nКількість голосних букв ---%s --- парна" % filt(riadok))
else:
    print("Кількість голосних букв ---%s --- НЕ ПАРНА" % filt(riadok))
