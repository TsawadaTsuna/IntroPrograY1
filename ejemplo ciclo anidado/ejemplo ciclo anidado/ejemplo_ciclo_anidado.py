def triangulo2(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1,end="")
        print()

def tri3(n):
    for i in range(n):
        for k in range(n-i,0,-1):
            print(k, end="")
        print()

def otrotri(n):
    for i in range(1,n+1):
        print("  "*(n-i),end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
otrotri(5)



