#funcion

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b == 0:
        division = None  
    else:
        division = a / b
    return (suma, resta, multiplicacion, division)

#principal
num1_str = input("Ingrese el primer número: ")
num2_str = input("Ingrese el segundo número: ")
num1 = float(num1_str)
num2 = float(num2_str)

resultados = operaciones_basicas(num1, num2)
suma, resta, multiplicacion, division = resultados  

print(f"Resultados de las operaciones son:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
if division is not None:
 print(f"División: {division}")
else:
 print("División: No se puede dividir por cero.")





