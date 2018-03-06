myList = [14,33,27,10,35,19,42,44]


def mergeLists(list1,list2):
    sortedList = []
    while(list1 != [] and list2 != []):
        if(list1[0]<list2[0]):
            sortedList.append(list1[0])
            list1.pop(0)
        else:
            sortedList.append(list2[0])
            list2.pop(0)
    
    while(list1 != []):
        sortedList.append(list1[0])
        list1.pop(0)
    
    while(list2 != []):
        sortedList.append(list2[0])
        list2.pop(0)

    return sortedList

def divideList(myList):
    n = len(myList)
    if(n == 1):
        return myList
    
    list1 = myList[0:n//2]
    list2 = myList[n//2:n]

    list1 = divideList(list1)
    list2 = divideList(list2)

    return(mergeLists(list1,list2))

def mergeSort(myList):
    return divideList(myList)

print(mergeSort(myList))