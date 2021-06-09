#Realizado por Siqi Yang y Kevin Contreras
import datetime,os
import matplotlib.pyplot as plt
#Funcion para limpiar pantalla con la libreria os
def clnscrn():
   os.system("cls") if os.name=="nt" else os.system("clear")
#Funcion para esperar un enter y evitar que el menu se muestre instantaneamente sin ver lo escrito
def wait():
    input("Presione enter para continuar")


#Funcion que pide el string gen que es un numero string que representa la generacion y la columna por estadistica
#Regresa el nombre del Pokemon con mas puntos de alguna caracteristica de una determinada generacion
def max_stat(gen,stat):
    mayorstat=0
    current=0
    name=""
    lis=[]
    try:
        file=open("Pokemon.csv",'r')
    except:
        print("El archivo no existe o no se puede abrir")
    else:
        for line in file:
            lis=line.rstrip().split(",")
            if lis[11]==gen:
                
                try:
                    current=int(lis[stat])
                except:
                    print("No se puede convertir")
                    
                else:
                    if current>mayorstat:
                        mayorstat=current
                        name=lis[1]
    file.close()
   
    return name
#Funcion que genera el reporte de Pokemones con mejores estadisticas utilizando la libreria daytime y la funcion max_stat
def Reporte():
    
    try:
        file = open(f"Reporte_{datetime.datetime.now().date()}.txt",'w')
    except:
        print("El archivo no existe o produce error")
    else:
        gens="123456"
        file.write("Reporte de Pokemones con mejores estadisticas por generacion\n\n")
        for i in range(1,7):
            file.write(f"Generacion {i}\n\nMaximos puntos de vida: {max_stat(gens[i-1],5)}\n")
            file.write(f"Maximos puntos de ataque: {max_stat(gens[i-1],6)}\n")
            file.write(f"Maximos puntos de defensa: {max_stat(gens[i-1],7)}\n")
            file.write(f"Maximos puntos de ataque especial: {max_stat(gens[i-1],8)}\n")
            file.write(f"Maximos puntos de defensa especial: {max_stat(gens[i-1],9)}\n")
            file.write(f"Maximos puntos de velocidad: {max_stat(gens[i-1],10)}\n\n")
            file.write("---------------------------------------------------------------------\n\n")
        file.write(f"Generado: {datetime.datetime.now()}")
        file.close()

#Funcion que imprime los NOMBRES de los Pokemones en base a val que es el valor que ingreso el usuario y col que es la columna que seleeciona el usuario en un menu
def busqueda(col,val):
    list=[]
    cont=0
    try:
        file=open("Pokemon.csv",'r')
    except:
        print("El archivo no existe o produce error")
    else:
        list=[]
        for line in file:
            list=line.rstrip().split(",")
            if cont != 800:
                if list[col]==val:
                    print(f"•{list[1]}")
                    cont=0
            else:
                print("Ninguno , los parametros de buqueda no coinciden con un Pokemon")
            cont+=1
        file.close()
        

#Funcion que imprime los NOMBRES de los Pokemones de un determinado tipo y otra caracteristica
def busqueda_av(type,val,sel):
    list=[]
    cont = 0
    try:
        file=open("Pokemon.csv",'r')
    except:
        print("El archivo no existe o produce error")
    else:
        list=[]
        for line in file:
            list=line.rstrip().split(",")
            #Validacion en las columnas de tipo y la caracteristica extra a evaluar. Convirtiendo a minuscualas para evitar problemas
            if cont != 800:
                if sel == "1":
                    if (list[2].lower()==type or list[3].lower()==type) and list[11]==val:
                        print(f"•{list[1]}")
                elif sel == "2":
                    if (list[2]==type or list[3]==type) and list[4]==val:
                        print(f"•{list[1]}")
            else:
                print("Ninguno , los parametros de buqueda no coinciden con un Pokemon")
            cont+=1
        file.close()

#Funcion que saca el porcentaje Pokemones de acuerdo a su tipo 
def promedio(type):
    sum=0
    lis=[]
    try:
        file=open("Pokemon.csv",'r')
    except:
        print("El archivo no existe o produce error")
        
    else:
        for line in file:
            lis=line.rstrip().split(",")
            if lis[2] == type or lis[3]== type:
                sum+=1
        file.close()
        return f"{sum/800*100:.2f}"

