import random
#Programa realizado por Kevin Contreras A01635597
i = "4"
while i != "3":
    print("""Hola bienvenido a la seleccion de juegos.
Seleccione un juego:
1. Adivine el numero que genera la computadora.
2. Ingrese un numero que la computadora tratara de adivinar.
3. Salir""")
    op = input(">")
    #Opcion del primer juego
    if op == "1":
        print("Hola y bienvenido. Tiene 7 intentos para adivinar un numero aleatorio entre 1 y 100 y ganar")
        num = random.randint(1,100)
        c = 1
#Ciclo para verificar los intentos

        while c<=7:
            n = int(input("Ingrese un numero. Trate de adivinar:"))
            #Condicional para marcar la comparacion entre el numero dado y el generado
            if n == num:
                print("Felicidades usted ha ganado.")
                c = 8
            elif n < num:
                print("Error, el numero que ingreso es menor que el numero generado")
                print(f"Le quedan {(c-7)*-1} intentos")
                c+=1
            else:
                print("Error, el numero que ingreso es mayor que el numero generado")
                print(f"Le quedan {(c-7)*-1} intentos")
                c+=1
        print("Fin del juego. Gracias por jugar")
        #Repeticion
        rep = input("""Quiere volver a ejecutar el programa
1. Si
2. No
>""")
        if rep == "2":
            i = "3"
    elif op == "2":
        #Segundo programa
        print("""Programa donde la computadora intenta adivinar el numero que penso.
Indique en cada numero generado por la computadora si es mayor, menor o igual.""")
        r1 = int(input("ingrese el valor minimo del intervalo a adivinar: "))
        r2 = int(input("ingrese el valor maximo del intervalo a adivinar: "))
        
        rel = ""
        #Primer valor
        num = r1+((r2-r1)//2)
        #Ciclo que quiebra cuando se teclea que es igual
        while rel != "igual":
            
            print(f"Tu numero es {num}?")
            rel = input("El numero es mayor, menor o igual: ")
            if rel == "mayor":
                #Modificador del rango
                r1 = num
                num = num + (r2-r1)//2
            elif rel == "menor":
                #Modificador del rango
                r2 = num
                num = num - (r2-r1)//2
            elif rel == "igual":
                print("Acerte. Gracias por jugar")
            else:
                print("opcion invalida")
        print("Fin del juego.")
        #Repeticion
        rep = input("""Quiere volver a ejecutar el programa
1. Si
2. No
>""")
        if rep == "2":
            i = "3"
    elif op == "3":
        #Opcion de salir
        i = "3"
    else:
        #Opcion invalida
        print("opcion invalida")
            
            
