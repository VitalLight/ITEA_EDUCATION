"""
На вхід отримати такі значення: name. mob_phone, email.
На екран вивести наступні речення: "Привіт мене звати <name>.
Мій мобільний <mob_phone>, електронна адреса <email>".
"""

print("\n ВВедіть дані")
name = input("\n Своє імя:  ")
mob_phone = input(" Свій номер мобільного телефону:  ")
email = input(" Свою електронну скриньку:  ")

print("\n Привіт, мене звати - {},\n мій мобільний - {},\n електронна адреса {}.".format(name, mob_phone, email))