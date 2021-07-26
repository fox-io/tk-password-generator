"""
tk-password-generator

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
import tkinter


def main():
    window = tkinter.Tk()
    window.title("Password Generator")
    window.config(padx=20, pady=20)

    padlock_image = tkinter.PhotoImage(file="./logo.png")
    image_frame = tkinter.Canvas(width=200, height=200, highlightthickness=0)
    image_frame.create_image(100, 100, image=padlock_image)
    image_frame.grid(column=1, row=0)

    website_label = tkinter.Label(text="Website:")
    website_label.grid(column=0, row=1, sticky=tkinter.E)
    username_label = tkinter.Label(text="Email/Username:")
    username_label.grid(column=0, row=2, sticky=tkinter.E)
    password_label = tkinter.Label(text="Password:")
    password_label.grid(column=0, row=3, sticky=tkinter.E)

    website_entry = tkinter.Entry(width=51)
    website_entry.grid(column=1, row=1, columnspan=2, sticky=tkinter.W)
    username_entry = tkinter.Entry(width=51)
    username_entry.grid(column=1, row=2, columnspan=2, sticky=tkinter.W)
    password_entry = tkinter.Entry(width=32)
    password_entry.grid(column=1, row=3, sticky=tkinter.W)

    generate_button = tkinter.Button(text="Generate Password")
    generate_button.grid(column=2, row=3, sticky=tkinter.W)

    add_button = tkinter.Button(text="Add", width=43)
    add_button.grid(column=1, row=4, columnspan=2, sticky=tkinter.W)

    # Run app event loop
    window.mainloop()


if __name__ == "__main__":
    main()
