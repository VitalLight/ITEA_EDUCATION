"""
Корисувач вказує дві назви файлів (у файлах якась текстова інформація).
Після цього вказує, що знаходить спільне в даних файлах: Речення, слова, словосполучення.
Вивести на екран кількість спільних елементів, які запросив користувач.
"""
import re

find_object = input("Вкажіть, що потрбіно спільного віднайти у двох файлах?   ")

# функція рахує кількіть вказаних символів у файлі
def find_(o, f):
    a = len(re.findall(o, f))
    print("Вказане слово --- %s --- згадується  %s разів у файлі" % (find_object, a))
    return a

print("\nПерший введениий файл")
file1 = open('d:\\Python_ITed\Lesson_8\\Homework_L8\\packeg_for_working with file\\ex_2_.txt', 'r')
test1 = file1.read()
find_(find_object, test1)
# print("Вказане слово --- %s --- згадується  %s разів у файлі " % (find_object))
file1.close()

print("\nДругий введениий файл")
with open('d:\\Python_ITed\\Lesson_8\\Homework_L8\\packeg_for_working with file\\kind_wine.txt', 'r') as file2:
    test2 = file2.read()

find_(find_object, test2)







