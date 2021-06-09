import math
def segundos(seg):
    st = 'dias: ',seg//86400,', horas: ',seg%86400//3600,', minutos: ',seg%86400%3600//60,', segundos: ',seg%86400%3600%60
    return st
def ftToCm(ft):
    return ft*30.48
def esfera(r):
    return 4/3*math.pi*r**3
def mult(n1,n2):
    if n1%n2==0:
        return True
    else:
        return False
def comp(n1,n2):
    if n1>n2:
        return 1
    elif n1==n2:
        return 0
    else:
        return -1
op = input("""Seleccione una opcion:
1. Convertir una cantidad de segundos a dias, horas, minutos y segundos.
2. Convertir pies a centimetros.
3. Calcular volumen de una esfera.
4. Comprobar si un numero es multiplo de otro.
5. Comparar dos numeros.
Opcion: """)
if op == "1":
    seg= int(input("Ingrese una cantidad de segundos: "))
    print(segundos(seg))
elif op == "2":
    pies = int(input("Ingrese la cantidad de pies a convertir a centimetros: "))
    print(f"{pies}ft es igual a {ftToCm(pies)}cm.")
elif op == "3":
    ra = float(input("Ingrese el radio de la esfera en cm: "))
    print(f"El volumen de la esfera es: {esfera(ra)}")
elif op == "4":
    num1 = int(input("Ingrese el numero a comprobar: "))
    num2 = int(input("Ingrese el divisor: "))
    if mult(num1,num2):
        print("si es multiplo")
    else:
        print("No es multiplo")
elif op == "5":
    num1 = int(input("Ingrese el primer numero a comprobar: "))
    num2 = int(input("Ingrese el segundo numero a comprobar: "))
    if comp(num1,num2)==1:
        print(f"{num1} es mayor a {num2}")
    elif comp(num1, num2)==0:
        print("Los numeros son iguales")
    else:
        print(f"{num2} es mayor que {num1}")
else:
    print("Opcion invalida")