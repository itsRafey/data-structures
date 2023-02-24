arr = [-3,-2,-1,0,1,2,]

pos = 0
neg = 0

for index in arr:
    if  index > 0:
        pos += 1
    elif index < 0:
        neg +=1
print (max(pos , neg))