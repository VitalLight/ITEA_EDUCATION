""""
Використати вбудовані функції, відфільтрувти масив, щоб залишилися лише цифри, і щоб цифри були унікальними.
 В кінці отримати суму всіх значень масиву.
"""
#   Кількість елементів в масиві
try:
    n = int(input("Enter quantity elements in masiv:  "))
except ValueError:
    print ("Quantity elements in masiv is inccorect. Try ender again")
    exit()

#  Створення масиву для обробки
masiv = []
for i in range (n):
    elem_masivy = input("Enter ---{}--- elements in masive:  ".format(i+1))
    masiv.append(elem_masivy) # Елементи масиву у стрічках

#  Фільтарція чисел від стрічок
masiv2 = []
def del_str (x):
    for i in range (len(x)):
        try:
            a = int(x[i])
        except ValueError:
            pass
        else:
            masiv2.append(x[i])
    return masiv2

#  створення унікального масиву та його сума
def unic_mas(b):
    c= []  # Масив з інікальними числами
    for i in range (len(b)):
        if int(b[i]) in c: # Читається наявність елемента в масиві с
            continue

        for j in range (len(b)):
           if b[j] == b[i]:
                c.append(int(b[i])) #  перетворюємо значення елемента зі str в int
                break
    print("Масив з унікальних чиисел =%s "%sorted(c)) # відсортований масив по зростанню
    print("Сума унікальних чиисел = %s "  %sum(c))

del_str(masiv)
unic_mas(masiv2)



