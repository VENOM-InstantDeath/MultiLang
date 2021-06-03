# AUTHOR: Darth Venom
# CREATED: 16/3/2021
#
# ABOUT: Convierte segundos a minutos.
#
# DEPENDS ON: ---

t = input("Input time in seconds: ")
if not t.isdigit:
    print("No se ha ingresado un número")
    exit(1)
t = int(t)
print(f"{int(t/60)}:{t%60}")
