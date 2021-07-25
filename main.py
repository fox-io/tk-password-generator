"""
tk-password-generator

(c)2021 John Mann <github.fox-io@foxdata.io>
"""
import tkinter


def main():
    window = tkinter.Tk()
    window.title("Password Generator")
    window.config(padx=20, pady=20)
    window.minsize(240, 240)

    padlock_image = tkinter.PhotoImage(file="./logo.png")
    image_frame = tkinter.Canvas(width=200, height=200, highlightthickness=0)
    image_frame.create_image(100, 100, image=padlock_image)
    image_frame.grid(column=0, row=0)

    # Run app event loop
    window.mainloop()


if __name__ == "__main__":
    main()
