import random
num_secreto = random.randint(0, 9)
print ("Bienvenidos a Adivinando el Numero Secreto!")
print("Adivina que numero estoy pensando entre el 0 y 9")
intentos= 0
acertado= False
while not acertado:
    num_usuario= int (input("Que numero estoy pensando?: "))
    intentos += 1
    
    if num_usuario == num_secreto:
        print("felicitaciones! Adivinaste el número!")
        acertado = True  
    elif num_usuario < num_secreto:
        print("te doy una pista, el numero es mayor") 
    else:
        print("te doy una pista, el numero es menor")

print(f"Lo lograste en {intentos} intentos!")

    