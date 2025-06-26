n=int(input("enter number:"))
#count=0
# for i in range(2,n):
#     if (n%i==0):
#         count=count+1
# if(count==0):
#     print("prime")
# else:
#     print("not prime")




# for i in range(2,n):
#     count=0
#     for j in range(2,i):
#         if (i%j==0):
#             count+=1
#     if (count==0):
#         print(i)

count=0
i=2
while(i<n):
    if(n%i==0):
        count+=1
    i+=1
if(count==0):
    print("prime")
else:
    print("not prime")