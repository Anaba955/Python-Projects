from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip  # copies text to clipboard
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password_gen = ''.join(password_list)
    password_input.insert(0, password_gen)
    pyperclip.copy(password_gen)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_name = website_input.get()
    user_email = email_input.get()
    user_password = password_input.get()
    new_data = {
        website_name: {
            "email": user_email,
            "password": user_password,
        }
    }
    if len(website_name) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)  # converts json to dict
                # Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                data = new_data
        finally:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)  # converts dic to json

            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def search_data():
    website_name = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    if website_name in data:
        value = data[website_name]
        messagebox.showinfo(title=website_name, message=f"email: {value['email']}\npassword: {value['password']}")
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website_name} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(row=1, column=0)

website_input = Entry(width=21, highlightthickness=0)
website_input.grid(column=1, row=1)
website_input.focus()

search = Button(text="Search", width=15, highlightthickness=0, command=search_data)
search.grid(column=2, row=1)

email = Label(text="Email/Username:")
email.grid(row=2, column=0)

email_input = Entry(width=40, highlightthickness=0)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "anaba@gmail.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

password_input = Entry(width=21, highlightthickness=0)
password_input.grid(column=1, row=3)

button = Button(text="Generate password", width=15, highlightthickness=0, command=gen_password)
button.grid(column=2, row=3)

add_button = Button(text="Add", width=26, highlightthickness=0, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
