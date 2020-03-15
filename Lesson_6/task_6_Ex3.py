""""
Розробити алгоритм бінарного пощуку числа у відсортованеому масиві
"""
import random
try:
    n = int(input(" Введіть кількість елементів у масиві >0:   "))
    while n<=0:
        n= int(input(" Введіть Введіть число більше від нуля:   "))
except ValueError:
     print("Введене не числове значення")
     exit()
#  створенян випадковго масиву чисел
sort_masiv = []
rand_masiv = []
i = 0
while i<n:
    rand_masiv.append(random.randrange(n*3))
    i+=1
    sort_masiv = sorted(rand_masiv)
number = int(input(" Вгадай число у випадковому масві чисел від 0 до %s: "%(n*3)))

def number_find (sort_masiv, number):
#  max = len(sort_masiv)-1, щоб уникнути помилок та визначити вхідний(перший) middle
    max = len(sort_masiv)-1
    min = 0
    middle = int(max //2)
#  max + 1  щоб охопити всі елементи по індексах(в компенсацію верхнього (першого) вхідного max)
    for min in range(max+1):
        if sort_masiv[middle] != number and sort_masiv[middle] >= number:
            max = middle-1
        elif sort_masiv[middle] != number and sort_masiv[middle] <= number:
            min = middle+1
        middle = int((min + max) // 2)
    if sort_masiv[middle] == number and (max >= min or min >= max):
        print(" Число %s НАЯВНЕ у випадковому масиві чисел" % number)
    else:
        print(" Число %s відсутнє у випадковому масиві чисел" % number)
    return number

print("Відсортований масив = %s" % sort_masiv)
#  функція шукає вказане число
number_find (sort_masiv, number)





