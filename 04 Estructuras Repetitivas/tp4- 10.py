numero = int(input("Ingrese un número entero: "))
num_absoluto = abs(numero)

num_invertido = 0

while num_absoluto > 0:
    digito = num_absoluto % 10  
    num_invertido = num_invertido * 10 + digito  
    num_absoluto //= 10  
if numero < 0:
    numero_invertido = -num_invertido

print(f"El número invertido es: {num_invertido}")