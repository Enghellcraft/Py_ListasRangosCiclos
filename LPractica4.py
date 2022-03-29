cant = int(input("Indique la cantidad de palabras: "))
lista = []
for i in range(0, cant):
    palabra = input(f"Escriba la {i+1}° palabra: ")
    lista.append(palabra)
print(lista)
buscada = input("Ingrese la palabra a borrar:")
buscada = buscada.lower()
for i in range(len(lista)-1,-1,-1):
    if lista[i] == buscada:
        del lista[i]
print(lista)