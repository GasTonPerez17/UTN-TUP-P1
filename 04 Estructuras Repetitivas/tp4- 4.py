total = 0 
print("Ingresa los numeros enteros que quiere sumar. Para finalizar, ingrese 0.")

while True:
    numero = int(input("Ingresa un número: "))
    if numero == 0:  
        break
    total = numero+total

print(f"El total es: {total}")

