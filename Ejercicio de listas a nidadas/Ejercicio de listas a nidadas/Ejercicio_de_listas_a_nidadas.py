import random

def printmatrix(matrix):
    for row in matrix:
        for val in row:
            print(f"{val:3d}", end=" ")
        print()

def crea_matriz1(n):
    matriz=[]
    for row in range(n):
        lis=[]
        for col in range(n):
            lis.append(-1)
        matriz.append(lis)
    return matriz

def crea_matriz2(n):
    matriz=[]
    for row in range(n):
        lis=[]
        for col in range(n):
            lis.append(col)
        matriz.append(lis)
    return matriz

def crea_matriz3(n):
    matriz=[]
    for row in range(n):
        lis=[]
        for col in range(n):
            lis.append(row)
        matriz.append(lis)
    return matriz

def crea_matriz_alet(r,c):
    matriz=[]
    for row in range(r):
        lis=[]
        for col in range(c):
            v=random.randint(0,100)
            lis.append(v)
        matriz.append(lis)
    return matriz

def crea_matriz4(n):
    matriz=[]
    for row in range(1,n+1):
        lis=[]
        for col in range(1,n+1):
            lis.append(col*n-((row-n)*-1))
        matriz.append(lis)
    return matriz

def crea_matriz4comp(n):
    matriz=[[col*n-((row-n)*-1) for col in range(1,n+1)] for row in range(1,n+1)]
    return matriz

def crea_matriz5(n):
    matriz=[[row*n-((col-n)*-1) for col in range(1,n+1)] for row in range(1,n+1)]
    return matriz

def cuenta_pares(matr):
    c=0
    for r in matr:
        for i in r:
            if i % 2 ==0:
                c+=1
    return c

def cuenta_positivos(matr):
    c=0
    for r in matr:
        for i in r:
            if i >= 0:
                c+=1
    return c

def cambia_negativos(matr):
    for row in  range(len(matr)):
        for col in range(len(matr[0])):
            if matr[row][col]<0:
                matr[row][col]=0


def cuenta_repeticiones(matr,n):
    c=0
    for r in matr:
        for i in r:
            if i  ==n:
                c+=1
    return c

def busca(matr,n):
    for r in matr:
        for val in r:
            if val == n:
                return True
    return False

def suma_mayor5(matr):
    s=0
    for r in matr:
        for val in r:
            if val > 5:
                s+=val
    return s

def cambia_ceros(matr):
    for row in  range(len(matr)):
        for col in range(len(matr[0])):
            if matr[row][col]==0:
                matr[row][col]=row+col+2
