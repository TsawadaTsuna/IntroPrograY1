#Programa realizado por Kevin Contreras A01635597
print("Programa para verificar si una division es exacta")
#Entradas
n1 = int(input("Ingrese el dividendo (entero):"))
n2 = int(input("Ingrese el divisor (entero):"))
#Procesos y salidas
if n2 == 0:
    print("No se puede dividir entre 0")
elif n1%n2 == 0:
    print(f"La divison es exacta. Cociente: {n1/n2}")
else:
    print(f"La division no es exacta. Cociente: {n1//n2}. Residuo: {n1%n2}")
#Reforze mis conocimientos de If