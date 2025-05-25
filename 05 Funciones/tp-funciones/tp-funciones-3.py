#funcion
def informacion_personal (nombre, apellido, edad, residencia):
    print (f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
    


#principal
nombre= input ("ingrese su nombre: ")
apellido= input ("ingrese su apellido: ")
edad= input ("ingrese su edad: ")
residencia= input ("ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)



