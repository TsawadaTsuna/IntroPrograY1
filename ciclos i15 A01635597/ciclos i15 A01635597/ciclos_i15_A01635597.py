import random
#Programa realizado por Kevin Contreras A01635597
print("Hola y bienvenido. Tiene 7 intentos para adivinar un numero aleatorio entre 1 y 100 y ganar")
num = random.randint(1,100)
i = 1
#Ciclo para verificar los intentos

while i<=7:
    n = int(input("Ingrese un numero. Trate de adivinar:"))
    #Condicional para marcar la comparacion entre el numero dado y el generado
    if n == num:
        print("Felicidades usted ha ganado.")
        i = 8
    elif n < num:
        print("Error, el numero que ingreso es menor que el numero generado")
        print(f"Le quedan {(i-7)*-1} intentos")
        i+=1
    else:
        print("Error, el numero que ingreso es mayor que el numero generado")
        print(f"Le quedan {(i-7)*-1} intentos")
        i+=1
print("Fin del juego. Gracias por jugar")