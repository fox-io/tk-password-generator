"""
tk-password-generator

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
import tkinter
import json


class PasswordGenerator:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Password Generator")
        self.window.config(padx=50, pady=50)

        self.padlock_image = tkinter.PhotoImage(file="./logo.png")
        self.image_frame = tkinter.Canvas(width=200, height=200, highlightthickness=0)
        self.image_frame.create_image(100, 100, image=self.padlock_image)
        self.image_frame.grid(column=1, row=0)

        self.website_label = tkinter.Label(text="Website:")
        self.website_label.grid(column=0, row=1, sticky=tkinter.E)
        self.username_label = tkinter.Label(text="Email/Username:")
        self.username_label.grid(column=0, row=2, sticky=tkinter.E)
        self.password_label = tkinter.Label(text="Password:")
        self.password_label.grid(column=0, row=3, sticky=tkinter.E)

        self.website_entry = tkinter.Entry(width=51)
        self.website_entry.grid(column=1, row=1, columnspan=2, sticky=tkinter.W)
        self.website_entry.focus()
        self.username_entry = tkinter.Entry(width=51)
        self.username_entry.grid(column=1, row=2, columnspan=2, sticky=tkinter.W)
        self.password_entry = tkinter.Entry(width=32)
        self.password_entry.grid(column=1, row=3, sticky=tkinter.W)

        self.generate_button = tkinter.Button(text="Generate Password")
        self.generate_button.grid(column=2, row=3, sticky=tkinter.W)

        self.add_button = tkinter.Button(text="Add", width=43, command=self.add_entry)
        self.add_button.grid(column=1, row=4, columnspan=2, sticky=tkinter.W)

    def add_entry(self):
        # Create a dict using input data
        form_data = {
            "website": self.website_entry.get(),
            "username": self.username_entry.get(),
            "password": self.password_entry.get()
        }

        with open(file="./data.json", mode="r+") as data_file:
            # Read the current file contents
            file_data = json.load(data_file)
            # Add new data with an index at the end of the json
            entry_count = len(file_data)
            file_data[f"{entry_count}"] = form_data
            # Move file pointer back to beginning and write json data
            data_file.seek(0)
            json.dump(file_data, data_file, indent=4)

        # Clear form
        self.website_entry.delete(0, tkinter.END)
        self.username_entry.delete(0, tkinter.END)
        self.password_entry.delete(0, tkinter.END)


def main():
    # Create app
    app = PasswordGenerator()

    # Run app
    app.window.mainloop()


if __name__ == "__main__":
    main()
