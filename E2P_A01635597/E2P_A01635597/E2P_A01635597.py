#Realizado por Kevin Contreras
#Funcion que convierte milisegundos a horas minutos y segundos
def convertir_milis(ms):
    seg=ms//1000
    min=seg//60
    horas=min//60
    min=min%60
    seg=seg%60
    st=f"{horas}:{min}:{seg}"
    return st
#Funcion que verifica si un numero es perfecto a travez de un ciclo
def es_perfecto(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return True
    else:
        return False
#Funcion que verifica cuantas curps de una lista son de un cierto estado a traves de una abreviacion utilizando indexacion y ciclo
#Funcion recibe lista de strings y un string que representa la abreviatura
def por_estado(list,ed):
    cont=0
    ed=ed.upper()
    for i in list:
        #Verificacion por indices ya que si uso el comando in puede que sea de un estado pero me lo detecta de otro
        if ed[0]==i[11] and ed[1]==i[12]:
            cont+=1
    return cont
#Funcion menu para correr el programa y pedir datos por funcion:
def menu():
    op = 0
    while op!="4":
        op=input("""Hola,porfavor seleccione un programa:
1. Convertir milisegundos
2. Verificar si un numero es perfecto
3. Contabilizar curps por estado
4. Salir
Opcion: """)
        print("\n")
        if op =="1":
            ms=int(input("Ingrese la cantidad de milisegundos a convertir: "))
            print(f"{ms} milisegundos son "+convertir_milis(ms)+" (horas:minutos:segundos)")
            print("\n")
        elif op=="2":
            num=int(input("Ingrese numero a verificar si es perfecto: "))
            if es_perfecto(num):
                print(f"{num} es perfecto")
                print("\n")
            else:
                print(f"{num} no es perfecto")
                print("\n")
        elif op=="3":
            lis=["AECJ940429HCHRRS01", "VIRF890629HSLZBR0", "GOLP850729MCHNNR03",  "JAAJ761004HCLLGS07", "COCA761007MDGRNN02", "FOAJ780210HGRLDR09", "VABI820909HGRZLL07"]
            ed=input("Escriba la abreviatura del estado que quiere contabilizar: ")
            ed=ed.upper()
            print(f"Las CURPS del estado {ed} son: {por_estado(lis,ed)}")
            print("\n")
        elif op == "4":
            print("Gracias por usar este programa")
        else:
            print("Opcion invalida")
            print("\n")
menu()