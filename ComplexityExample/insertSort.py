myList = [14,33,27,10,35,19,42,44]

def isUnsorted(elem1,elem2):
    if(elem1 >= elem2):
        return True
    else:
        return False

#Check all elem
for i in range(1,len(myList)):
    j = i
    #Sort elem
    while (j>0):
        if(isUnsorted(myList[j-1],myList[j])):
            temp = myList[j-1]
            myList[j-1] = myList[j]
            myList[j] = temp
            j-=1
        else:
            break

print(myList)