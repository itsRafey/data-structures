  
# binary search alogrithm  use d when arry is sorted only because it improve time complexity  in sorted arry
flag = False
nums = [1,2,3,4,5,6,7,8,9,10]
target = 11
left = 0
right = len(nums) - 1

while left <= right:
    middle = right - left // 2
    if nums[middle] == target:
        flag = True
        break
    elif nums[middle] < target:
        left = middle + 1
    else:
        right = middle -1    
if flag == True:
    print("found")
else:
    print("not found")
