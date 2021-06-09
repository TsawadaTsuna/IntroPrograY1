#Programa realizado por Kevin Contreras A01635597
print("Programa que imprime los numeros del 100 al 200 que sean divisibles entre 5 o 6 pero no ambos")

c = 0
#Ciclo for del 100 al 200
for i in range(100,201):
   #Condicion de impresion
   if i%5==0 and i%6!=0 or i%6==0 and i%5!=0:
        print(i, end=" ")
        c+=1
   #Condicion de salto de linea
   if c == 10:
        print("\n")
        c=0