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
        

