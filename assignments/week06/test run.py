def create_user_profile(username, age=18, premium=False):
    # Your Problem 3 solution
    if premium == False:
        return f"{username} (age: {age}) - premium user"
    else:
        return f"{username} (age: {age}) - standard User"

print(create_user_profile("Suthiwat",19))
print(create_user_profile("Talay"))
print(create_user_profile("Lay",77,False))
