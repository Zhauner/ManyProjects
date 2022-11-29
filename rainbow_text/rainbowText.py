import colorama as c
from random import randint
from colors import colors

c.init()
lister = []

def rainbow_text(text):
    for x in text:
        lister.append(colors[randint(1, 7)])
        lister.append(x)

    print(''.join(lister))
    return ''