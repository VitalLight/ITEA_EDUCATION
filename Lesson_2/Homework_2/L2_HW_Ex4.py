"""
Визначити століття за введеним роком
"""

try:
    year = int(input ("Введіть рік:   "))

except ValueError:
    print("\n Рік введено у не числовому форматі")

if year%100 >= 1:
    stolitia = (year//100) + 1
else:
    stolitia = (year // 100) - 1

print("\n Введений рік знаходиться в {} -му столітті.".format(stolitia))