import tkinter.ttk as ttk
from idlelib.debugger_r import frametable


def create_widgets(root):
    # change row size
    # root.rowconfigure(0, weight=2)
    # root.columnconfigure(0, weight=2)
    #
    # root.rowconfigure(0, weight=2)
    # root.columnconfigure(1, weight=2)
    #
    # root.rowconfigure(1, weight=1)
    # root.columnconfigure(0, weight=1)
    #
    # root.rowconfigure(1, weight=1)
    # root.columnconfigure(1, weight=1)

    # change column size

    # root.rowconfigure(0, weight=2)
    # root.columnconfigure(0, weight=2)
    #
    # root.rowconfigure(0, weight=1)
    # root.columnconfigure(1, weight=1)
    #
    # root.rowconfigure(1, weight=2)
    # root.columnconfigure(0, weight=2)
    #
    # root.rowconfigure(1, weight=1)
    # root.columnconfigure(1, weight=1)
    #
    # button1 = ttk.Button(root, text="Label 1")
    # button2 = ttk.Button(root, text="Label 2")
    # button3 = ttk.Button(root, text="Label 3")
    # button4 = ttk.Button(root, text="Label 4")
    #
    # # row - строка
    # # column - столбец
    # button1.grid(row=0, column=0, sticky="nsew")
    # button2.grid(row=0, column=1, sticky="nsew")
    # button3.grid(row=1, column=0, sticky="nsew")
    # button4.grid(row=1, column=1, sticky="nsew")

    upper_frame = ttk.Frame(root, borderwidth="2", relief="solid")
    lower_frame = ttk.Frame(root, borderwidth="2", relief="solid")

    # configure frames
    root.rowconfigure(0, weight=3)
    root.columnconfigure(0, weight=3)

    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=3)

    # configure upper frame grid elements
    upper_frame.rowconfigure(0, weight=2)
    upper_frame.columnconfigure(0, weight=2)

    upper_frame.rowconfigure(0, weight=1)
    upper_frame.columnconfigure(1, weight=1)

    upper_frame.rowconfigure(1, weight=2)
    upper_frame.columnconfigure(0, weight=2)

    upper_frame.rowconfigure(1, weight=1)
    upper_frame.columnconfigure(1, weight=1)

    # configure lower frame grid elements

    lower_frame.rowconfigure(0, weight=1)
    lower_frame.columnconfigure(0, weight=1)

    lower_frame.rowconfigure(0, weight=1)
    lower_frame.columnconfigure(1, weight=1)

    lower_frame.rowconfigure(0, weight=1)
    lower_frame.columnconfigure(2, weight=1)

    #
    upper_frame.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
    lower_frame.grid(column=0, row=1, sticky="nsew", padx=5, pady=5)

    # upper frame buttons

    button1 = ttk.Button(upper_frame, text="Button 1")
    button2 = ttk.Button(upper_frame, text="Button 2")
    button3 = ttk.Button(upper_frame, text="Button 3")

    button1.grid(row=0, column=0, sticky="nsew")
    button2.grid(row=0, column=1, rowspan=2, sticky="nsew")
    button3.grid(row=1, column=0, sticky="nsew")

    # lower frame buttons



    entry1 = ttk.Entry(lower_frame)
    button5 = ttk.Button(lower_frame, text="Button 5")

    def on_button6_clicked():
        current_text: str = entry1.get()

        last_index = len(current_text) - 1

        entry1.insert(last_index, "1")

    button6 = ttk.Button(lower_frame, text="CLICK ME", command=on_button6_clicked)

    button5.grid(row=0, column=0, sticky="nsew")
    button6.grid(row=0, column=1, sticky="nsew")
    entry1.grid(row=0, column=2, sticky="nsew")