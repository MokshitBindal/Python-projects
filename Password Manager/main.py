from tkinter import *
from tkinter import messagebox
import my_pass_gen
import pyperclip
import json
# messagebox is another module in tkinter thus it is not imported using *
# as only classes, constants and functions are imported.

# ---------------------------------- SEARCH-------------------------------------- #


def search_data():
    website = website_box.get()

    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="Error", message=f"No data file exists, start by entering the data.")
    else:
        if website != "":
            if website in data.keys():
                email = data[website]["email"]
                password = data[website]["password"]

                messagebox.showinfo(title = "Website found",
                                    message = f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(
                    title="Website Not Found", message=f"No data related to {website} was found")
        else:
            messagebox.showinfo(
                title="Website Not Entered", message=f"Enter a Website to search")

    # if website != "":
    #     try:
            # with open("data.json", 'r') as data_file:
            #     data = json.load(data_file)
                # if website in data.keys():
                #     email = data[website]["email"]
                #     password = data[website]["password"]

                #     messagebox.showinfo(title = "Website found",
                #                         message = f"Email: {email}\nPassword: {password}")
    #             else:
    #                 messagebox.showinfo(
    #                     title="Website Not Found", message=f"No data related to {website} was found")
    #     except FileNotFoundError:
    #         messagebox.showinfo(
    #             title="Error", message=f"No data file exists, start by entering the data.")
    # else:
    #     messagebox.showinfo(
    #         title="Website Not Entered", message=f"Enter a Website to search")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def new_pass():
    generated_pass = my_pass_gen.generate_pass()
    # print(generated_pass)
    password_box.delete(0, END)
    password_box.insert(0, generated_pass)
    pyperclip.copy(generated_pass)
    messagebox.showinfo(
        title="Password Generated", message="Your password has been generated and copied to your clipboard")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_data():
    website = website_box.get().strip(" ") # To remove difference between name+space rather than name only
    email = id_box.get()
    password = password_box.get()
    new_data = {
        website: {
        "email": email,
        "password": password,
        }
    }

    if website != "" and password != "" and email != "":
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail- {email} "
                                       f"\nPassword- {password} \nIs it ok to save?")
        if is_ok:
            # with open("passwords.txt", 'a') as f:
            #     f.write(f"{website} | {email} | {password} \n")
            # website_box.delete(0, END)  # variable in tk for end index
            # password_box.delete(0, END)  # clears the text box from start to end

            # try:
            #     with open("data.json", 'r') as data_file:
            #         data = json.load(data_file)
            #         # print(data) #Type = dictionary
            #         data.update(new_data)

            #     with open("data.json", 'w') as data_file:  # write to Json
            #         json.dump(data, data_file, indent=4) #saving updated data

            #         website_box.delete(0, END)
            #         password_box.delete(0, END)

            # except FileNotFoundError:
            #     with open("data.json", 'w') as data_file:
            #         json.dump(new_data, data_file, indent=4)

            #     website_box.delete(0, END)
            #     password_box.delete(0, END)

            try:
                with open("data.json", 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", 'w') as data_file:  # write to Json
                    json.dump(data, data_file, indent=4)  # saving updated data
            finally:
                website_box.delete(0, END)
                password_box.delete(0, END)

    else:
        messagebox.showinfo(
            title="Error", message="Please don't leave any fields blank")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_box = Entry(width=29)
website_box.grid(row=1, column=1)
website_box.focus()  # puts cursor on it at start of app

id_label = Label(text="Email/Username:")
id_label.grid(row=2, column=0)
id_box = Entry(width=50)
id_box.grid(row=2, column=1, columnspan=2)
id_box.insert(0, "mygmailid@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_box = Entry(width=29)
password_box.grid(row=3, column=1)

generate_button = Button(text="Generate password", command=new_pass)
generate_button.grid(row=3, column=2)

search_button = Button(text="Search", command=search_data, width=16)
search_button.grid(row=1, column=2)

add_button = Button(text="Add", width=47, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
