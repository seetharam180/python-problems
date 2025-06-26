li=[32,67,89,12,98,65,55,43]
# li1=li.sort()
# max=li[-1]
# min=li[0]
# print(max)
# print(min)

#max 1st and 2nd
# max=0
# smax=0
# for i in range(0,len(li)):
#     if (max>li[i]):
#         max=max
#     else:
#         smax=max
#         max=li[i]
# print(max)
# print(smax)

#min value
min=li[0]
for i in range(0,len(li)):
    if (min<li[i]):
        min=min
    else:
        min=li[i]
print(min)