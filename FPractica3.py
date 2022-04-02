n = int(input(f"Ingrese el numero para factorial: "))
factorial = 1
for i in range (1,n+1):
    factorial = (factorial*i)
print (f"El factorial de {n} es: {factorial}")