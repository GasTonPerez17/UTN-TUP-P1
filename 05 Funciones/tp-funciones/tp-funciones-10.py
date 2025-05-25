#funcion
def calcular_promedio(a, b, c):
    calculo_promedio= (a + b + c) / 3
    return calculo_promedio
    





#principal
num1_str= input("ingrese el primer numero: ")
num1=float(num1_str) 
num2_str= input("ingrese el segundo numero: ")
num2= float(num2_str)
num3_str= input("ingrese el tercer numero: ")
num3= float(num3_str)
promedio=calcular_promedio(num1, num2, num3)
print (f"el promedio de los tres numeros es {promedio}")




