# Inspired in https://www.instagram.com/p/CC5cHl7HvgJ/

from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

window = Tk()
window.title("QR Code Generator")

# QR Code Generation
def generate():
  if len(subject.get()) != 0:
    global mQr
    mQr = pyqrcode.create(subject.get())
    qrImage = mQr.xbm(scale=6)
    global photo
    photo = BitmapImage(data=qrImage)
  else:
    messagebox.showinfo("Erro!", "Please Enter The Subject")
  try:
    showCode()
  except:
    pass

# Show QR Code
def showCode():
  global photo
  notificationLabel.config(image=photo)
  subLabel.config(text="Showing QR Code for: " + subject.get())

# Save QR Code
def save():
  # Folter to Save All The Codes
  dir = path1 = os.getcwd() + "\\QRCodes"
  # Create a folder if doesnt existis
  if not os.path.exists(dir):
    os.makedirs(dir)
  try:
    if len(name.get()) != 0:
      qrIrmage = myQr.png(os.path.join(dir, name.get() + ".png"), scale=6)
    else:
      messagebox.showerror("Error!", "File name cannot be empty!")
  except:
    messagebox.showerror("Error!", "Please, generate the code first!")

lab1 = Label(window, text="Enter Subject", font=("Helvetica", 12))
lab1.grid(row=0, column=0, sticky=N + S + E + W)

lab2 = Label(window, text="Enter File Name", font=("Helvetica", 12))
lab2.grid(row=1, column=0, sticky=N + S + E + W)

subject = StringVar()
subjectEntry = Entry(window, textvariable=subject, font=("Helvetica", 12))
subjectEntry.grid(row=0, column=1, sticky=N + S + E + W)

name = StringVar()
nameEntry = Entry(window, textvariable=name, font=("Helvetica", 12))
nameEntry.grid(row=1, column=1, sticky=N + S + E + W)

createButton = Button(window, text="Create QR Code", font=("Helvetica", 12), width=15, command=generate)
createButton.grid(row=0, column=3, sticky=N + S + E + W)

notificationLabel = Label(window)
notificationLabel.grid(row=2, column=1, sticky=N + S + E + W)

subLabel = Label(window, text="")
notificationLabel.grid(row=3, column=1, sticky=N + S + E + W)

showButton = Button(window, text="Save as PNG", font=("Helvetica", 12), width=15, command=save)
showButton.grid(row=1, column=3, sticky=N + S + E + W)

totalRows = 3
totalCols = 3

for row in range(totalRows + 1):
  window.grid_rowconfigure(row, weight=1)

for col in range(totalCols + 1):
  window.grid_columnconfigure(col, weight=1)

window.mainloop()
