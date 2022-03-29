cant = int(input("Indique la cantidad de palabras: "))
lista1 = []
for i in range(0, cant):
    palabra = input(f"Escriba la {i+1}° palabra: ")
    lista1.append(palabra)
print(lista1)
lista2 = []
for i in reversed(lista1):
    lista2.append(i)
print(lista2)
