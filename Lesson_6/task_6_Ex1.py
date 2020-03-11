""""
Ввести десяткове число і перетроврити його в шістнадцяткове.
"""
try:
    b = int(input(" Enter a number:   "))
except ValueError:
    print("Введене не числове значення")
    exit()

# my first function
def transformation (a):
    d = a ** 3
    c = hex(a)

    print(" Transformation chart {}".format (c))
    print (" Evalue chart **3 {}".format (d))
    # return d
    return c

print(transformation (b))  # потрібно вписувати назву змінної яку вводимо


