
Nkard = input("Введіть номер своєї кредитної карти(16  цифр)   ")

#ВВодяться дані щодо терміну дії картки
dd_yy = input("Введіть термін дії кредитної карти у форматі (місяць/рік)) у форматі mm/yy    :")
a=dd_yy.split("/",2)# створюємо список елементи якого у введеній стрічці Пайтон бачить через розділювач "/",
# 2 - означає кількість частин

# Вводимо значення CVV
CVV = input ("ВВедіть номер CVV - 3 числа   ")

# перевіряємо чи в номері карти введені лише цілі числа
try:
    intNkard = int(Nkard)
except ValueError: #  працює і без ValueError Чому?
    print ('Не всі символи в номері карти цифри. Номер карти повинен містити лише цифри!')
if len(Nkard)<16:
    print (" \nУ номер карти введено менше 16 цифр")
if len(Nkard)>16:
    print (" \n             У номер карти введено більше 16 цифр")

# перевіряємо на правильність введення формату місяця (mm) в терміну дії карти в int, якщо правда, то помилки не буде
if len (a[0]) ==2:
    try:
        idd = int(a[0])
    except :
        print ('\n          НЕ правильно введений формат місяця. Правильно введіть формат місяця!')
else:
    print("                 Потрібно вірно ввести формат місяця - 2 цифри")


# перевіряємо на правильність введення формату року (yy)в терміну дії карти в int, якщо правда, то помилки не буде
if len (a[1]) ==2:
    try:
        print (a[1])
        iyy = int(a[1])
    except :
        print ('\n          НЕ правильно введений формат року. Правильно введіть формат року!')
else:
    print("                 Потрібно вірно ввести формат Року - 2 цифри")


# перевірка правильності введення CVV
if len(CVV)==3:
    try:
        iCVV = int(CVV)
    except:
        print("              Введене число CVV НЕ відповідного формату")

if (len (Nkard) ==16 and intNkard == int(Nkard)) \
        and (len (a[0]) ==2 and idd == int (a[0]))\
        and (len (a[1]) ==2 and iyy == int(a[1])) \
        and (len(CVV)==3 and iCVV == int(CVV)):

    print ("\n              Ha-ha-ha.Now I will use your credit card! А людською мовою- Було Ваше стало Наше")
else:
    print (" \n             ВВеди дані правильно і жити стане ВЕСЕЛІШЕ!")







