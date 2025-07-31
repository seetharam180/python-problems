#Write a Python Program to Check Leap Year
year=int(input("Enter Year:"))
if year%4==0 and (year%100!=0 or year%400==0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")