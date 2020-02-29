a= input(' Enter number_1  ')
b= input(' Enter number_2  ')
c= input(' Enter number_3  ')

"якщо буде правда, tо відбудеться виконання інструкції try"
try:# перевіряється чи  введенні дані як цілі числа
    aK= int(a)
    bK = int(b)
    cK = int(c)
except ValueError:
    print(" You enter not all Number as Number")
    exit()# виходить з цієї програми якщо інструкція try  відбулася

if (a>b and a>c) and (b>c or b<c):
    print('Number max %s' %a)
elif (b>a and b>c) and (a>c or a<c):
        print('Number max %s' %b)
else:
    print('Number max %s' %c)


