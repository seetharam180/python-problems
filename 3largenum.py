# third largest number in an array
arr=[23,78,90,45,34,24]
max1=0
max2=0
for i in arr:
    if max1<i:
        max1,max2,max3=i,max1,max2
    elif max1>i:
        if max2>i and max3<i:
            max3=i
print(max1,max2,max3)