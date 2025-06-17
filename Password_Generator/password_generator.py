import random

def generate_password(length, use_lower, use_upper, use_digits, use_specials):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    specials = '!@#$%^&*()'

    # Build character set based on user input
    character_set = ''
    
    if use_lower:
        character_set = character_set + lowercase
    if use_upper:
        character_set = character_set + uppercase
    if use_digits:
        character_set = character_set + digits
    if use_specials:
        character_set = character_set + specials

    if not character_set:
        return "Error: No character sets selected. Cannot generate password."

    password = ''
    for i in range(length):
        password = password + random.choice(character_set)
    return password

# Get user inputs
try:
    # Get password length
    length = int(input("Enter desired password length (e.g., 8, 12, 16): "))
    if length <= 0:
        print("Password length must be positive. Try again.")
        exit()

    # Collect options from user
    lower = input("Include lowercase letters? (Y/N): ").strip().lower() == 'y'
    upper = input("Include uppercase letters? (Y/N): ").strip().lower() == 'y'
    digits = input("Include digits? (Y/N): ").strip().lower() == 'y'
    specials = input("Include special characters? (Y/N): ").strip().lower() == 'y'

    # Generate and display password
    password = generate_password(length, lower, upper, digits, specials)
    if password.startswith("Error"):
        print(password) # just show the error message
    else:
        print("Your generated password is:", password)

except ValueError:
    print("Please enter a valid number.")