import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import END
import password_generator as pass_gen


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    password_input.insert(0, pass_gen.generate_password())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    login = login_input.get()
    password = password_input.get()

    if website == "" or password == "":
        msgbox.showerror(title="Oops!", message="Please do not leave any fields empty.")
    else:
        is_continue_to_save = msgbox.askokcancel(title=website, message=f"These are the entered details:"
                                                                        f"\nLogin: {login}\nPassword: {password}"
                                                                        f"\nIs it okay to save?")
        if is_continue_to_save:
            with open("data.txt", "a") as file:
                file.write(f"\n{website} | {login} | {password}")
                website_input.delete(0, END)
                login_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = tk.Entry(width=35)
website_input.grid(column=1, columnspan=2, row=1, sticky="EW")

login_label = tk.Label(text="Email/Username:")
login_label.grid(column=0, row=2)
login_input = tk.Entry(width=35)
login_input.insert(0, "example@gmail.com")
login_input.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = tk.Entry(width=21)
password_input.grid(column=1, row=3, sticky="EW")

create_password_bn = tk.Button(text="Generate Password", command=create_password)
create_password_bn.grid(column=2, row=3, sticky="EW")

add_bn = tk.Button(text="Add", command=save_password, width=36)
add_bn.grid(column=1, columnspan=2, row=4, sticky="EW")

window.mainloop()
