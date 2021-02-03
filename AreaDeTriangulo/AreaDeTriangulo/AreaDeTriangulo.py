#Kevin Contreras A01635597
base = input("Ingrese el tamaño de la base del triangulo: ")
alt = input("Ingrese el tamaño de la altura del triangulo: ")
try:
    base = int(base)
    alt = int(alt)
except:
    print("Porfavor ingrese un número")
else:
    print(f"El are del triangulo es {base*alt/2}")
