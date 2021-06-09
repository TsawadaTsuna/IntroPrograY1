#Realizado por Kevin Contreras A01635597
print("Programa que muestra la conjetura de collatz desde un numero dado")
n = int(input("Desde donde iniciar (numero entero):"))
#Inicio de ciclo que terminara cuando se llege a 1
while n!=1:
    print(n)
    #Condicional para proceder a operaciones
    if n%2 == 0:
        n=n//2
    else:
        n=3*n+1
print(n)