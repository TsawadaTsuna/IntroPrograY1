#Realizado por Kevin Contreras
st = "bbab"
#Split por espacio
lis = st.split()
#Join para el nuevo string sin espacios
stt = "".join(lis)
#For para verificar la mitad de los elementos
for i in range(len(stt)//2):
   #Condicion para verificar si un caracter no es igual a su responsivo
    if stt[i] != stt[len(stt)-1-i]:
        print("no es plindoromo")
        break
    #Condicion para ver si esta en la ultima iteracion
    if i == len(stt)//2-1:
        if stt[i] != stt[len(stt)-1-i]:
            print("no es palindromo")
        else:
            print("si es palindromo")
