#Programa realizado por Kevin Contreras A01635597
print("Programa que imprime tablas de multiplicar")
#Variable para preguntarle al usuario la tabla a imprimir
tab = int(input("Tabla a imprimir: "))
#Ciclo que imprime la tabla
for i in range(1,11):
    print(f"{tab} x {i} = {i*tab}")