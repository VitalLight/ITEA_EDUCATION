"""
Корисувач вказує дві назви файлів (у файлах якась текстова інформація).
Після цього вказує, що знаходить спільне в даних файлах: Речення, слова, словосполучення.
Вивести на екран кількість спільних елементів, які запросив користувач.
"""
import re

def enter_way_file ():
    ways = []
    index = 0
    while True:
        way = input("Введіть шлях до файлу:  ")
        ways.append(way)
        index += 1
        add = input("Ввести ще шлях натисніть +")
        if add == "+":
            continue
        else:
            break
    return ways, index
mas_ways, mas_index = enter_way_file ()



#  Запуск функц2ії введення шляхів до файлів порівняння
enter_way_file()

find_object = input("Вкажіть, що потрбіно спільного віднайти у вказаних файлах?   ")

# функція рахує кількіть вказаних символів у файлі
def find_(o, f,i):
    a = len(re.findall(o, f))
    print("Вказане слово --- %s --- згадується  %s разів у файлі" % (find_object, a))
    return a


def open_f (w, o, i):
    for n in range(len(mas_ways)):
        with open(w, 'r') as f:
            t = f.read()
            find_(o, t,i)

open_f (mas_ways, find_object, mas_index)


#
# while i<=index:
#     open_f(ways)

