# AUTHOR: Darth Venom
# CREATED: 02/06/2021
#
# ABOUT: Convierte horas a segundos.
#
# DEPENDS ON: ---

from re import match

print("Example: 16:24")
x = input("Input time in hours: ")
if not match('[0-9]+:[0-9]+', x):
    exit(1)
l = x.split(':')
for i in l:
    if not i.isdigit():
        exit(1)
l = [int(i) for i in l]
if l[1] > 60:
    r = l[1]//60
    l[1] = l[1]-60*r
    l[0] += r

print((l[0]*3600)+(l[1]*60))
