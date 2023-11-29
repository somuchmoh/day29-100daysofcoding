import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # From Day 5 - Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pwd_l = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pwd_s = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pwd_n = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = pwd_n + pwd_s + pwd_l
    random.shuffle(password_list)
    new_password = "".join(password_list)
    password_input.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_entry = website_input.get()
    email_entry = email_input.get()
    password_entry = password_input.get()
    new_data = {
        website_entry: {
            "email": email_entry,
            "password": password_entry,
        }
    }

    if len(website_entry) == 0 or len(password_entry) == 0:
        messagebox.showinfo(title="Error", message="Please do not leave any field empty!")
    else:
        try:
            f = open("passwords.json", mode="r")
        except FileNotFoundError:
            with open("passwords.json", mode="w") as f:
                # Writing the new data to the JSON file
                json.dump(new_data, f, indent=4)
        else:
            # Read JSON File
            data = json.load(f)
            # Update JSON File
            data.update(new_data)
            with open("passwords.json", mode="w") as f:
                # Writing the new data to the JSON file
                json.dump(data, f, indent=4)
        finally:
            website_input.delete(0, len(website_entry))
            password_input.delete(0, len(password_entry))


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    web_entry = website_input.get()
    try:
        with open("passwords.json", mode="r") as data_file:
            content = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No File Found")
    else:
        entry = {key: value for key, value in content.items() if key == web_entry}
        if bool(entry):
            messagebox.showinfo(title=web_entry, message=f"email: {content[web_entry]['email']} \n password: "
                                                   f"{content[web_entry]['password']}")
        else:
            messagebox.showinfo(title="Error", message="Website not found")



# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
image = tkinter.PhotoImage(file="padlock.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=2)

website = tkinter.Label()
website.config(text="Website:", font=("Arial", 14))
website.grid(row=1, column=1)

website_input = tkinter.Entry()
website_input.focus()
website_input.config(width=20, highlightthickness=0)
website_input.grid(row=1, column=2)

search_button = tkinter.Button()
search_button.config(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=3)

email = tkinter.Label()
email.config(text="Email/Username:", font=("Arial", 14))
email.grid(row=2, column=1)

email_input = tkinter.Entry()
email_input.insert(0, "mohanasindhuri@gmail.com")
email_input.config(width=35, highlightthickness=0)
email_input.grid(row=2, column=2, columnspan=2)

password = tkinter.Label()
password.config(text="Password:", font=("Arial", 14))
password.grid(row=3, column=1)

password_input = tkinter.Entry()
password_input.config(width=20, highlightthickness=0)
password_input.grid(row=3, column=2)

password_button = tkinter.Button()
password_button.config(text="Generate", width=10, command=generate_password)
password_button.grid(row=3, column=3)

add_button = tkinter.Button()
add_button.config(text="Add", width=33, command=save)
add_button.grid(row=4, column=2, columnspan=2)


window.mainloop()
