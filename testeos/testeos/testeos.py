
#def checkPalindrome(inputString):
#    lis = []
 #   for i in range((len(inputString)//2)+1):
  #      if inputString[i] != inputString[len(inputString)-1-i]:
   #         return False
    #return True


#print(checkPalindrome("aabaa"))
#if checkPalindrome("aabaa") == True:
 #   print("ok")
#else:
 #   print("not ok")

#def shapeArea(n):
 #   a =[1]
  #  for i in range(2,n+1):
   #     a.append(a[i-2]+((i-1)*4))
    #return a[n-1]
#print(shapeArea(4))

#def almostIncreasingSequence(sequence):
#    hits = False
 #   pre = sequence[0]
  #  for i in range(len(sequence)-1):
   #     if sequence[i+1]<=sequence[i] or sequence[i+1]<=pre:
    #        if i==0:
     #           pre=sequence[i+1]
      #      else:
       #         pre=sequence[i-1]
        #    if hits==False:
#                hits = True
 #               
  #          else:
   #             return False
    #    else:
     #       pre=sequence[i]
#    return True

#print(almostIncreasingSequence([1, 2, 3, 4, 5, 3, 5, 6]))

dic1 = { 
    }
    for i in s1:
        var = dic1.get(i)
        if var == None:
            dic1[i] = 1
        else:
            dic1[i] = var+1
    dic2 ={
        }
    for i in s2:
        var = dic2.get(i)
        if var == None:
            dic2[i] = 1
        else:
            dic2[i] = var+1
    lis1 = list(dic1.keys())
    con1 =0
    con2=0
    sum = 0
    for j in lis1:
        con1 = dic1.get(j)
        con2 = dic2.get(j)
        if con2 == None:
            continue
        if con1 < con2:
            sum+=con1
        else:
            sum+= con2
    return sum