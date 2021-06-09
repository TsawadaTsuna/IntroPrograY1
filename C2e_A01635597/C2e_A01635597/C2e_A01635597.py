#Realizado por Kevin Contreras A01635597
print("Programa para indicar relacion entre 2 numeros")
#Entradas
n1 = int(input("Ingrese un numero (entero):"))
n2 = int(input("Ingrese otro numero (entero):"))
#Procesos y salidas
if n1 == n2:
    print(f"{n1} es igual a {n2}")
elif n1<n2:
    print(f"{n1} es menor que {n2}")
else:
    print(f"{n1} es mayor que {n2}")
#Reforze conocimientos de If