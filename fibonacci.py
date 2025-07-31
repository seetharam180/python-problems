# n=int(input("enter number:"))
# a=0
# b=1
# for i in range(1,n+1):
#     print(a)
#     a,b=b,a+b

def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
terms=int(input("Enter number greater than 0:"))
if terms<=0:
    print("Enter a positive number:")
else:
    for i in range(terms):
        print(fib(i))

