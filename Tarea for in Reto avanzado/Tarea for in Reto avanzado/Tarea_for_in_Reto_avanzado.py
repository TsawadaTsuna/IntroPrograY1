#Programa relizado por Kevin Contreras A01635597
print("Programa que imprime el triangulo de pascal hasta un nivel determinado")
lim = int(input("Ingresa el nivel hasta el cual imprimir la secuencia: "))
c=0

#Ciclo desde una hasta el limite para imprimir
for i in range(1,lim+1):
    print((lim-i)*"  ", end ="")
    c = i
    #Ciclo que controla la impresion de la parte izquierda del triangulo
    for j in range(i,0,-1):
        print(c, end="  ")
        c-=1
       
    #Ciclo que controla la impresion de la parte derecha del triangulo
    for co in range(2,i+1):
        print(co, end="  ")
        
    
    print("\n")
        