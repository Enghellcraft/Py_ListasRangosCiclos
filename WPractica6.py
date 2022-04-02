ntop = int(input("Ingrese un valor tope de suma: "))
suma, i = 0, 1
while suma <= ntop:
    num = int(input(f"Ingrese el {i}° numero a sumar: "))
    suma += num
    i += 1
if suma > num:
    suma -= num
    print(f"La suma total es: {suma}, se sumo {i-2} veces, con limite de {ntop}")
else:
    print(f"La suma total es: {suma}, se sumo {i-2} veces, con limite de {ntop}")