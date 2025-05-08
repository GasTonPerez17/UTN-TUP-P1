cant_num = 6  # cambiar a 100 

suma_total = 0

for i in range(cant_num):
    while True:
        try:
            numero = int(input(f"Ingrese el número entero #{i + 1}: "))
            suma_total += numero
            break  
        except ValueError:
            print("Por favor, ingrese un número válido:")
media= suma_total / cant_num 

print("\n--- Resultado ---")
print(f"La media es {media}")