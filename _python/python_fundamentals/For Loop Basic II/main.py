# 1
# def biggie_size(biggie):
   
#     for i in range(0,len(biggie)):
#         if  biggie[i] > 0 :
#          biggie[i]="big"

#     return biggie
# print(biggie_size([-1,3,5,-5]))

# 2

# def count_positives(num):
#     count =0
#     for i in range (len(num)):
#         if num[i] > 0:
#             count+=1
#     last_index = len(num)-1
#     num[last_index] = count
#     return num
# print(count_positives([-1,1,1,1]))

# 3

# def sum_total(num):
#     sum = 0
#     for i in range (len(num)):
#         sum +=num[i]
#     return sum
# print(sum_total([1,2,3,4]))

# 4

# def average(num):
#     sum = 0
#     for i in range (len(num)):
#         sum +=num[i]
#     return sum / len(num)
# print(average([1,2,3,4]))

# 5

# def length(num):
#     return len(num)    
# print(length([]))

# 6

# def minimum(num):
#     if len(num) == 0:
#             return False
#     else:
#         mini = num[0]
#     for i in range(len(num)):
#          if num[i] < mini:
#               mini = num[i]
#     return mini
# print(minimum([-1,2,3,-1,-9,5,100,20,-2,-200]))

# 7

# def maximum(num):
#     if len(num) == 0:
#         return False
#     else:
#      maxi = num[0]
#     for i in range (len(num)):
#        if num[i] > maxi:
#           maxi = num[i]
#     return maxi
# print(maximum([9,5,101,200]))

#8

# def ultimate_analysis(num):
#     sum = sum_total(num)
#     avge = average(num)
#     min = minimum(num)
#     max = maximum(num)
#     leng = length(num)
#     Analysis = {
#         'sumTotal' : sum,
#         'average' : avge,
#         'minimum' : min,
#         'maximum' : max,
#         'length' : leng

#     }
#     return Analysis


# def sum_total(num):
#     sum = 0
#     for i in range (len(num)):
#         sum +=num[i]
#     return sum

# def average(num):
#     sum = 0
#     for i in range (len(num)):
#         sum +=num[i]
#     return sum / len(num)

# def minimum(num):
#     if len(num) == 0:
#             return False
#     else:
#         mini = num[0]
#     for i in range(len(num)):
#          if num[i] < mini:
#               mini = num[i]
#     return mini

# def maximum(num):
#     if len(num) == 0:
#         return False
#     else:
#      maxi = num[0]
#     for i in range (len(num)):
#        if num[i] > maxi:
#           maxi = num[i]
#     return maxi

# def length(num):
#     return len(num) 
 

# print(ultimate_analysis([37,2,1,-9]))

#9

def reverse_list(num):
    x = len(num)
    for i in range (int(x / 2)):
        temp = num[x -1 -i]
        num[x -1 -i] = num[i]
        num[i] = temp
    return num
print(reverse_list([3,2,5,9,7]))