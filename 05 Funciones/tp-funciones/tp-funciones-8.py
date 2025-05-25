#funcion
import math
def calcular_imc(peso, altura):
     imc = peso / (altura ** 2)
     return imc
    


#principal
peso_str= input ("Ingrese su peso en kg: ")
peso= float(peso_str)
altura_str= input("Ingrese su altura en metros: ")
altura= float(altura_str)
imc=calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")




