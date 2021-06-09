#Realizado por Kevin Conteras
from math import sqrt
print("Programa que calcula si un punto se encuentra dentro o fuera de una circunferencia")
#Entradas
r = float(input("Ingrese el radio de la circunferencia: "))
x1 = float(input("Ingrese la coordenada x del centro de la circunferencia: "))
y1 = float(input("Ingrese la coordenada y del centro de la circunferencia: "))
x2 = float(input("Ingrese la coordenada x del punto a calcular: "))
y2 = float(input("Ingrese la coordenada y del punto a calcular: "))
d = sqrt((x2-x1)**2+(y2-y1)**2)
#Procesos y salida
if d < r:
    print("El punto se encuentra dentro de la circunferencia.")
elif d>r:
    print("El punto se encuentra fuera de la circunferencia.")
else:
    print("El punto se encuentra sobre de la circunferencia.")
#Reforce estructuras condicionales y manejo de operadores relacionales