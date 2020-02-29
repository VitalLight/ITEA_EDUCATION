a = input ('enter numb_ ')
try:
    aK = int(a)
except ValueError:
    print("Couldn't convert inputs to numbers")
else:
    print("Success")
