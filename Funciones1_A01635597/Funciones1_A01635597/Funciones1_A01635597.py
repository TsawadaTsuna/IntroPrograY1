#Realizado por Kevin Contreras
import time
def energia_cinetica(m,v):
    return 1/2*m*v**2
def multiplos_comunes(n1,n2,lim):
    lis = []
    for i in range(lim+1):
        if i % n1 == 0 and i% n2 ==0:
            lis.append(i)
    return lis
def ofertas(charge):
    if charge<10:
        return charge
    elif charge<=25:
        return charge+charge*0.03
    elif charge<=50:
        return charge+charge*0.08
    else:
        return charge+charge*0.2
def barra_progreso(t):
    for i in range(t//5):
        time.sleep(5)
        print("X", end="",flush=True)
def menu():
    op = input("""Seleccione una opcion:
1. Calcular energia cinetica.
2. Verificar multiplos comunes.
3. Verificar tu saldo de la recarga a tu tarjeta de llamadas.
4. Ver una barra de progreso.
5. Salir
opcion: """)
    return op
def main():
    op = "0"
    while op != "5":
        op=menu()
        if op =="1":
            m = float(input("Ingrese la masa del objeto: "))
            v = float(input("Ingrese la velocidad del objeto: "))
            print(f"La energia cinetica del objeto es: {energia_cinetica(m,v)} J")
            print("\n")
        elif op=="2":
            n1 = int(input("Ingrese el primer numero a verfificar: "))
            n2 = int(input("Ingrese el segundo numero a verfificar: "))
            lim = int(input("Ingrese el limite hasta el cual se va a verificar a verfificar: "))
            print(f"Los multiplos comunes de {n1} y {n2} hasta {lim} son: {multiplos_comunes(n1,n2,lim)}")
            print("\n")
        elif op =="3":
            charge = float(input("Ingrese la cantidad a recargar en su tarjeta: "))
            print(f"Su recarga final es de: {ofertas(charge)}")
            print("\n")
        elif op == "4":
            seg = int(input("Ingrese la catidad de segundos que va a durar la barra de progreso: "))
            barra_progreso(seg)
            print("\n")
        elif op == "5":
            print("Gracias, vuelva pronto")
            print("\n")
        else:
            print("Opcion inavlida.")
            print("\n")
main()