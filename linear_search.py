# linear serach alogrithem we used when arry is unsorted 

flag = False
nums = [1,2,3,4,5,6,7,8,9,10]
target = 11

for index , number in enumerate(nums):
    if number == target:
        flag = True
        break

if flag == True:
    print("found")
else:
    print ("-1")