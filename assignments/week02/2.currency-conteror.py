""" Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used """

print("======What do you want======")
print("1.Convert Thai currency to US dollars.")
print("2.Convert US dollars  to Thai currency.")
user = int(input("Number is "))

if user == 1 :
    a = float(input("your money is (THB): "))
    b = a / 35.5 
    print(f"your money USD is :{b:.2f}")
elif user == 2:
    c = float(input("your money is (USD): "))
    d = 35.5 * c
    print(f"your money THB is :{d:.2f}")



