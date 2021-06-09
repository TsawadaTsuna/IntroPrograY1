import math
print("Programa para cconvertir segundos a dias")
#Entradas
s = float(input("Ingrese los segundos:"))
#Procesos y salidas
print(f"{s} segundos equivalen a {s//86400} dias, {(s%86400)//3600} horas, {s%86400%3600//60} y {s%86400%3600%60} segundos")