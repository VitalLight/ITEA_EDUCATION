import json
import random
import re


def word_capcha():
    k = """
    The city in China where the coronavirus pandemic began, Wuhan, has partially re-opened after
more than two months of isolation.
Crowds of passengers were pictured arriving at Wuhan train station on Saturday.
People are being allowed to enter but not leave, according to reports.
Wuhan, the capital of Hubei province, saw more than 50,000 coronavirus cases.
At least 3,000 people in Hubei died from the disease.
But numbers have fallen dramatically, according to  figures.
The state on Saturday reported 54 new cases emerging the previous day - which it said were all imported.
As it battles to control cases coming from abroad, China has announced a temporary ban on all foreign visitors,
even if they have visas or residence permits. It is also limiting Chinese and foreign airlines to one flight per week,
and flights must not be more than 75% full.
    """

with open('d:\\Python_ITed\\Lesson_10\\Homework_L10\\packeg_for_HWL10\\text_capcha.json','r') as f:

    word = json.loads(f.read())

    filt_word = re.findall(r'\w\w\w\w\w', word)
    choice_word = random.choice(filt_word)

    print(choice_word)

word_capcha()