# pip install tkinter
from tkinter import * 
# pip install pyperclip
import pyperclip  
import random
 
root = Tk()
root.title("REDB1RD PASSWORD GENERATOR")
root.geometry("480x250")
root.configure(bg="black")

passwrd = StringVar()
passlen = IntVar()
passlen.set(0)
 
 
def generate():  # Function to generate the password
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
             '*', '(', ')']
    password = ""
    for x in range(passlen.get()):
        password = password + random.choice(pass1)
    passwrd.set(password)
 
# function to copy the passcode
 
 
def copyclipboard():
    random_password = passwrd.get()
    pyperclip.copy(random_password)
# Labels
 
 
Label(root, text="REDB1RD PASSWORD GENERATOR", font="consolas 15 bold",  bg="black", fg="white").pack()
Label(root, text="by REDB1RD", font="consolas 10 bold", bg="black", fg="white").pack()
Label(root, text="Enter preferred password length", font="consolas 15 bold", bg="black", fg="white").pack(pady=3)
Entry(root, width=30, textvariable=passlen).pack(pady=3)
Button(root, text="Click here to generate password", font="consolas 15 bold",  bg="black", fg="white", command=generate).pack(pady=7)
Entry(root, width=30, textvariable=passwrd).pack(pady=3)
Button(root, text="Copy to clipboard", font="consolas 15 bold", bg="black", fg="white", command=copyclipboard).pack()
root.mainloop()

