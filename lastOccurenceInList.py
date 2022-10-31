def lastIndex(a,x):
    l=len(a)
    if l==0:
        return -1
    smallerList=a[1:]
    smalllerListOut=lastIndex(smallerList,x)
    if smalllerListOut!=-1:
        return smalllerListOut+1
    else:
        if a[0]==x:
            return 0
        else:
            return -1

#optimised Code
def lastIndexB(a,x,s):
    l=len(a)
    if s==l:
        return -1
    smallerListOutput=lastIndexB(a,x,s+1)
    if smallerListOutput!=-1:
        return smallerListOutput
    else:
        if a[s]==x:
            return s
        else:
            return -1


a=[1,2,4,5,6,4,8,7,1]
print(lastIndex(a,4))
print(lastIndexB(a,4,00))                                      