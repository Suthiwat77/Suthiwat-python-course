# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
""" if age >= 60 :
    print("senior")
elif age >= 59 :
    print("adult")
elif age >= 20 :
    print("adult")
elif age >= 12 :
    print("child")
else :
    print("none") """

# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        withdraw = 0
        deposit = 0
        if choice == "1":
            print("balance",balance)
        elif choice == "2" :
            withdraw = int(input("withdraw :"))
        elif choice == "3 ":
            Deposit = int(input("deposit :"))
        elif choice == "4" :
            break 

        balance = Deposit + balance 
        balance = balance - withdraw

else:
    print("Invalid PIN") 
