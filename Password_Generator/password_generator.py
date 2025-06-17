import random, datetime, base64

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

def check_strength(length, use_lower, use_upper, use_digits, use_specials):
    score = 0

    # Add points for character variety
    score = score + use_lower + use_upper + use_digits + use_specials

    if length >= 12:
        score = score + 1

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else:
        return "Strong"

# Get user inputs
try:
    # Get password length
    length = int(input("Enter desired password length (e.g., 8, 12, 16): "))
    if length <= 0:
        print("Password length must be positive. Try again.")
        exit()

    # Ask user for label/tag
    label = input("Enter a label or purpose for this password (e.g., Gmail, Netflix): ").strip()

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
        strength = check_strength(length, lower, upper, digits, specials)
        print(f"💪 Password Strength: {strength}")

        # Save to file
        with open("saved_passwords.txt", "a") as file:
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file.write(f"\n[{timestamp}]\n")
            file.write(f"Label: {label}\n")
            # Encode the password before saving
            encoded_password = base64.b64encode(password.encode()).decode()
            file.write(f"Encoded Password: {encoded_password}\n")
            file.write(f"Included - Lowercase: {lower}, Uppercase: {upper}, Digits: {digits}, Special Characters: {specials}\n")
            file.write("-" * 40 + "\n")

        print("✅ Password saved to 'saved_passwords.txt")

except ValueError:
    print("Please enter a valid number.")