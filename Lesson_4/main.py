a = int(input ('enter numb_1 '))
try:
    aK = int(a)
except ValueError:
    print("Couldn't convert inputs to numbers")

if a%2==0:
    print("You enter Good")
else:
    print("You enter wrong")

# Finish