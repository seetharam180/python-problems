def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiplication")
print("4.divide")
operation=int(input("Enter operation:"))
num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
if operation==1:
    print(add(num1,num2))
elif operation==2:
    print(sub(num1,num2))
elif operation==3:
    print(mul(num1,num2))
elif operation==4:
    print(div(num1,num2))
else:
    print("Enter correct operation")