#tp3- ejercicio 1- mayor de edad
edad = int (input ("Ingrese su edad: "))
if edad >= 18:
    print ("Es mayor de edad.")
else:
    print ("Es menor de edad.")
    
    
  #tp3- ejercicio 2- nota
nota= int (input ("Ingrese su nota: "))
if nota >= 6: 
    print ("APROBADO")
else:
    print ("DESAPROBADO")
    
    
      # tp3- ejercicio 3- numero par
while True:
    try:
        numero= int(input ("Ingrese un numero entero: "))
        resto= numero % 2 
        if resto == 0:
            print("Ha ingresado un número par.")
        elif resto!=0:
            print("Por favor, ingrese un número par.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        
        # tp3- ejercicio 4- categoria edad
while True:
    try:
        edad= int(input ("Ingrese su edad: "))
        if edad<12:
            print("NIÑO.")
        elif edad >=12 and edad < 18:
            print("ADOLESCENTE.")
        elif edad >= 18 and edad < 30:
            print ("ADULTO JOVEN.")
        elif edad >= 30:
            print ("ADULTO.")
    except ValueError:
        print("Por favor, ingrese una edad válida.")
        
        #tp3- ejercicio 5- contraseña 
contraseña= str(input("Ingrese su contraseña: "))
longitud= len(contraseña)
if longitud >= 8 and longitud <=14:
    print ("Ha ingresado una contraseña correcta.")
else: 
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
    
    
    # tp3- ejercicio 6- moda, mediana y media
import random 
from statistics import mode, median, mean
import statistics 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
media = statistics.mean(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
moda = statistics.mode (numeros_aleatorios)
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

if media > mediana and media > moda:
    print("Hay un sesgo positivo.")
elif media < mediana and media < moda:
    print("Hay un sesgo negativo.")
else:
    print("No hay un sesgo.")

# tp3- ejercicio 7- vocal
  
def termina_vocal(texto):
  vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
  if texto and texto[-1] in vocales:
    nuevo_texto = texto + "!"
  else:
    nuevo_texto= texto
  print(nuevo_texto)

entrada= input("Ingrese una frase o palabra: ")

termina_vocal(entrada)
        
        
        # tp3- ejercicio 8- nombre 1,2,3
nombre= str (input ("Ingrese su nombre: "))

def menu():
    print("Seleccione una opcion:")
    print("1")
    print("2")
    print("3")

def main():
    while True:
        menu()
        opcion = input("Ingresa la opcion elegida (1, 2 o 3): ")

        if opcion == '1':
            print("Opción Uno elegida:")
            nombreMayuscula= nombre.upper()
            print (nombreMayuscula) 
            break 
        elif opcion == '2':
            print("Opción Dos elegida:")
            nombreMinuscula= nombre.lower()
            print (nombreMinuscula)
            break
        elif opcion == '3':
            print("Opción Tres elegida:")
            primeraMayus= nombre.title()
            print (primeraMayus)
            break  
        else:
            print("Opción inválida. Por favor, ingrese una opcion correcta.")
if __name__ == "__main__":
    main()



#tp3- ejercicio 9- terremoto
magnitud= int (input ("Ingrese la magnitud del terremoto: "))

def main():
    while True:
        

        if magnitud < 3:
            print("Muy leve (imperceptible).")
            break 
        elif magnitud >= 3 and magnitud < 4:
            print("Leve (ligeramente perceptible)." )
            break
        elif magnitud >= 4 and magnitud < 5:
            print("Moderado (sentido por personas, pero generalmente no causa daños).")
            break  
        elif magnitud >= 5 and magnitud < 6:
            print ("Fuerte (puede causar daños en estructuras débiles).")
            break
        elif magnitud >= 6 and magnitud < 7:
            print ("Muy Fuerte (puede causar daños significativos).")
            break
        elif magnitud >= 7:
            print ("Extremo (puede causar graves daños a gran escala).")
            break 
        else:
            print("Opción inválida. Por favor, ingrese una opcion correcta.")
if __name__ == "__main__":
    main()


#tp3- ejercicio 10- hemisferio

def periodoAño(hemisferio, mes, dia):
    mes = mes.lower()

    if (mes == 'diciembre' and dia >= 21) or mes == 'enero' or mes == 'febrero' or (mes == 'marzo' and dia <= 20):
        periodo = "Desde el 21 de diciembre hasta el 20 de marzo (incluidos)"
        norte = "Invierno"
        sur = "Verano"
    elif (mes == 'marzo' and dia >= 21) or mes == 'abril' or mes == 'mayo' or (mes == 'junio' and dia <= 20):
        periodo = "Desde el 21 de marzo hasta el 20 de junio (incluidos)"
        norte = "Primavera"
        sur = "Otoño"
    elif (mes == 'junio' and dia >= 21) or mes == 'julio' or mes == 'agosto' or (mes == 'septiembre' and dia <= 20):
        periodo = "Desde el 21 de junio hasta el 20 de septiembre (incluidos)"
        norte = "Verano"
        sur = "Invierno"
    elif (mes == 'septiembre' and dia >= 21) or mes == 'octubre' or mes == 'noviembre' or (mes == 'diciembre' and dia <= 20):
        periodo = "Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)"
        norte = "Otoño"
        sur = "Primavera"
    else:
        return "Fecha inválida", "Fecha inválida"

    if hemisferio == 'N':
        return periodo, norte
    elif hemisferio == 'S':
        return periodo, sur
    else:
        return "Hemisferio inválido", "Hemisferio inválido"


def main():
    
    hemisferio = input("En qué hemisferio te encuentras? (N/S): ").upper()
    mes = input("Qué mes del año es?: ")
    dia_str = input("Qué día del mes es?: ")

    try:
        dia = int(dia_str)
        resultado = periodoAño(hemisferio, mes, dia)

        if resultado[0] == "Fecha inválida.":
            print("La fecha ingresada no es válida.")
        elif resultado[0] == "Hemisferio inválido":
            print("El hemisferio ingresado no es válido.")
        else:
            periodo, estacion = resultado
            print(f"Usted se encuentra en: {estacion}")

    except ValueError:
        print("El día ingresado no es válido.")

if __name__ == "__main__":
    main()
    
    
    
