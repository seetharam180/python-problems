#sumof the elements in an array
# arr=[1,2,3,4,5]
# sum=0
# for i in arr:
#     sum+=i
# print(sum)

#find largest element in array
# arr=[1,3,5,3,56,43,89,34]
# max=0
# for i in arr:
#     if max>i:
#         max=max
#     else:
#         max=i
# print(max)

#rotate the elements in an array
# import random
# arr=[1,45,67,89,90,3,43]
# random.shuffle(arr)
# print(arr)


# Write a Python Program to Split the array and add the first part to the end?
def split(arr,k):
    if k<=0 and k>=len(arr):
        return arr
    else:
        first=arr[:k]
        end=arr[k:]
        return end+first
arr=[1,2,3,4,5]
print(split(arr,2))