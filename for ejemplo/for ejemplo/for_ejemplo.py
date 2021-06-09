

suma = 0
n = int(input("limite: "))
if n>0:
    for i in range(1,n+1):
        if i != n:
            if i%2 == 0:
                print(f"+ {i}", end = " ")
            else:
                print(f"- {i}", end = " ")
        else:
            if i%2 == 0:
                print(f"+ {i} =", end = " ")
            else:
                print(f"- {i} =", end = " ")
        if i%2 == 0:
            suma +=i
        else:
            suma -= i
    print(suma)
else:
    print("Limite invalido")