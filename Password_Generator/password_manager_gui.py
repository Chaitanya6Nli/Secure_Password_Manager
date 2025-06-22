# Import necessary libraries
import os, random, datetime
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet

# Generate Password
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

# Check password strength
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
    
# Get or generate encryption key
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        print("🔐 Key generated.")
    else:
        print("🔑 Key loaded.")

    with open ("secret.key", "rb") as key_file:
        return key_file.read()
    
# Encrypt password using key
def encrypt_password(password, key):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

# On generate click
def on_generate_click():
    try:
        length_input = password_length_entry.get().strip()
        length = int(length_input) if length_input else 12
        label = purpose_entry.get().strip() or "Unnamed"
        lower = use_lower.get()
        upper = use_upper.get()
        digits = use_digits.get()
        specials = use_specials.get()

        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be positive.")
            return

        password = generate_password(length, lower, upper, digits, specials)
        if password.startswith("Error"):
            messagebox.showwarning("Oops", password)
            return

        strength = check_strength(length, lower, upper, digits, specials)

        messagebox.showinfo(
            "Password Generated",
            f"🔐 Label: {label}\n\nPassword: {password}\n\n💪 Strength: {strength}"
        )

        # Save to file (encrypted)
        key = load_key()
        encrypted = encrypt_password(password, key)

        with open("saved_passwords.txt", "a") as file:
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            file.write(f"\n[{timestamp}]\n")
            file.write(f"Label: {label}\n")
            file.write(f"Encrypted Password: {encrypted}\n")
            file.write(f"Strength: {strength}\n")
            file.write("-" * 40 + "\n")

        messagebox.showinfo("✅ Saved", f"Password saved securely to file.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid number for length.")



# Create the main window
window = Tk()
window.title("Password Book")
icon = PhotoImage(file="icons8-password-book-24.png")
window.iconphoto(False, icon)
window.geometry('900x700')
window.configure(bg='dark slate gray')
window.resizable(False, False)                           # Fixed size window


# Create a frame inside the main window
frame = Frame(bg='dark slate gray')

# Add a welcome label
welcome_label = Label(frame, text="Welcome to your Password Manager!", bg='dark slate gray', fg="azure", font="fixedsys 30 bold")
welcome_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

# ------------------------
# INPUT SECTION
# ------------------------

# Label for service/platform name (like Google, Gmail, Netflix)
purpose_label = Label(frame, text="Enter a label or purpose for this password:", bg='dark slate gray', fg="ivory2", font=("Arial", 16))
purpose_label.grid(row=1, column=0)

purpose_entry = Entry(frame, font=("Arial", 16))
purpose_entry.grid(row=1, column=1, pady=20)

# Label for Password length
password_length_lable = Label(frame, text="Enter desired password length:", bg='dark slate gray', fg="ivory2", font=("Arial", 16))
password_length_lable.grid(row=2, column=0)

password_length_entry = Entry(frame, font=("Arial", 16))
password_length_entry.grid(row=2, column=1, pady=20)

# Checkboxes for character types
use_lower = BooleanVar()
use_upper = BooleanVar()
use_digits = BooleanVar()
use_specials = BooleanVar()

lower_cb = Checkbutton(frame, text="Include lowercase letters", variable=use_lower, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2", selectcolor="blue")
lower_cb.grid(row=3, column=0, columnspan=2, pady=(30, 20), )

upper_cb = Checkbutton(frame, text="Include Uppercase letters", variable=use_upper, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2", selectcolor="blue")
upper_cb.grid(row=4, column=0, columnspan=2, pady=(0, 20))

digits_cb = Checkbutton(frame, text="Include digits", variable=use_digits, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2", selectcolor="blue")
digits_cb.grid(row=5, column=0, columnspan=2, pady=(0, 20))

specials_cb = Checkbutton(frame, text="Include special characters", variable=use_specials, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2", selectcolor="blue")
specials_cb.grid(row=6, column=0, columnspan=2, pady=(0, 30))

# # Button to generate password
generate_btn = Button(frame, text="Generate Password", bg="slate gray", fg="ivory2", font="Arial 16 bold")
generate_btn.grid(row=7, column=0, columnspan=2, pady=30)
generate_btn.config(command=on_generate_click)


# Pack the frame
frame.pack()

# Run the loop
window.mainloop()