#Reakizado por Kevin Contreras
def divide_cadena(st,n):
    lis=[]
    for i in range(0,len(st),n):
        lis.append(st[i:i+n])
    return lis

