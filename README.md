# 🔐 Secure Password Manager

This is a simple and secure Password Manager built with Python. It includes both a **GUI (Graphical User Interface)** and a **CLI (Command Line Interface)** version.

---

## 📌 Features

* ✅ Generate strong passwords
* ✅ Choose password length and character types
* ✅ Check password strength
* ✅ Save passwords with encryption (Fernet)
* ✅ View and decrypt saved passwords
* ✅ Use either GUI or CLI

---

## 📂 Project Structure

```
SECURE_PASSWORD_MANAGER/
├── password_manager_gui.py       # GUI interface
├── password_manager_cli.py       # CLI version
├── view_passwords_cli.py         # View passwords in CLI
├── decrypt_passwords_cli.py      # Decrypt tool for CLI
├── icons8-password-book-24.png   # GUI icon
├── .gitignore                    # Ignore sensitive files
├── README.md                     # This file
```

---

## 🔧 Setup Instructions

### Step 1: Install Dependencies

```bash
pip install cryptography
```

### Step 2: Run the GUI version

```bash
python password_manager_gui.py
```

### Step 3: Run the CLI version

```bash
python password_manager_cli.py
```

---

## 💡 How It Works

### Generate Password

You enter options like:

* Length
* Include lowercase, uppercase, digits, or special characters

The program creates a random password using your choices.

### Check Strength

Then, it checks if the password is weak, medium, or strong.

### Save Securely

Next, it encrypts the password using **Fernet** from the `cryptography` library.

After that, it saves it to a file named `saved_passwords.txt` with timestamp and label.

### View Passwords

Finally, you can view all saved passwords using a button in the GUI or a script in CLI.

---

## ⚠️ Security Note

This project uses **Fernet encryption** to protect your saved passwords.

Files like `secret.key` and `saved_passwords.txt` are excluded from version control using `.gitignore`.

> Do not share your `secret.key` with anyone. If you lose it, saved passwords cannot be decrypted.

---

## 💼 Ideal For:

* Python beginners who want a real-world project
* Students looking to learn encryption and GUI
* Anyone who wants a simple password manager

---

## ⭐ GitHub Ready

This project was built using proper Git practices:

* Every feature added on a new branch
* Meaningful commit messages
* Clean merge history

