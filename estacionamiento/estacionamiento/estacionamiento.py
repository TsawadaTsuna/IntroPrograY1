import random
def estacionamiento():
    file=open("park.txt",'w')
    for i in range(10):
        for j in range(15):
            v=random.randint(0,1)
            if j!=14:
                file.write(f"{v},")
            else:
                file.write(f"{v}")
        file.write("\n")
    file.close()

estacionamiento()

def vacios():
    lis=[]
    lisv=[]
    chars="ABCDEFGHIJ"
    try:
        file=open("park.txt",'r')
    except:
        print("error")
    else:
        for line in file:
            v=line.rstrip()
            lis.append(v.split(","))
        for row in range(10):
            for col in range(1,16):
                if lis[row][col-1]=="0":
                    x=f"{chars[row]}{col}"
                    lisv.append(x)
        file.close()
        return lisv



print(vacios())