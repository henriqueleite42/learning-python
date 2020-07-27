# Inspired in https://www.instagram.com/p/CC7st6KBf2X/

import tkinter as tk
import pyjokes

root = tk.Tk()

root.geometry('300x100')
root.title('FUN GAME')

T = tk.Text(root, height=4, width=80)
T.pack()

def generate_joke():
  global joke
  joke = pyjokes.get_joke()
  T.insert(tk.END, joke)

b = th.Button(text='JOKE', command=generate_joke)
b.pack()

root.mainloop()
