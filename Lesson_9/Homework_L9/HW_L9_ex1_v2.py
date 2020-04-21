""""
Написати програму, яка конвертуватиме звичайне число у римське.
 Тобто “3” має бути конвертовано у “ІІІ”, “4” - “IV”, “58” - “LVIII”. Ось таблиця, за якою треба конвертувати числа.

"""
import roman
while True:
    try:
        a = int(input("Enter your number\t"))
        print(roman.toRoman(a))

    except ValueError:
        print("Enter number! not Word")
        exit()




