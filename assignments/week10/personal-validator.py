"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), isspace() ,upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name:")
age = int(input("Enter your age:"))
phone = input("Enter your phone number:")

print("Validation Results:")

check_name = False
for i in name:
    if i.isalpha() or i.isspace():
        check_name =True
    else :
        check_name = False 
        break


check_age = False
if age >= 18 and age <=65 :
    check_age = True

check_phone=False
if phone.isdigit() and len(phone) ==10 :
    check_phone = True

if check_name:
    print("Valid (contains only letters and spaces)")
else :
    print("name invalid")
if check_age :
    print(f"Age: Valid ({age} years old)")
else:
    print("age invalid")
if check_phone:
    print("Valid (10-digit number)")
else:
    print("phone invalid")


if check_name and check_age and check_phone:
    print("Formatted Information:")
    print("name:",name.upper())
    print("age:",age)
    print("phone",phone)