lista = []
op = 's'
while op == 's':
    num = int(input("Ingrese un numero: "))
    if num%2==0:
        lista.append(num)
    else:
        print("El numero ingresado debe ser par")
    opi = str(input("Si desea continuar agregando numeros, ingrese 's' "))
    op = opi.lower()
print(f"Los numeros ingresados son: {lista}")
