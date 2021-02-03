lim = int(input("estudiantes: "))
ma1 = 0 
ma2 = 0
for i in range(1,lim+1):
    cal = int(input(f"Ingrese la calificacion del alumno {i}: "))
    if cal > ma1:
        ma2 = ma1
        ma1 = cal
    elif cal>ma2:
        ma2 = cal
print(f"La primer calificacion mayor es: {ma1}")
print(f"La segunda calificacion mayor es: {ma2}")