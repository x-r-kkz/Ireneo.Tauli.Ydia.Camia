# INPUT STAGE:

user = str(input("Please create a username(5-10 characters): "))

# DATA PROCESSING AND VALIDATION
if 5 <= len(user) <= 10 and user.strip() and user.isalnum():
    print("Your username is valid, Thank you for your time!")
else:
    print("Your username is invalid, Make sure your username has no special characters and is 5-10 characters!")
