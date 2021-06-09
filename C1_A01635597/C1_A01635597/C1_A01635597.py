#Realizado por Kevin Contreras
import math
print("Programa para calcular el volumen de un tronco de un cono")
#Entradas
abma = float(input("Area de la base mayor (Numero positivo):"))
abm = float(input("Area de la base menor (Numero positivo):"))
h = float(input("Altura (Numero positivo):"))
#Procesos y salida
if abm<=0 or abma<=0 or h<=0:
    print("Datos invalidos")
else:
    print(f"El volumen del tronco de cono es: {(h/3*(abm + abma + math.sqrt(abm + abma))):.2f}")
#Reforze sobre relacionales en condicionales