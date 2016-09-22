#python implementation of Merge Sort

def merge(left,right,alist):
    i,j,k=0,0,0
    while(i<len(left)) and (j<len(right)):
        if (left[i]<right[j]):
            alist[k]=left[i]
            i+=1
        else:
            alist[k]=right[j]
            j+=1
        k+=1

    while i<len(left):
        alist[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        alist[k]=right[j]
        j+=1
        k+=1

    return alist

def mergesort(alist):
    if len(alist)>1:
        
        mid=len(alist)//2
        left=alist[:mid]
        right=alist[mid:]
        mergesort(left)
        mergesort(right)
        merge(left,right,alist)


if __name__=='__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    mergesort(alist)
    print(alist)
