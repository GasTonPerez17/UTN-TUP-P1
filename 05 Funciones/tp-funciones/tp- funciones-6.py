#funcion

def tabla_multiplicar(numero):
   for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    


#principal
numero_str= input ("ingrese un numero: ")
numero= float (numero_str)
multiplicar=tabla_multiplicar(numero)