#Funcion que saca el porcentaje de Pokemones legendarios por generacion
def legendarios(gen):
    sum=0
    lis=[]
    cont=0
    try:
        file=open("Pokemon.csv",'r')
    except:
        print("El archivo no existe o no se puede abrir")
    else:
        for line in file:
            lis=line.rstrip().split(",")
            if lis[11]==gen:
                cont+=1
                if lis[12]=="True":
                    sum+=1
    return sum/cont*100

#Funcion que calcula la suma total de las estadisticas de todos los pokemones en una determinada generacion
def statstotales(gen):
    sum=0
    val=0
    lis=[]
    try:
        file=open("Pokemon.csv",'r')
    except:
        print("El archivo no existe o no se puede abrir")
    else:
        for line in file:
            lis=line.rstrip().split(",")
            if lis[11]==gen:
                val=int(lis[4])
                sum+=val
        file.close()
        
    return sum

#Funcion que genera la grafica de generacion vs poder total usando la funcion statstotales y la libreria matplotlib nombrada como plt
def grafica():
    #Valores del eje x
    names=["Gen. 1","Gen. 2","Gen. 3","Gen. 4","Gen. 5","Gen. 6"]
    #Valores del eje Y
    values=[statstotales("1"),statstotales("2"),statstotales("3"),statstotales("4"),statstotales("5"),statstotales("6")]
    #Creacion de la linea agregando el conjunto de datos en X y luego en Y
    plt.plot(names,values)
    #Rango de valores de los ejes [X inicial, X final, Y inicial, Y final]
    plt.axis([0,6,35000,75000])
    #Titulo superior
    plt.suptitle("Fuerza total de los Pokemones por generacion")
    #Leyenda del eje X
    plt.xlabel("Genraciones")
    #Leyenda del eje Y
    plt.ylabel("Total de fuerzas por generacion")
    #Metodo de la libreria para mostrar la grafica
    plt.show()

