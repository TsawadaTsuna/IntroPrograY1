#Realizado por Kevin Contreras
print("Programa comparador de años")
#Entradas
a1 = int(input("En que año estamos:"))
a2 = int(input("Ingrese un año cualquiera:"))
if a2-a1 == 1:
    print(f"Falta un año para el {a2}")
elif a1-a2 == 1:
    print(f"Ya paso 1 año desde el {a2}")
elif a2>a1:
    print(f"Faltan {a2-a1} años para el {a2}")
else:
    print(f"Han pasado {a1-a2} desde el {a2}")