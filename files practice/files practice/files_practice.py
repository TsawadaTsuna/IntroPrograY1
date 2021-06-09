try:
    file = open("Prueba1.txt",'w',encoding="UTF-8")
except:
    print("exception")
else:
    file.write("1234567890\n")
    file.write("abcdefghijklmnopqrstuvwxyz")
    file.close()