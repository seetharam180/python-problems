# Write a Python Program to calculate your Body Mass Index
w=int(input("Enter weight in kgs:"))
h=int(input("Enter height in m:"))
bmi=w/(h*h)
print(f"BMI is {bmi}")
if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
     print("Your weight is normal.")
elif 25 < bmi <= 29.29:
     print("You are overweight.")
else:
     print("You are obese.")

