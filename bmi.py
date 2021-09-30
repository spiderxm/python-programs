print("Enter your weight in kgs")
wt=float(input())
print("Enter your height in metres")
ht=float(input())
bmi=wt/(ht*ht)
print("Your BMI is ", bmi)
if bmi>24.9:
    print("You fall in overweight category")
elif bmi<18.5:
    print("You fall in underweight category")
else:
    print("You fall in normal category")