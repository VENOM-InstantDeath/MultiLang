import random

I = int(input("Range1: "))
II = int(input("Range2: "))

a = 0
for i in range(10):
    s = [random.randint(I,II), random.randint(I,II)]
    print(f"{s[0]} + {s[1]}")
    r = input("answer: ")
    if int(r) == s[0] + s[1]: a += 1

print(f"\n{a}/10")
