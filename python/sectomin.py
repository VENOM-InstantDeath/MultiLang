t = input("Input time in seconds: ")
if not t.isdigit: print("No se ha ingresado un número"); exit(1)
t = int(t)
print(f"{int(t/60)}:{t%60}")
