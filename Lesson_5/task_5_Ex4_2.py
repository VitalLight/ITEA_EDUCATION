""""
                     Написати програму, яка перевіряє, чи введене число є паліндромом
"""
"""
використано метод list (reversed ())
"""

arr = []  # створюємо пустий масив(ящик для завантаження)
#  введення кількості елементів масиву
try:
    n= int (input ("Введіть кількіть елементів в масиві:    "))
except ValueError:
    print("ВВедене значення елементів в масиві не є число. Запустіть програму і введіть число ")
    exit()

"цикл для заповнення масиву елементами в кількість n"

for i in range(n):
    value =   input ("Заповніть %s елемент масиву:   " %(i+1))  # заповнення елементів масиву
    arr.append(value)  # до масиву вводяться елементи
print ("\nВаш введений масив %s" %arr )

for i in range (n):

    a= list(arr[i])
    b= list (reversed (arr[i]))
    if a==b:
        print (" Число  %s ПОЛІНДРОМ" %arr[i])