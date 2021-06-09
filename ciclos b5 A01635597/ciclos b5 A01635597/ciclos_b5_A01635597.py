#Programa realizado por Kevin Contreras
print("Programa que despliega la tabla de multiplicar del numero deseado")
n = int(input("Tabla a desplegar (numero entero): "))
i = 1
#Ciclo que despliega la tabla
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i+=1
