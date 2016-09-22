#Python program for Insertion sort

def insertion_sort(arr):
    for i in range (1,len(arr)):
        j=i-1
        key=arr[i]
        while (key<arr[j] and j>=0):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

if __name__=="__main__":
    list1=[5,6,11,12,13]
    print insertion_sort(list1)
