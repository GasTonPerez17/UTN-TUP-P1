cantidad_numeros = 10 #cambiar por 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad_numeros):
    while True:
        try:
            numero = int(input(f"Ingrese el número entero #{i + 1}: "))
            break  
        except ValueError:
            print("Por favor, ingrese un número entero válido:")

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\n--- Resultados ---")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")