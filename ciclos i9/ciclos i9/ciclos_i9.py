#Programa realizado por Kevin Contreras A01635597
print("Programa que verifica si un numero es perfecto")
n = int(input("Ingrese un numero entero para revisar si es perfecto:"))
i = 1
sum =0
#ciclo para encontrar los divisores y samarlos
while i<n:
    if n%i==0:
        sum+=i
    i+=1
#Condicional para verificar si es numero perfecto
if sum==n:
    print("Numero perfecto")
else:
    print("No es numero perfecto")