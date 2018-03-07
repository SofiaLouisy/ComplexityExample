def mergeSort(myList):
    n = len(myList)
    
    if(n == 1):
        return myList
    
    list1 = myList[:n//2]
    list2 = myList[n//2:]

    mergeSort(list1)
    mergeSort(list2)

    k = 0
    while(list1 != [] and list2 != []):
        print(list1)
        print(list2)
        if(list1[0]<list2[0]):
            myList[k] = list1.pop(0)
            k+=1
        else:
            myList[k] = list2.pop(0)
            k+=1

    
    while(list1 != []):
        myList[k] = list1.pop(0)
        k+=1
    
    while(list2 != []):
        myList[k] = list2.pop(0)
        k+=1

myList = [14,33,27,10,35,19,42,44]
mergeSort(myList)
print(myList)