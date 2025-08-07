#  Write a Python program to check if the given number is a Disarium Number.

#  A Disarium number is a number that is equal to the sum of its digits each raised to the
#  power of its respective position. For example, 89 is a Disarium number because 8**1+9**2=8+81=89

# num=int(input("Enter a number:"))
# n1=num
# n2=num
# count=0
# while n1>0:
#     count+=1
#     n1//=10
# sum=0
# while n2>0:
#     ld=n2%10
#     sum=sum+(ld**count)
#     count-=1
#     n2//=10
# if sum==num:
#     print("Disarium number")
# else:
#     print("Not a Disarium number")


def disarium_num(num):
    n1=num
    n2=num
    count=0
    while n1>0:
        count+=1
        n1//=10
    sum=0
    while n2>0:
        ld=n2%10
        sum=sum+(ld**count)
        count-=1
        n2//=10
    if sum==num:
        return True
disarium_numbers=[num for num in range(1,1000) if disarium_num(num)]
print(disarium_numbers)