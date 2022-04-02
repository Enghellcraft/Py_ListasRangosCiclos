ntop = int(input("Ingrese un limite superior: "))
nbot = int(input("Ingrese un limite inferior: "))
i = 1
lista = []
num = int(input(f"Ingrese el {i}° numero:"))
i += 1
while (num > nbot) and (num < ntop):
    lista.append(num)
    num = int(input(f"Ingrese el {i}° numero:"))
    i += 1
print(f"Los numeros ingresados son: {lista}")