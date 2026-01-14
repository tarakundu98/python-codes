user_name = input("Enter your username: ")
if len(user_name) < 12:
    print("Username must be atleast 12 characters long.")
elif user_name.count(" ")>0:
    print("Username must not contain any space.")
elif user_name.isdigit():
    print("Username must contain no digits.")
else:
    print("Username is valid.")
