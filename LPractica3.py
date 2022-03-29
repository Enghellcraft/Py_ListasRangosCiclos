cant = int(input("Indique la cantidad de palabras: "))
lista = []
for i in range(0, cant):
    palabra = input(f"Escriba la {i+1}° palabra: ")
    lista.append(palabra)
print(lista)
buscada = input("Ingrese la palabra a buscar:")
buscada = buscada.lower()
cambiada = input("Ingrese la palabra en reemplazo: ")
cambiada = cambiada.lower()
for i in range(len(lista)):
    if lista[i] == buscada:
        lista[i] = cambiada
print(lista)