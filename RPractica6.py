n1 = int(input("Ingrese un primero numero: "))
n2 = int(input("Ingrese un segundo numero: "))
if n1 % 2 != 0:
    n1 += 1
if n2 % 2 == 0:
    n2 += 1
print(f"La lista es: {list(range(n1, n2, 2))}")