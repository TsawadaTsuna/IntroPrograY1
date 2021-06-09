#Programa relizado por Kevin Contreras A01635597
print("Programa que imprime una piramide de asteriscos hasta un nivel determinado")
lim = int(input("Ingresa el nivel hasta el cual imprimir la secuencia: "))
#Variable para la repeticion de los asteriscos
mult = range(lim)
#Ciclo desde una hasta el limite para imprimir
for i in range(1,lim+1):
   #Multiplicaciones de strings para ordenar los espacios y los asteriscos
   print((lim-i)*" "+((mult+i)*"*")
   #Contador para la repeticion de asteriscos
   