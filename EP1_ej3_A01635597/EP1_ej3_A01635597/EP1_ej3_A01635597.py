#Realizado por Kevin Contreras A01635597
print("Programa que realiza una sumatoria hasta que se ingrese un numero mayor a un numero base")
base = int(input("Ingrese el numero que servira como base:"))
i = 0
sum = 0 
#Ciclo que controla la entrada de datos hasta que se de un numero mayor a la base
while i<base:
    #Generacion de la sumatoria e introduccion de dato (condicion de quiebre)
    sum+=i
    i = int(input("Ingrese un numero a sumar:"))
print(f"El resultado de la sumatoria es {sum}")