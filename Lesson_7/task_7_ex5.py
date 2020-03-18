""""
У введеному реченні змінити регістр всіх букв. Наприклад:
рядок “I`m eaTinG BaNaNa.” має бути конвертований у “i`M EAtINg bAnAnA.”
"""
s = "I`m eaTinG BaNaNa"
b = []
for i in s:
    if i == i.lower():
        i = i.upper()
        b.append(i)
    else:
        i = i.lower()
        b.append(i)
 print(''.join(b))

