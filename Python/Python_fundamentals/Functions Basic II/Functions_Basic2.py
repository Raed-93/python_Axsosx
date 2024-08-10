
# def countDown(n):
#    new=[]
#    for x in range (n,-1,-1) :
#       new.append(x)
#    return new
# print(countDown(5))



# def print_and_return(n1):
#      print(n1[0])
#      return n1[1]
# print(print_and_return([1,3]))


# def first_plus_length(list):
#      x=(list[0]+len(list))
    
#      return x
# print(first_plus_length([1,2,3,4,5]))


arr=[]
def greater_than_secound(array):
   if len(array) < 2 :
            return False
    
   for x in range (0, len(array) ,1):
    if array[x]> array[1] and len(array)>=2:
        arr.append(array[x])
       
        y= len(arr)
        print(y)
   return arr
print(greater_than_secound([5,4,4]))


# def length_and_value(size,value):
#    list = []
#    for i in range(size):
#        list.append(value)
#    return list
# print(length_and_value(6,2))


