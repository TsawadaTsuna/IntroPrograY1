#Realizado por Kevin Contreras A01635597 y Jorge Sanchez A01635375
import os, random

def clrscr():
   os.system("cls") if os.name=="nt" else os.system("clear")

# Elige la palabra a utilizar
#Funcion que selecciona la palabra a jugar con ayuda de un random
def elige_palabra(usadas):
    palabras = ["hola","fierro","computadora","tecnologia","guerra","salsa","datos","arroz","escuela","tierra"]
    if len(usadas)<10:
        i = random.randint(0,len(palabras)-1)
        while palabras[i] in usadas:
            i= random.randint(0,len(palabras)-1)
        return palabras[i]
    else:
        return ""

# Crear la lista de caracteres escondidos
#Funcion que genera una lista de asteriscos del mismo tamano que la palabra a jugar
def genera_escondida(palabra):
    lisharp=[]
    for i in palabra:
        lisharp.append("*")
    return lisharp


# Revisa si la letra está en la palabra, la cambia en la escondida y devuelve True, en caso de no estar devuelve False
#Funcion que sustituye los asteriscos en nuestra lista a desplegar por la letra jugada
def revisa_letra(palabra, escondida, letra):
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i]==letra:
                escondida[i]=letra
        return True
    else:
        return False

# Imprime a pantalla el dibujo del ahorcado dependiendo del numero de errores
def dibuja_ahorcado(numero_error):
    dibujos=['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
  =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']
    return dibujos[numero_error]

# Imprime el estado del juego, luego de haber revisado una palabra
#Hace las impresiones a pantalla
def imprime_estado(escondida, utilizadas, num_error):
    clrscr()
    if num_error>0:
        print(dibuja_ahorcado(num_error-1))
    print(escondida)
    print(utilizadas)
    print(f"Errores: {num_error}")
    #Ingresa tu código

# Pide al usuario una letra y verifica su validez
#Pide la letra valida que sea viable para jugar
def obtener_letra(utilizadas):
    l = input("Ingresa una letra: ")
    l=l.lower()
    lis=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    while l in utilizadas or l not in lis:
        if len(l)>1:
            l = input("Solo se aceptan letras solas. Ingresa otra letra: ")
        else:
            if l in utilizadas:
                l = input("Letra ya utilizada. Ingresa otra letra: ")
            elif l not in lis:
                l = input("Solo se aceptan letras. Ingresa otra letra: ")
    return l


# Código de un juego
def juego(palabra):
    errores=0
    letras_utilizadas=[]
    escondida=genera_escondida(palabra)
    print("Palabra escondida: ", end=" ")
    print(" ".join(escondida))
    while errores < 7:
        letra=obtener_letra(letras_utilizadas)
        letras_utilizadas.append(letra)
        if revisa_letra(palabra, escondida, letra):
            palabra_escondida="".join(escondida)
            imprime_estado(escondida, letras_utilizadas, errores)
            if palabra_escondida==palabra:
                return True
        else:
            errores+=1
            imprime_estado(escondida, letras_utilizadas, errores)
    return False


# Programa principal, se ejecutará el juego mientras el usuario quiera seguir jugando
palabras_usadas=[]
usuario="1"
print("Bienvenidos a .....")
print("""
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
|  _ \ / _  |  _ \ / _  |  _   _ \ / _  |  _  \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\___ |_| |_|\__  |_| |_| |_|\__ _|_| |_|
                    __/ |
                   |___/

""")

while usuario=="1":
    palabra=elige_palabra(palabras_usadas)
    if palabra!="":
        palabras_usadas.append(palabra)
        gano=juego(palabra)
        if gano:
            print("\nFelicidades, ganaste!!\n")
        else:
            print("\nHas perdido, lo siento, puedes jugar de nuevo...\n")
            del palabras_usadas[-1]
        usuario=input("Teclea 1 si quieres jugar de nuevo o cualquier tecla en caso contrario: ")
    else:
        usuario="0"
        print("Lo siento, se acabaron las palabras")

