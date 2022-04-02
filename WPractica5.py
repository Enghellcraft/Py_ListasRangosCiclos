i = 1
num = int(input(f"Ingrese el {i}° numero: "))
i += 1
op = 1
suma = num
while op==1:
    numu = int(input(f"Ingrese el {i}° numero: "))
    while numu < 0:
        print(f"El numnero ingresado no es positivo")
        numu = int(input(f"Ingrese el {i}° numero: "))
    else:
        suma += numu
        i += 1
    op = int(input("Si desea finalizar presione 0, sino presione 1: "))
print(f"La suma total es: {suma}")
