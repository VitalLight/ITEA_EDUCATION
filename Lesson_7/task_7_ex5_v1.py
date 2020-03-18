""""
У введеному реченні змінити регістр всіх букв. Наприклад:
рядок “I`m eaTinG BaNaNa.” має бути конвертований у “i`M EAtINg bAnAnA.”
"""
while True:
    s = input ("Введіть вираз з ВЕЛИКИХ Та малих букв ")
# s = "I`m eaTinG BaNaNa"
    print(s.swapcase())
