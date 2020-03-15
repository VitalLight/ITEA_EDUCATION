""""
Ввести десяткове число і перетроврити його в шістнадцяткове.
"""
try:
    b = int(input(" Enter a number:   "))
except ValueError:
    print("Введене не числове значення")
    exit()
f = 0
# my first function
def transformation (a):
    d = pow(a,3)
    c = hex(a)
    f = pow (a,7)

    print(" Transformation chart {}".format (c))
    print (" Evalue chart **3 {}".format (d))
    return d, c, f

print(transformation (b))  # потрібно вписувати назву змінної яку вводимо
print("f = ".format (f)) #   оце не виводиться? Як вивести його сюди

