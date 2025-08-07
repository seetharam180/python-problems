#  Write a Python program to determine whether the given number is a Harshad
#  Number.
#  A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
#  In other words, a number is considered a Harshad number if it can be evenly divided by the
#  sum of its own digits.
#  For example:
#  18 is a Harshad number because 1 +8 =9, 18 is disible by 9


num=int(input("Enter a num:"))
n1=num
sum=0
while n1>0:
    ld=n1%10
    sum+=ld
    n1//=10
if num%sum==0:
    print("Harshad number")
else:
    print("Not a harshad number")
