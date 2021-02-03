#Ejercicio 1 laboratorio 2
import math
print("Programa que calcula el area de un prisma rectangular")
#entradas
L = float(input("Ingrese el valor de la bese del triangulo:"))
H = float(input("Ingrese el valor de la bese de la altura del cuerpo:"))
#procesos
Ht = math.sqrt(L**2-(L/2)**2)
At = (L*Ht)/2
Ac = L*H
#salida
print(f"El area del prisma rectangular con base del triangulo {L} y de altura {H} es: {At*2+Ac*3} unidades cuadradas")