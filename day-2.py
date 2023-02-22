#  find the sum off array

 # using for loop


# for i in sum(arr[i]):
#     print(arr[i])
#     i += 1

arr = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in range(len(arr)):
    sum += arr[i]
    print("sum using for loop ",sum)





arr = [1,2,3,4,5]
sum = 0
i = 0
while i < len(arr):   
    sum += arr[i]
    i += 1
    
    print(" sum using while loop ", sum)
