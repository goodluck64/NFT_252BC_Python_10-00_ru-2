import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()

root.title("My Program")
root.geometry("800x600")
root.resizable(False, False)

leftFrame = ttk.Frame(root, borderwidth=2, relief="solid")
rightFrame = ttk.Frame(root, borderwidth=2, relief="solid")

leftFrame.pack(side="left", fill="both", expand=False)
rightFrame.pack(side="right", fill="both", expand=False)

# Entry & Button

entry = ttk.Entry(rightFrame)
entry1 = ttk.Entry(rightFrame)

def add_label():
    text = entry.get()

    new_label = ttk.Label(leftFrame, text=text)

    new_label.pack()

def remove_label():
    for widget in leftFrame.winfo_children():
        if widget.cget("text") == entry1.get():
            widget.destroy()
            break


button = ttk.Button(rightFrame, text="Add", command=add_label)
button1 = ttk.Button(rightFrame, text="Remove", command=remove_label)

entry.pack(side="bottom", fill="x")
entry1.pack(side="bottom", fill="x")
button.pack(side="bottom", fill="x")
button1.pack(side="bottom", fill="x")

root.mainloop()