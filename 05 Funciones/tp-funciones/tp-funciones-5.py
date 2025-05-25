#funcion
import math
def segundos_a_horas(segundos):
    horas= segundos / 3600
    return horas

#principal
segundos_str= input ("Ingrese la cantidad de segundos: ")
segundos= float (segundos_str)
horas=segundos_a_horas(segundos)
print (f"los segundos ingresados equivalen a {horas} horas")




