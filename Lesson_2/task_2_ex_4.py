""""
Спитати  про вік користувача, імя та його хобі. Результати введених даних вивести на екран.
"""
print("\n Давай знайомитись! Напиши відповіді на запитання у тому ж рядку")
name = input("\n Як тебе звати?:  ")
old = input(" Скільки тобі років?:  ")
hobby = input(" Яке твоє хобі?:  ")

if "" <= name <= ""*10 or "" <= old <= ""*10 or "" <= hobby <= ""*10:
    print("Я не буду з тобою знайомитись, бо ти ввів не усі дані")
    exit()

print("\n - Мене звати {}, мені {} років. Моє улюблене хобі {}".format(name, old, hobby))




