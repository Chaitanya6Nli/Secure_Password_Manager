import random

def generate_password(length=12, use_special_chars=True):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    specials = '!@#$%^&*()'

    # Build character set based on user input
    if use_special_chars:
        characters = letters + digits + specials
    else:
        characters = letters + digits

    password = ''
    for i in range(length):
        password = password + random.choice(characters)
    return password

try:
    # Get password length
    user_input = int(input("Enter desired password length (e.g., 8, 12, 16): "))

    if user_input <= 0:
        print("Password length must be a positive number. Try again.")
    else:
        # Ask if special characters should be included
        special_choice = input("Include special characters? (Y/N): ").strip().lower() # trims space, converts to lowercase

        if special_choice == 'y':
            use_specials = True
        elif special_choice == 'n':
            use_specials = False
        else:
            print("Invalid input. Please enter Y or N.")
            exit() # stop execution if invalid input
        
        # Generate and show password
        generated_password = generate_password(user_input, use_specials)
        print("Your generated password is:", generated_password)

except ValueError:
    print("Please enter a valid number.")