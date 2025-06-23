# Import necessary libraries
import os, random, datetime
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet

# ------------------------
# FUNCTION DEFINITIONS
# ------------------------

# Generate password based on user options
def generate_password(length, use_lower, use_upper, use_digits, use_specials):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    specials = '!@#$%^&*()'

    character_set = ''
    if use_lower: character_set += lowercase
    if use_upper: character_set += uppercase
    if use_digits: character_set += digits
    if use_specials: character_set += specials

    if not character_set:
        return "Error: No character sets selected. Cannot generate password."

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

# Check password strength
def check_strength(length, use_lower, use_upper, use_digits, use_specials):
    score = use_lower + use_upper + use_digits + use_specials
    if length >= 12:
        score += 1

    if score <= 2:
        return "Weak"
    elif score in (3, 4):
        return "Medium"
    else:
        return "Strong"

# Load or create encryption key
def load_key():
    key_path = "secret.key"

    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        print("🔐 Key generated.")
        return key
    else:
        with open(key_path, "rb") as key_file:
            key = key_file.read()

        # ✅ Verify it's a valid Fernet key
        try:
            Fernet(key)  # This will raise ValueError if invalid
            print("🔑 Valid key loaded.")
            return key
        except ValueError:
            print("❌ Invalid key detected. Regenerating...")
            key = Fernet.generate_key()
            with open(key_path, "wb") as key_file:
                key_file.write(key)
            print("🔐 New key generated.")
            return key

# Encrypt the password
def encrypt_password(password, key):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

# Button click logic
def on_generate_click():
    length_input = password_length_entry.get().strip()
    label = purpose_entry.get().strip() or "Unnamed"
    lower = use_lower.get()
    upper = use_upper.get()
    digits = use_digits.get()
    specials = use_specials.get()

    # Handle default or invalid input safely
    if length_input == "":
        length = 12
    elif length_input.isdigit():
        length = int(length_input)
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive number.")
            return
    else:
        messagebox.showerror("Invalid Input", "Enter a valid number for length.")
        return

    # Generate the password
    password = generate_password(length, lower, upper, digits, specials)
    if password.startswith("Error"):
        messagebox.showwarning("Oops", password)
        return

    strength = check_strength(length, lower, upper, digits, specials)

    # Show result popup
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

    messagebox.showinfo("✅ Saved", "Password saved securely to file.")  

# ------------------------
# GUI LAYOUT
# ------------------------

# Create main window
window = Tk()
window.title("Password Book")
icon = PhotoImage(file="icons8-password-book-24.png")
window.iconphoto(False, icon)
window.geometry('900x700')
window.configure(bg='dark slate gray')
window.resizable(False, False)

# Create main frame
frame = Frame(bg='dark slate gray')

# Welcome text
welcome_label = Label(frame, text="Welcome to your Password Manager!", bg='dark slate gray', fg="azure", font="fixedsys 30 bold")
welcome_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

# Label entry
purpose_label = Label(frame, text="Enter a label or purpose for this password:", bg='dark slate gray', fg="ivory2", font=("Arial", 16))
purpose_label.grid(row=1, column=0)

purpose_entry = Entry(frame, font=("Arial", 16))
purpose_entry.grid(row=1, column=1, pady=20)

# Length entry
password_length_label = Label(frame, text="Enter desired password length:", bg='dark slate gray', fg="ivory2", font=("Arial", 16))
password_length_label.grid(row=2, column=0)

password_length_entry = Entry(frame, font=("Arial", 16))
password_length_entry.grid(row=2, column=1, pady=20)

# Optional placeholder label (recommended)
default_note = Label(frame, text="*Default is 12 if left empty", bg='dark slate gray', fg="gray80", font=("Arial", 10))
default_note.grid(row=3, column=1, sticky='w')

# Character set checkboxes
use_lower = BooleanVar()
use_upper = BooleanVar()
use_digits = BooleanVar()
use_specials = BooleanVar()

Checkbutton(frame, text="Include lowercase letters", variable=use_lower, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2", selectcolor="blue").grid(row=4, column=0, columnspan=2, pady=(30, 20))
Checkbutton(frame, text="Include Uppercase letters", variable=use_upper, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2", selectcolor="blue").grid(row=5, column=0, columnspan=2, pady=(0, 20))
Checkbutton(frame, text="Include digits", variable=use_digits, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2", selectcolor="blue").grid(row=6, column=0, columnspan=2, pady=(0, 20))
Checkbutton(frame, text="Include special characters", variable=use_specials, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2", selectcolor="blue").grid(row=7, column=0, columnspan=2, pady=(0, 30))

# Generate button
generate_btn = Button(frame, text="Generate Password", bg="slate gray", fg="ivory2", font="Arial 16 bold", command=on_generate_click)
generate_btn.grid(row=8, column=0, columnspan=2, pady=30)

# Pack the frame
frame.pack()

# Start the app
window.mainloop()
