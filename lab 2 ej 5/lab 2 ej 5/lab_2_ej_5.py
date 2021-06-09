import math
print("Programa para calcular areas de triangulos en base a 2 lados y en algunlo entre si")
#Entradas
l1 = float(input("Lado 1:"))
l2 = float(input("Lado 2:"))
a = float(input("Angulo:"))
#Procesos y salida
r = a*math.pi/180
print(f"El area del triangulo  con lado 1 {l1}, lado 2 {l2} y angulo {a} es: {1/2*l1*l2*math.sin(r)} unidades cuadradas")