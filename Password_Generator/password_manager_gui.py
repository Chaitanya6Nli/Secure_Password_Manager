from tkinter import *

# STEP 1: Create the main window
root = Tk()                                            # Starts a window 
icon = PhotoImage(file="icons8-password-book-24.png")  # Load the image and create object "icon"     
root.iconphoto(False, icon)                            # Icon of the window
root.title("Password Book")                            # Title of the window
root.geometry("900x700")                               # with x Height in pixels
root.resizable(False, False)                           # Fixed size window

# STEP 2: Add a welcome label
welcome_label = Label(root, text="Welcome to your Password Manager!", font="fixedsys 20 bold")
welcome_label.pack(pady=40)

# STEP 3: Start the main GUI loop
root.mainloop()