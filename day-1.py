# insert
arr = [1,2,3,4,5]

# adding value at end in array
arr.append(6)
print(arr)

# specified index
arr.insert(3,7)
print(arr)
# to delete at the end of index
arr.pop(2)

#delete end of array
arr.pop()
print(arr)

arr = [6,7,8,9,0]
i = 1
while i < len(arr): # to print array
 
    print(arr[i])
    i += 1


arr = [ 10,11,12,13] 

# range syntex ( start, end, step  ) 
for i in range( len(arr)):
    print("answer is ",arr[i])

for i in range(2,len(arr)):
    print(arr[i])

for i in range(1,len(arr) ,2):
    print(arr[i])


