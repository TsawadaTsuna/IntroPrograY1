lis = [1,2,3,4,5,6,7,8,9]

ini = 2
pibo=-2
rec = []
dis = []
i=0
while i<len(lis):
    if ((ini not in rec) and (ini < len(lis))):
        dis.append(lis[ini])
        rec.append(ini)
        ini+=pibo
        i+=1
    elif (ini in rec):
        ini+=1
    else:
        ini = ini-len(lis)
        
print(dis)


        
