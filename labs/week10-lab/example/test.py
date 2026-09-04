
password = input("your password : ")
len = len(password)
check = password.isalnum()
if len>= 8 and check == False:
    print("password is good")
else :
    print("password is not good")