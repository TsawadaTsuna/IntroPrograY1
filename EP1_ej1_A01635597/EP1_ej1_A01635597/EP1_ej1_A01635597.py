#Realizado por Kevin Contreras A01635597
print("Programa que realiza converciones de unidades")
op = input("""Elije un opcion:
1. Convertir de pies a centimetros.
2. Convertir de centrimetros  pies
3. Salir
>""")
#Ciclo para controlar la repeticion del menu
while op != "3":
    #Condicional para realizar la accion y pedir nuevos datos
    if op == "1":
        ft = float(input("Ingrese la cantidad de pies para convertir a cm:"))
        print(f"{ft} pies es equivalente a {ft*30.48} cm.")
        op = input("""Elije un opcion:
1. Convertir de pies a centimetros.
2. Convertir de centrimetros  pies
3. Salir
>""")
    elif op == "2":
        cm = float(input("Ingrese los centrimetos para convertir a pulgadas:"))
        print(f"{cm} centrimetros es equivalente a {cm/2.54} pulgadas")
        op = input("""Elije un opcion:
1. Convertir de pies a centimetros.
2. Convertir de centrimetros  pies
3. Salir
>""")
    elif op == "3":
        print("Gracias por usar este progrma")
        #Quiebre del ciclo
        op = "3"
    else:
        print("Opcion invalida,seleccione una correcta")
        op = input("""Elije un opcion:
1. Convertir de pies a centimetros.
2. Convertir de centrimetros  pies
3. Salir
>""")

