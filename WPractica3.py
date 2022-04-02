lista = []
i = 1
num = int(input(f"Ingrese el {i}° numero: "))
lista.append(num)
i += 1
op = 1
while op==1:
    numu = int(input(f"Ingrese el {i}° numero: "))
    while numu < num:
        print(f"El numnero ingresado no es mayor que {num}")
        numu = int(input(f"Ingrese el {i}° numero: "))
    else:
        lista.append(numu)
        i += 1
    op = int(input("Si desea finalizar presione 0, sino presione 1"))
print(f"{lista}")
