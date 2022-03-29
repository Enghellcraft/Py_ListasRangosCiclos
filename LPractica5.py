cant = int(input("Indique la cantidad de palabras de ambas listas: "))
lista1 = []
for i in range(0, cant):
    palabra = input(f"Escriba la {i+1}° palabra de la primera lista: ")
    lista1.append(palabra)
print(lista1)
lista2 = []
for i in range(0, cant):
    palabra = input(f"Escriba la {i+1}° palabra de la segunda lista: ")
    lista2.append(palabra)
print(lista2)
for i in range(len(lista1)-1, -1, -1):
    for j in range(len(lista2)-1, -1, -1):
        if lista1[i] == lista2[j]:
            del lista1[i]
print(lista1)
print(lista2)