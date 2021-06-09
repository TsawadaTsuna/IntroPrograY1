#Programa realizado por Kevin Contreras A01635597
print("Programa que imprime los de 1 a 120 que son divisibles entre 3 o 4 pero no ambos")
c = 0
for i in range(1,121):
    if i%3==0 and i%4!=0 or i%4==0 and i%3!=0:
        print(i, end=" ")
        c+=1
    if c==10:
        print("\n")
        c=0