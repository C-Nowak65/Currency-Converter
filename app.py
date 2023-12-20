import tkinter as tk
from tkinter import ttk, messagebox
from main import get_supported_currencies, get_exchange_rates

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

root = tk.Tk()
root.title("Currency Converter")

source_currency_var = tk.StringVar()
target_currency_var = tk.StringVar()
amount_var = tk.StringVar()
result_var = tk.StringVar()

ttk.Label(root, text="Source Currency:").pack()
source_currency_entry = ttk.Entry(root, textvariable=source_currency_var)
source_currency_entry.pack()

ttk.Label(root, text="Target Currency:").pack()
target_currency_entry = ttk.Entry(root, textvariable=target_currency_var)
target_currency_entry.pack()

ttk.Label(root, text="Amount:").pack()
amount_entry = ttk.Entry(root, textvariable=amount_var)
amount_entry.pack()

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.pack()

result_label = ttk.Label(root, textvariable=result_var)
result_label.pack()

root.mainloop()

