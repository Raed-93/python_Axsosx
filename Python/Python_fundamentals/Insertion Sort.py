def Insertion_Sort(arr):
    for i in range(1,len(arr)):
        j = i
        
        while j > 0 and arr[j-1] > arr[j]:
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -=1
            
arr =[8,5,2,3,-1,7]
Insertion_Sort(arr)
print(arr)

