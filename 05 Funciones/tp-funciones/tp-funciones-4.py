#funcion
import math

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

def calcular_perimetro_circulo(radio):
     perimetro = 2 * math.pi * radio
     return perimetro
 


#principal
radio_str= input ("Ingresar radio: ")
radio= float(radio_str)
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo con radio {radio} es: {area}")
print(f"El perímetro del círculo con radio {radio} es: {perimetro}")





