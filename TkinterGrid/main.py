import tkinter as tk
from tkinter import ttk
import my_widgets

root = tk.Tk()

root.title("Grid Test")
root.geometry("800x600")
# root.resizable(False, False)

my_widgets.create_widgets(root)

root.mainloop()


# res = eval("(2 + 2) * 2 ** 5")
#
# print(res)
