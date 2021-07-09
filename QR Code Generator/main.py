from tkinter import *
import qrcode


def generate():
    qr = qrcode.QRCode(
        version=6,
        box_size=16,
        border=5,
    )
    qr.add_data(data=secret.get())
    qr.make(fit=True)
    img = qr.make_image(fill="Black", back_color="white")
    img.save("qrcode.png")


root = Tk()
root.geometry("600x600")
root.title("My GUI")

Label(root, text="Generate QR Code", font="arial 14 bold").grid(row=0, column=1)

secret = StringVar()
secretentry = Entry(root, textvariable=secret)

secretentry.grid(row=2, column=1)

lb = Button(root, text="Generate Code", command=generate).grid(row=2, column=2)

root.mainloop()
