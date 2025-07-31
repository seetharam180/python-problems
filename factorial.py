# #Write a Python Program to Find the Factorial of a Number.
# num=int(input("Enter a num:"))
# factorial=1
# if num<0:
#     print("factorial doesn't exist.")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         factorial*=i
#     print(f"factorial of {num}={factorial}")


def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
num=int(input("Enter a num:"))
if num<0:
    print("sorry,factorial doesn't exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print(f"The factorial of a given number is {fact(num)}")

