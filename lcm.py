greatest=0
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
if num1>num2:
    for i in range(1,num1+1):
        if num1%i==0 and num2%i==0:
            greatest=i
else:
    for i in range(1,num2+1):
        if num1%i==0 and num2%i==0:
            greatest=i
lcm=int((num1*num2)/greatest)
print(f"lcm of ({num1},{num2}) is {lcm}")



# import math
# print(math.gcd(54,24))