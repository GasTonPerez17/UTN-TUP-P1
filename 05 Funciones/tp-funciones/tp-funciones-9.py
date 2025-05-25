#funcion
def celsius_a_fahrenheit(celsius):
    fahrenheit=(temperatura * 9/5) + 32
    return fahrenheit



#principal
temperatura_str= input ("ingresar la temperatura en Celsius: ")
temperatura=float(temperatura_str)
fahrenheit = celsius_a_fahrenheit(temperatura)
print(f"{temperatura} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")





