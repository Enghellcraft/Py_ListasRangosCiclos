n = int(input(f"Ingrese el numero de impares que quiere sumar: "))
suma=0
for i in range(n*2):
    if (i%2==1):
        suma += i
        print(f"{suma}")
print(f"La suma de los {n}eros numeros impares es: {suma}")
