import tkinter

# Create the main window
window = tkinter.Tk()
window.title("Password Book")
icon = tkinter.PhotoImage(file="icons8-password-book-24.png")
window.iconphoto(False, icon)
window.geometry('900x700')
window.configure(bg='dark slate gray')
window.resizable(False, False)                           # Fixed size window


# Create a frame inside the main window
frame = tkinter.Frame(bg='dark slate gray')

# Add a welcome label
welcome_label = tkinter.Label(frame, text="Welcome to your Password Manager!", bg='dark slate gray', fg="azure", font="fixedsys 30 bold")
welcome_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

# ------------------------
# INPUT SECTION
# ------------------------

# Label for service/platform name (like Google, Gmail, Netflix)
purpose_label = tkinter.Label(frame, text="Enter a label or purpose for this password:", bg='dark slate gray', fg="ivory2", font=("Arial", 16))
purpose_label.grid(row=1, column=0)

purpose_entry = tkinter.Entry(frame, font=("Arial", 16))
purpose_entry.grid(row=1, column=1, pady=20)

# Label for Password length
password_length_lable = tkinter.Label(frame, text="Enter desired password length:", bg='dark slate gray', fg="ivory2", font=("Arial", 16))
password_length_lable.grid(row=2, column=0)

password_length_entry = tkinter.Entry(frame, font=("Arial", 16))
password_length_entry.insert(0, "12 (default)")
password_length_entry.grid(row=2, column=1, pady=20)

# Checkboxes for character types
use_lower = tkinter.BooleanVar()
use_upper = tkinter.BooleanVar()
use_digits = tkinter.BooleanVar()
use_specials = tkinter.BooleanVar()

lower_cb = tkinter.Checkbutton(frame, text="Include lowercase letters", variable=use_lower, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2")
lower_cb.grid(row=3, column=0, columnspan=2, pady=(30, 20), )

upper_cb = tkinter.Checkbutton(frame, text="Include Uppercase letters", variable=use_upper, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2")
upper_cb.grid(row=4, column=0, columnspan=2, pady=(0, 20))

digits_cb = tkinter.Checkbutton(frame, text="Include digits", variable=use_digits, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2")
digits_cb.grid(row=5, column=0, columnspan=2, pady=(0, 20))

specials_cb = tkinter.Checkbutton(frame, text="Include special characters", variable=use_specials, width=20, bg="dark slate gray", font=('Helvetica', 12, 'bold'), fg="ivory2")
specials_cb.grid(row=6, column=0, columnspan=2, pady=(0, 30))

# # Button to generate password
generate_btn = tkinter.Button(frame, text="Generate Password", bg="slate gray", fg="ivory2", font="Arial 16 bold")
generate_btn.grid(row=7, column=0, columnspan=2, pady=30)


# Pack the frame
frame.pack()

# Run the loop
window.mainloop()