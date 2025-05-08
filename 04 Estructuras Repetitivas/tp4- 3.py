v1 = int(input("Ingresa el primer valor entero: "))
v2 = int(input("Ingresa el segundo valor entero: "))
if v1 < v2:
    inicio = v1 + 1
    fin = v2
else:
    inicio = v2 + 1
    fin = v1
suma = 0
for numero in range(inicio, fin):
    suma = numero+1
suma = sum(range(inicio, fin))

print(f"La suma de los números entre {v1} y {v2}, excluyendo los mismos34, es: {suma}")
