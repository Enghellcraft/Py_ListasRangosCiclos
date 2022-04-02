n = int(input(f"Ingrese la cantidad de numeros a listar: "))
lista = []
i = 0
while i < n:
    num = int(input(f"Ingrese el {i+1}° numero: "))
    if num > 0 :
        lista.append(num)
        i += 1
    else:
        print ("No es un numero positivo, reingrese el numero.")
print(f"{lista}")