print("\n КОНВЕКТОР ВАЛЮТ ДЛЯ ГРИВНІ, ДОЛАРА ТА ЄВРО ")

print ("               \nВкажіть валюту Яку хочете перевести")
V1 = input("           Гривні - grn, Долари - dol, Євро -evro    ")
if  not V1=="grn" and not  V1=="dol" and not V1=="evro":
    print ("Перезапустіть конвертер. Правильно введіть дані Яку волюту конвертувати")
    exit()

print ("                \nВкажіть валюту В яку хочете перевести")
V2 =input("            Гривні - grn, Долари - dol, Євро -evro    ")
if  not V2=="grn" and not  V2=="dol" and not V2=="evro":
    print ("Перезапустіть конвертер. Правильно введіть дані В яку волюту конвертувати")
    exit()
try:
    S = float (input("\nБазова сума для конвертування в %s    "% V1 ))
except:
    print("ВВедіть суму цілим числом. Запустіть конвертор спочатку")
    exit()
try:
    Kurs = float(input("\nВкажіть курс: Вартість 1 %s в %s  " % (V2,V1)))
except:
    print ("ВВедіть курс цілим числом. Запустіть конвертор спочатку")

konvek = S/Kurs

print("     \nВи отримаєте %s %s "%(konvek,V2))