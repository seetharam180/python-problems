#Write a Python Program to Check if a Number is Odd or Even.
n=int(input("enter number:"))
# if(n%2==0):
#     print("even number")
# else:
#     print("odd number")
if (n & 1==0):
    print("even number")
else:
    print("odd number")

