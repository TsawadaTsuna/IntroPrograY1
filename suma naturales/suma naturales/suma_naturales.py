lim = int(input("limite: "))
sum = 0
i = 0
while i <= lim:
    sum+=1/2**i
    i+=1
print(sum)