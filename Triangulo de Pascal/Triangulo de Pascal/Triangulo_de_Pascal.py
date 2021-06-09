def triPascal(n):
    for i in range(1,n+1):
        for j in range(n,0,-1):
            print(j if j<=i else " ", end="")
        for k in range(1,i+1):
            print(k if k<=i and k!=1 else "", end="")
        print()

triPascal(5)
