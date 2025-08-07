#  Write a Python program to check if the given number is Happy Number.
#  Happy Number: A Happy Number is a positive integer that, when you repeatedly replace
#  the number by the sum of the squares of its digits and continue the process, eventually
#  reaches 1. If the process never reaches 1 but instead loops endlessly in a cycle, the number
#  is not a Happy Number.
#  For example:
#  19 is a Happy Number because:

# num=int(input("Enter a num:"))
# li=[]
# while num!=1 and num not in li:
#     li.append(num)
#     sum=0
#     while num>0:
#         ld=num%10
#         sum=sum+(ld**2)
#         num//=10
#     num=sum
# print(li)
# if num==1:
#     print("Happy number")
# else:
#     print("Not a happy number")

def happy_num(num):
    li=[]
    while num!=1 and num not in li:
        li.append(num)
        sum=0
        while num>0:
            ld=num%10
            sum=sum+(ld**2)
            num//=10
        num=sum
    if num==1:
        return True
happy_numbers=[num for num in range(100) if happy_num(num)]
print(happy_numbers)