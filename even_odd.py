# 2nd is... Given an array count the number of even and odd numbers in it


arr = [1,2,3,4,5,10,13,11,12,14,15,16,19,20,21]

n_even = 0
n_odd = 0

for i in arr:
    if i % 2 == 0:
        n_even +=1
    
    else:
        n_odd += 1
    
print("even is ",n_even)
print("odd is ",n_odd)

