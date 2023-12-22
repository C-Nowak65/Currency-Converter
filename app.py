#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk, messagebox
from main import get_supported_currencies, get_exchange_rates

def exit():
    root.destroy()

def convert_currency():
    source = source_currency_var.get().upper()
    target = target_currency_var.get().upper()
    amount_str = amount_var.get()

    try:
        amount = float(amount_str)
        if amount < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a positive number for the amount.")
        return

    rate = get_exchange_rates(source, target)
    if rate is not None:
        converted_amount = rate * amount
        result_var.set(f"{amount} {source} is equal to {converted_amount:.2f} {target}")
    else:
        messagebox.showerror("Conversion Error", "Failed to convert currencies.")

#Setting up the main application window.
root = Tk()
root.title("Currency Converter")


#Creating the content frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

source_currency_var = StringVar()
source_currency_var_entry = ttk.Entry(mainframe, width=7, textvariable=source_currency_var)
source_currency_var_entry.grid(column=2, row=1, sticky=(W, E))

target_currency_var = StringVar()
target_currency_var_entry = ttk.Entry(mainframe, width=7, textvariable=target_currency_var)
target_currency_var_entry.grid(column=2, row=2, sticky=(W, E))

amount_var = StringVar()
amount_var_entry = ttk.Entry(mainframe, width=7, textvariable=amount_var)
amount_var_entry.grid(column=2, row=3, sticky=(W, E))


ttk.Label(mainframe, text="Source Currency").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Target Currency").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Amount").grid(column=3, row=3, sticky=W)

convert_button = ttk.Button(mainframe, text="Convert", command=convert_currency)
convert_button.grid(column=2, row=4)

result_var = StringVar()
result_label = ttk.Label(mainframe, textvariable=result_var)
result_label.grid(column=2, row=5, sticky=(W, E))

root.bind('<Return>', lambda _: convert_currency())
root.bind('<Escape>', lambda _: exit())

source_currency_var_entry.focus()

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()

