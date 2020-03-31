import random

class Country:
    def __init__(self, nasel, nazva, squere):
        self.nasel = nasel
        self.nazva = nazva
        self.squere = squere
    def calc_pop(self,nasel):
        diff_nasel = nasel + (((random.random(2)-1) * ((random.random()-1))) * random.randrange(nasel))
        return diff_nasel
u = Country(48, 'Krakosia', 54)

print(u.nazva)
print(u.nasel)
print(u.squere)

print(u.calc_pop(u.nasel))


