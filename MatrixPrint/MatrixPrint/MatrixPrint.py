#A function its the definition of a command,usng the word def follow by the name of the function and parentesis () where you put the parameters
def MatPrint(matrix):
    print("A matrix its a list of lists")
    #A first for to check the general list
    for i in range(len(matrix)):
        print("Elements of the ",(i+1)," sublist:",end="\n")
        #A second for to check the elementes of the sublists
        for j in range(len(matrix[i])):
            print(matrix[i][j],end="\n")

#We have a matrix of 3 sublists, where each sublist have 3 elements
matrix=[[1,2,3],[4,5,6],[7,8,9]]

#We are using the function. This is called invoque
#We invoque the function with the list matrix as argument
#The rguments are the values of the parameters when we invoque the function
MatPrint(matrix)
