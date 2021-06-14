# AUTHOR: Darth Venom
# CREATED: 02/06/2021
#
# ABOUT: División entre dos números
#
# DEPENDS ON: ---

import re

def isfloat(n):
    return re.match("^[-+]?[0-9]+\.[0-9]+$", n)

def isint(n):
    return re.match("^[-+]?[0-9]+$", n)

def conv(n):
    if isfloat(n) and n.endswith('.0'): return int(n[:-2])
    if isfloat(n): return float(n)
    if isint(n): return int(n)


if __name__ == "__main__":
    N = input("Introduce numerador: ")
    D = input("Introduce denominador: ")
    
    for i in (N,D):
        if not (isfloat(i) or isint(i)):
            exit(1)
    print(conv(str(conv(N) / conv(D))))
