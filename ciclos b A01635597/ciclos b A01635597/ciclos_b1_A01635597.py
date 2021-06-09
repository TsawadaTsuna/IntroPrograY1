#Realizado por Kevin Contreras A01635597
print("Programa que muestra numeros acendentes de 2 en 2 en un intervalo dado")
min = int(input("Desde donde empezar (Numero entero):"))
max = int(input("Hasta donde llegar (Numero entero):"))
#Ciclo que imprime los numero hasta lavarible max y condicion de validacion del intervalo
if min<max:
    while min <= max:
        print(min)
        min+=2
else:
    print("Intervalo invalido")
    
    
