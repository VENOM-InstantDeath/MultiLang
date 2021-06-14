# AUTHOR: Darth Venom
# CREATED: 16/3/2021
#
# ABOUT: Convierte segundos a minutos.
#
# DEPENDS ON: ---

def sectomin(t):
    if not t.isdigit:
        return
    t = int(t)
    return f"{int(t/60)}:{t%60}"

if __name__ == "__main__":
    t = input("Input time in seconds: ")
    response = sectomin(t)
    if response:
        print(response)
    else:
        print("No se ha ingresado un número")
        exit(1)
