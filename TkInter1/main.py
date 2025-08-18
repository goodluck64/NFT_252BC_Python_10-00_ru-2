import tkinter as tk
import tkinter.ttk as ttk

# GUI

default_font = ("Tahoma", 24)
root = tk.Tk()

root.geometry("800x600")

label1 = ttk.Label(text="Hello, {0}", font=default_font, background="navy", foreground="white")
entry1 = ttk.Entry()

def on_clicked():
    text = entry1.get()
    replacedText = label1.cget("text").replace("{0}", text)

    label1.configure(text=replacedText)

button1 = ttk.Button(text="Click me", command=on_clicked)

label1.pack(anchor="ne", expand=True, fill="both")
entry1.pack(anchor="ne")
button1.pack(anchor="center")

root.mainloop()

