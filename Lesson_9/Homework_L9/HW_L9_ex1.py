""""
Написати програму, яка конвертуватиме звичайне число у римське.
 Тобто “3” має бути конвертовано у “ІІІ”, “4” - “IV”, “58” - “LVIII”. Ось таблиця, за якою треба конвертувати числа.

"""
digit_konvert = {1:'I', 5: 'V', 10: 'X', 100: 'C', 500: 'D', 1000: 'M'}
digit = int(input (f"Введіть арабське число {set(digit_konvert)} для його ковертації в Римське   "))  #   множина вибирає з переліку ключів
print(f" Для арабського числа {digit }  відповідає символ ---{digit_konvert[digit]}")