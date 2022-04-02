lista = []
num1 = int(input(f"Ingrese el 1° numero: "))
lista.append(num1)
num2 = int(input(f"Ingrese el 2° numero: "))
while num2 > num1:
    print("El segundo numero debe ser menor al primero")
    num2 = int(input(f"Reingrese el 2° numero: "))
else:
    lista.append(num2)
print(f"{lista}")