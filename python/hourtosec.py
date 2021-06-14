# AUTHOR: Darth Venom
# CREATED: 02/06/2021
#
# ABOUT: Convierte horas a segundos.
#
# DEPENDS ON: ---

from re import match

def hourtosec(x):
    if not match('[0-9]+:[0-9]+', x):
        return "if"
    l = x.split(':')
    for i in l:
        if not i.isdigit():
            return "NaN"
    l = [int(i) for i in l]
    if l[1] > 60:
        r = l[1]//60
        l[1] = l[1]-60*r
        l[0] += r
    return (l[0]*3600)+(l[1]*60)


if __name__ == "__main__":
    print("Example: 16:24")
    x = input("Input time in hours: ")
    x = hourtosec(x)
    if x == "if":
        print("Incorrect format.")
        exit(1)
    elif x == "NaN":
        print("Not a Number Error")
        exit(1)
    else:
        print(x)
