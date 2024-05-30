
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x600")
window.configure(bg = "#161616")


canvas = Canvas(
    window,
    bg = "#161616",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    103.0,
    42.0,
    anchor="nw",
    text="YT DROID Downloader",
    fill="#FFFFFF",
    font=("Inter Bold", 48 * -1)
)

canvas.create_text(
    311.0,
    93.0,
    anchor="nw",
    text="Youtube video Downloader",
    fill="#FF0000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    330.0,
    219.0,
    anchor="nw",
    text="Enter video URL",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

canvas.create_text(
    335.0,
    320.0,
    anchor="nw",
    text="Select quality",
    fill="#FFFFFF",
    font=("Inter Medium", 20 * -1)
)

canvas.create_text(
    330.0,
    571.0,
    anchor="nw",
    text="By Viraj Ray 2024©",
    fill="#FFFFFF",
    font=("Inter Medium", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=298.0,
    y=482.0,
    width=203.28878784179688,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=298.0,
    y=420.0,
    width=203.28878784179688,
    height=50.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    408.0,
    274.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=189.0,
    y=256.0,
    width=438.0,
    height=41.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    407.0,
    172.0,
    image=image_image_1
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=300.0,
    y=354.0,
    width=206.0,
    height=38.0
)
window.resizable(False, False)
window.mainloop()
