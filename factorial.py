#Write a Python Program to Find the Factorial of a Number.
num=int(input("Enter a num:"))
factorial=1
if num<0:
    print("factorial doesn't exist.")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial*=i
    print(f"factorial of {num}={factorial}")


