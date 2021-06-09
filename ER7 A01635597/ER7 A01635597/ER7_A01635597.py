#Programa realizado por Kevin Contreras A01635597
frase = input("ingrese una frase: ")
voc = input("ingrese una vocal: ")
lis = []
for i in range(len(frase)):
    if frase[i] in "aeiouAEIOU":
        lis.append(voc)
    else:
        lis.append(frase[i])
print("".join(lis))
