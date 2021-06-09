#Realizado por Kevin Contreras A01635597
print("Programa que evalua una funcion seccionada")
#Entradas
num = float(input("Ingrese un numero cualquiera:"))
#Procesos y salidas
if num <= 1:
    print("Tu numero esta en la seccion menor o igual a 1")
    print(f"El resultado de la funcion evaluada en {num} es: 1")
elif num > 1 and num <= 3:
    print("Tu numero esta en la seccion mayor a 1 e igual o menor a 3")
    print(f"El resultado de la funcion evaluada en {num} es: {num}")
elif num > 3 and num <= 6:
    print("Tu numero esta en la seccion mayor a 3 e igual o menor a 6")
    print(f"El resultado de la funcion evaluada en {num} es: {-num+6}")
else:
    print("Tu numero esta en la seccion mayor a 6")
    print(f"El resultado de la funcion evaluada en {num} es: 0")