import random

def generate_password(length=12):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    password = ''
    for i in range(length):
        password = password + random.choice(characters)
    return password

print("Your generated password is:", generate_password())