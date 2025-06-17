import random

def generate_password(length=12):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''
    for i in range(length):
        password = password + random.choice(characters)
    return password

try:
    user_input = int(input("Enter desired password length (e.g., 8, 12, 16): "))

    if user_input <= 5:
        print("Password length must be a greater than 5. Try again.")
    else:
        generated_password = generate_password(user_input)
        print("Your generated password is:", generated_password)

except ValueError:
    print("Please enter a valid number.")