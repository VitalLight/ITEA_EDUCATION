print("ВВести 3 числа(a,b,c) і вивести їх в порядку зростання")

try:
    a = int(input('\n '
                  'Введіть число a:    '))
    b= int(input('Введіть число b:    '))
    c= int(input('Введіть число c:    '))
except:
    print ('\n'
           '                Останнє введене число містить символи відмінні від цифр')
# знаходимо максимум числа:
if a>b and a>c and(b>c or c>b):
    max = a
elif b>a and b>c and (a>c or c>a):
    max = b
else:
    max=c
#знаходимо мінімум числа
if a<b and a<c and(b>c or c>b):
    min = a
elif b<a and b<c and (a>c or c>a):
    min = b
else:
    min=c

# визначаємо послідовність в зротанні
if max==a and min ==b:
    print("числа в послідовності зростання %s, %s, %s" %(b,c,a))
elif max==a and min ==c:
    print("числа в послідовності зростання %s, %s, %s" % (c, b, a))
elif max==b and min ==a:
    print("числа в послідовності зростання %s, %s, %s" % (a, c, b))
elif max==b and min ==c:
    print("числа в послідовності зростання %s, %s, %s" % (c, a, b))
elif max==c and min ==a:
    print("числа в послідовності зростання %s, %s, %s" % (a, b, c))
else:
    print("числа в послідовності зростання %s, %s, %s" % (b, a, c))

print("\n"
      "                      Завдання виконано!")
