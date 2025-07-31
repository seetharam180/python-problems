# num=int(input("Enter a num:"))
# n=num
# n1=num
# power=0
# while n1>0:
#     power+=1
#     n1//=10
# sum=0
# while n>0:
#     lastdigit=n%10
#     sum+=lastdigit**power
#     n//=10
# if sum==num:
#     print(f"{num} is a armstrong number")
# else:
#     print(f"{num} is not a armstrong number")


#print armstrong numbers in an interval
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))
# for i in range(num1,num2+1):
#     n=i
#     n1=i
#     power=0
#     while n1>0:
#         power+=1
#         n1//=10
#     sum=0
#     while n>0:
#         lastdigit=n%10
#         sum+=lastdigit**power
#         n//=10
#     if sum==i:
#         print(i)

#Find Armstrong Number in an Interval. print in list
def arm_strong(num):
    n=num
    n1=num
    power=0
    while n1>0:
        power+=1
        n1//=10
    sum=0
    while n>0:
        lastdigit=n%10
        sum+=lastdigit**power
        n//=10
    if sum==num:
        return num
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
arm_strongnumbers=[num for num in range(num1,num2+1) if arm_strong(num)]
print(arm_strongnumbers)