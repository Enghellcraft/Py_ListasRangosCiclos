cant = int(input("Indique la cantidad de palabras: "))
lista = []
for i in range(0, cant):
    palabra = input(f"Escriba la {i+1}° palabra: ")
    lista.append(palabra)
print(lista)