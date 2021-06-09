import math
print("Programa para cañcular ecuaciones cuadraticas")
#Entrada
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
#Proceso y salida
if a == 0:
    if b== 0:
        print("no es una ecuacion")
    else:
        print("a= 0")
        print(f"el resulatdo es: {-c/b}")
elif b**2-4*a*c<0:
    print("imaginario")
elif b**2-4*a*c>0:
    x1 = (-b/2*a)+(math.sqrt(b**2-4*a*c) / (2*a))
    x2 = (-b/2*a)-(math.sqrt(b**2-4*a*c) / (2*a))
    print("real")
    print(f"el resulatado es: {x1} y {x2}")
else:
    print("raiz 0")
    print(f"El resultado es: {-b/2*a}")