op="0"
#Inicio del programa principal
#Menu que cicla las opciones
while op !="6":
    clnscrn()
    op=input("""Hola, bienvenido a tu dataset de Pokemon. Porfavor selecciona una opcion:
1. Reporte. Pokemones con mejores estadisticas por generacion.
2. Busqueda de pokemon por dato.
3. Consulta avanzada.
4. Estadisticas.
5. Grafica.
6. Salir.
Opcion: """)
    if op == "1":
        #Generacion de reporte
        try:
            Reporte()
        except:
            print("Se ha producido un error")
        else:
            clnscrn()
            print(f"Reporte_{datetime.datetime.now().date()}.txt generado exitosamente")
            wait()
    elif op == "2":
        clnscrn()
        opbu="0"
        #Submenu para las opciones de busqueda sencilla
        opbu=input("""Seleccione el dato por el cual quiere buscar la informacion de un Pokemon:
1.Numero de Pokemon.
2.Tipo del Pokemon
3.Vida del Pokemon.
4.Ataque del Pokemon.
5.Defensa del Pokemon.
6.Ataque especial del Pokemon.
7.Defensa especial del pokemon.
8.Velocidad del Pokemon.
Opcion: """)
        if opbu == "1":
            clnscrn()
            col=0
            val=input("Ingresa el numero del Pokemon a buscar: ")
            print(f"El o los pokemones con el dato ingresado son:")
            busqueda(col,val)
            wait()
        elif opbu == "2":
            clnscrn()
            col=2
            val=input("Ingresa el tipo del Pokemon a buscar en ingles: ")
            print(f"El o los pokemones con el dato ingresado son:")
            busqueda(col,val)
            wait()
        elif opbu == "3":
            clnscrn()
            col=5
            val=input("Ingresa los puntos de vida del Pokemon a buscar: ")
            print(f"El o los pokemones con el dato ingresado son:")
            busqueda(col,val)
            wait()
        elif opbu == "4":
            clnscrn()
            col=6
            val=input("Ingresa los puntos de ataque del Pokemon a buscar: ")
            print(f"El o los pokemones con el dato ingresado son:")
            busqueda(col,val)
            wait()
        elif opbu == "5":
            clnscrn()
            col=7
            val=input("Ingresa los puntos de defensa del Pokemon a buscar: ")
            print(f"El o los pokemones con el dato ingresado son:")
            busqueda(col,val)
            wait()
        elif opbu == "6":
            clnscrn()
            col=8
            val=input("Ingresa los puntos de ataque especial del Pokemon a buscar: ")
            print(f"El o los pokemones con el dato ingresado son:")
            busqueda(col,val)
            wait()
        elif opbu == "7":
            clnscrn()
            col=9
            val=input("Ingresa los puntos de defensa especial del Pokemon a buscar: ")
            print(f"El o los pokemones con el dato ingresado son:")
            busqueda(col,val)
            wait()
        elif opbu == "8":
            clnscrn()
            col=10
            val=input("Ingresa los puntos de velocidad del Pokemon a buscar: ")
            print(f"El o los pokemones con el dato ingresado son:")
            busqueda(col,val)
            wait()
        else:
            clnscrn()
            print("Opcion invalida")
            wait()

    elif op == "3":
        
        clnscrn()
        opav="0"
        #Submenu para las opciones de busqueda avanzada
        opav=input("""Seleccione como quiere buscar el Pokemon.
1. Por tipo y generacion.
2. Por tipo y poder total.
Opcion: """)
        type=""
        
            
            
        if opav == "1":
            type=input("Ingresa el tipo del Pokemon en ingles: ")
            type=type.lower()
            gener=""
            gener=input("Ingresa el numero de la generacion a buscar: ")
            print(f"El/los Pokemones de tipo {type} de la generacion {gener} son:")
            busqueda_av(type,gener,opav)
        elif opav == "2":
            type=input("Ingresa el tipo del Pokemon en ingles: ")
            type=type.lower()
            pow=""
            pow=input("Ingresa el numero poder total del pokemon a buscar a buscar: ")
            print(f"El/los Pokemones de tipo {type} con poder de {pow} son:")
            busqueda_av(type,pow,opav)
        else:
            print("Opcion inavalida")
        wait()
    elif op == "4":
        clnscrn()

        opes="0"
        #Submenu de estadisticas
        opes=input("""Seleccione la estadistica a analizar:
1. Promedios de Pokemon por tipo.
2. Promedio de Pokemones legendarios en relacion a su generacion.
Opcion: """)
        if opes == "1":
            clnscrn()
            print(f"Porcentaje de Pokemones tipo normal: ",promedio("Normal"),"%")
            print("Porcentaje de Pokemones tipo fuego: ",promedio("Fire"),"%")
            print("Porcentaje de Pokemones tipo agua: ",promedio("Water"),"%")
            print("Porcentaje de Pokemones tipo planta: ",promedio("Grass"),"%")
            print("Porcentaje de Pokemones tipo volador: ",promedio("Flying"),"%")
            print("Porcentaje de Pokemones tipo luchador: ",promedio("Fighting"),"%")
            print("Porcentaje de Pokemones tipo tierra: ",promedio("Ground"),"%")
            print("Porcentaje de Pokemones tipo roca: ",promedio("Rock"),"%")
            print("Porcentaje de Pokemones tipo electrico: ",promedio("Electric"),"%")
            print("Porcentaje de Pokemones tipo hielo: ",promedio("Ice"),"%")
            print("Porcentaje de Pokemones tipo siniestro: ",promedio("Dark"),"%")
            print("Porcentaje de Pokemones tipo acero: ",promedio("Steel"),"%")
            print("Porcentaje de Pokemones tipo veneno: ",promedio("Poison"),"%")
            print("Porcentaje de Pokemones tipo fantasma: ",promedio("Ghost"),"%")
            print("Porcentaje de Pokemones tipo insecto: ",promedio("Bug"),"%")
            print("Porcentaje de Pokemones tipo dragon: ",promedio("Dragon"),"%")
            print("Porcentaje de Pokemones tipo psiquico: ",promedio("Psychic"),"%")
            print("Porcentaje de Pokemones tipo hada: ",promedio("Fairy"),"%")
            wait()
        elif opes == "2":
            clnscrn()
            gens="123456"
            print(F"El porcentaje de pokemones legendarios en la primera generacion es: {legendarios(gens[0]):.2f}%")
            print(f"El porcentaje de pokemones legendarios en la segunda generacion es: {legendarios(gens[1]):.2f}%")
            print(f"El porcentaje de pokemones legendarios en la tercera generacion es: {legendarios(gens[2]):.2f}%")
            print(f"El porcentaje de pokemones legendarios en la cuarta generacion es: {legendarios(gens[3]):.2f}%")
            print(f"El porcentaje de pokemones legendarios en la quinta generacion es: {legendarios(gens[4]):.2f}%")
            print(f"El porcentaje de pokemones legendarios en la sexta generacion es: {legendarios(gens[5]):.2f}%")
            wait()
        else:
            clnscrn()
            print("Opcion invalida")
            wait()
        
    elif op =="5":
        #Generacion de grafica
        clnscrn()
        grafica()
        print("Grafica generada exitosamente")
        wait()
        
    elif op == "6":
        #Salida
        print("Gracias por usar este programa")
    else:
        print("Dato invalido")