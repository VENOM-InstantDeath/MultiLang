# AUTHOR: Darth Venom
# CREATED: 17/3/2021
#
# ABOUT: Programa que genera sumas aleatorias
#        dentro de un intervalo dado.
#
# DEPENDS ON: color.py

import random
from color import *

I = int(input("Range1: "))
II = int(input("Range2: "))

a = 0
for i in range(10):
    s = [random.randint(I,II), random.randint(I,II)]
    print(f"{s[0]} + {s[1]}")
    r = input("answer: ")
    if int(r) == s[0] + s[1]:
        a += 1
        print(f"\033[1A\033[12C{green}true{nm}")

print(f"\n{a}/10")
