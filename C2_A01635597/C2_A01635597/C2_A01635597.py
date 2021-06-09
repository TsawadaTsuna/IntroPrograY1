#Programa realizado por Kevin Contreras
print("Programa que indica si se ingreso una seri de numeros en orden decreciente")
#Entradas
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
n3 = int(input("Ingrese otro numero: "))
#Procesos y salidas
if n1 > n2 and n2 > n3:
    print("Felicidades, tus números fueron ingresados en orden decreciente")
else:
    print("No fueron ingresados en orden decreciente")
#Reforce conocimientos de operadores relacionales en estructuras condicionales