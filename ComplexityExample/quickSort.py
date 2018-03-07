def sortFromPivot(aList):
    
    pivot = aList[len(aList)-1]

    leftindex = 0
    rightindex = len(aList)-2

    while(True):
        while(aList[leftindex] < pivot and leftindex < len(aList)-1):
            leftindex+=1
        
        while(aList[rightindex] >= pivot and rightindex > 0):
            rightindex-=1

        if(leftindex < rightindex):
            temp = aList[rightindex]
            aList[rightindex] = aList[leftindex]
            aList[leftindex] = temp
        else:
            break

    temp = pivot
    aList[len(aList)-1] = aList[leftindex]
    aList[leftindex] = temp

    return [leftindex,aList]

def quickSort(myList):
    if(len(myList) <= 1):
        return myList

    data = sortFromPivot(myList)
    pivotIndex = data[0]

    alist = data[1]
    list1 = alist[0:pivotIndex]
    list2 = alist[pivotIndex+1:] #här inkluderar jag pivoten
    pivot = alist[pivotIndex]
    list1 = quickSort(list1)
    list2 = quickSort(list2)

    return list1+[pivot]+list2

myList = [14,33,27,10,35,19,42,44,103,5,12,14]
print(quickSort(myList))