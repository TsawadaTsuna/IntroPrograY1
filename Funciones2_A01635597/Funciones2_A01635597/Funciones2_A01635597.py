import random
#Funcion que dada una lista de strings regresa cuantas tienen un cierto numero de letras o mas a travez de un contador
def con_N_letras(list, n):
    cont=0
    for i in list:
        if len(i)>=n:
            cont+=1
    return cont
#Funcion que duplica los valores de una lista
def duplica(list):
    for i in len(list):
        list[i]*=2
#Funcion que combina intercaladamente 2 listas
def combina_listas(list1,list2):
    max=0
    if len(list1)<len(list2):
        max=len(list2)
    else:
        max=len(list1)
    lis=[]
    for i in range(max):
        if i<len(list1):
            lis.append(list1[i])
        if i<len(list2):
            lis.append(list2[i])
    return lis
#Funcion que simula un cierto numero de tiradas de un dado y regresa la suma de estas
def tirada(n):
    sum = 0
    for i in range(n):
        sum+=random.randint(1,6)
    return sum
#Funcion que revuelve el orden de las letras de un string
def revuelvePalabra(st):
    r=0
    lisind=[]
    lisch=[]
    for i in range(len(st)):
        r=random.randint(0,len(st)-1)
        while r in lisind:
            r=random.randint(0,len(st)-1)
        lisind.append(r)
        lisch.append(st[r])
    str="".join(lisch)
    return str
#Funcion que realiza una busqueda binaria en una lista ordenada
def busqueda_binaria(lis, n):
    lim1=0
    lim2=len(lis)-1
    c=0
    while c==0:
        if lim1!=lim2:
            if lis[(lim2-lim1)//2+lim1] == n:
                return (lim2-lim1)//2+lim1
            elif lis[(lim2-lim1)//2+lim1] > n:
                lim2=(lim2-lim1)//2+lim1
            else:
                lim1 =(lim2-lim1)//2+lim1
        else:
            if lis[lim1]==n:
                return lim1
            else:
                return -1
#Funcion que genera una lista de strings con solo las primeras n letras de cada string de otro lista dada
def solo_x(lis,x):
    lis2=[]
    for i in lis:
        lis2.append(i[:x])
    return lis2
#Funcion que separa un string con guiones cada cierto numero de letras
def separa_guiones(st,n):
    lis=[]
    c=0
    for i in range(len(st)):
        lis.append(st[i])
        c+=1
        if i!=len(st)-1:
            
            if c==n:
                lis.append("-")
                c=0
    sr="".join(lis)
    return sr

        


