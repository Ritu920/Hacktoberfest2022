def isSorted(a):
    l=len(a)
    if l==0 or l==1:
        return True
    if a[0]>a[1]:
        return False
    smallerList=a[1:]
    isSmallerListSorted=isSorted(smallerList)  
    return isSmallerListSorted  

    


#OPTIMISED WAY

def isSort(a,start):
    l=len(a)
    if start==l-1 or start==l:
        return True
    if a[start]>a[start+1]:
        return False
    isSmallPartSorted=isSort(a,start+1)
    return isSmallPartSorted

a=[1,2,3,3,4,5,6]
print(isSorted(a))  
print(isSort(a,0))  