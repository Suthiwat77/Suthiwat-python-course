""" BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below """

k = float(input("How much do you weigh? (gk)"))
m = float(input("How much do you height? (m)"))

bmi = k / (m**2)

print(f"bmi is {bmi:.1f}")

if bmi <=18.5 :
    print("you Underweight")
elif bmi >=18.6 and bmi <= 24.9 :
    print("you Normal weight")
elif bmi >=25.0 and bmi <=29.9 :
    print("you Overweight")
elif bmi >30.0 :
    print("you Obese")

