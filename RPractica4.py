n1 = int(input("Ingrese un primero numero: "))
n2 = int(input("Ingrese un segundo numero: "))
print(f"La lista al derecho es : {list(range(n1, n2+1))}")
print(f"La lista al reverso es: {list(range(n2, n1-1, -1))}")