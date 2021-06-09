#Programa realizado por Kevin Contreras A01635597
print("Programa que demiestra que de la conjetura de Leibnitz multiplicada por 4 se aceca a pi")
n=0
sum=0
lim=int(input("Ingrese el numero de elementos a sumar:"))
#Inicio de ciclo
while n<=lim:
    sum+= (-1)**n/(2*n+1)
    n+=1
#Resultado
print(f"la sumatoria multiplicada por 4 es: {sum*4}")