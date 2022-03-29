from tkinter import N


n1 = int(input("Ingrese un primero numero: "))
n2 = int(input("Ingrese un segundo numero: "))
pri = 0
ult = 0
if n1 < n2:
    pri = n1
    ult = n2
else:
    pri = n2
    ult = n1
print(f"Los numeros intermedios son: {list(range(pri+1, ult))}")