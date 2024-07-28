x = [9,1,2,6,4,7,3,5,8]

for i in range(len(x)-1):
    
    mini = i
    for r in range(i+1,len(x)):
        if x[mini] > x[r]:
            mini = r
    x[i],x[mini] = x[mini],x[i]
    
print("Sorting Array")
for i in range(len(x)):
    print(x[i],end=" ")
    

# def Sorting(arr):
#     for i in range(len(arr)-1):
#         mini_value = i
        
#         for x in range(i+1,len(arr)):
#             if arr[mini_value] > arr[x]:
#                 mini_value = x
#                 arr[mini_value],arr[i] = arr[i],arr[mini_value]
                
# arr=[8,5,2,3,-1,7]
# Sorting(arr)
# print(arr)
        

