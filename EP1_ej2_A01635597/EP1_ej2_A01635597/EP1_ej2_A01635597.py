#Reaizado por Kevin Contreras A01635597
print("Programa de apuestas con dados")
ap = float(input("Valor a apostar:"))
print("Muy bien ahora tire los dados")
dado1 = int(input("Ingrese el valor que le dio el primer dado:"))
dado2 = int(input("Ingrese el valor que le dio el segundo dado:"))
#Condicion para la apuesta inicia con una validacion de combinaciones reales de dados
if dado1 < 1 or dado2<1 or dado1>6 or dado2>6:
    print("Datos erroneos")
    #Condicion Para verificr combinaciones faciles y dificiles y poner la apuesta ganada
elif dado1==dado2:
    if dado1+dado2 == 4 or dado1+dado2 == 10:
        print(f"Felicidades usted ha recibido ${ap*7}")
    elif dado1+dado2 == 12 or dado1+dado2 == 2:
        print(f"Usted se mantuvo con ${ap}")
    else:
        print(f"Felicidades usted ha recibido ${ap*9}")
else:
    if dado1+dado2 == 4 or dado1+dado2 == 6 or dado1+dado2 == 8 or dado1+dado2 == 10 or dado1+dado2 == 7:
        print("Usted perdio su apesta.")
    else:
        print(f"Usted se mantuvo con ${ap}")
