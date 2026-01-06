import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def set_placeholder(entry, text):
    entry.insert(0, text)
    entry.config(foreground="gray")

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, END)
            entry.config(foreground="black")

    def on_focus_out(event):
        if not entry.get():
            set_placeholder(entry, text)

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def convert():
    try:
        amount = float(amnt_entry.get())
        from_curr = from_currency_var.get()
        to_curr = to_currency_var.get()

        if from_curr == "Select Currency" or to_curr == "Select Currency":
            messagebox.showwarning("Input Error", "Please select both currencies.")
            return

        amount_in_usd = amount / currencies[from_curr]
        converted = round(amount_in_usd * currencies[to_curr], 4)

        output_box.config(state="normal")
        output_box.delete(1.0, END)
        output_box.insert(END, f"{amount} {from_curr} = {converted} {to_curr}")
        output_box.config(state="disabled")

    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")


root = Tk()
root.title("Currency Converter")
root.geometry("420x350")
root.configure(bg="#2c2f33")

# Fetch currency rates
url = "https://v6.exchangerate-api.com/v6/ad61cf7006d8ccbfbcd7c378/latest/USD"
data = requests.get(url).json()
currencies = data['conversion_rates']

# Frame Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox",
                background="#ffffff", padding=6, relief="flat",
                font=("Arial", 12))

frame = Frame(root, bg="#2c2f33")
frame.pack(pady=10)

# Amount Entry with Placeholder
amnt_entry = Entry(frame, font=("Arial", 14), width=25, relief="flat")
amnt_entry.pack(pady=8)
set_placeholder(amnt_entry, "Enter Amount")

# Scrollable Currency Dropdown
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

from_currency_var = StringVar()
from_currency = Listbox(frame, font=("Arial", 12), width=22, yscrollcommand=scrollbar.set)
for curr in currencies.keys():
    from_currency.insert(END, curr)

scrollbar.config(command=from_currency.yview)
from_currency.pack(pady=5)

def set_from_currency(event):
    index = from_currency.curselection()
    if index:
        from_currency_var.set(from_currency.get(index))
        from_currency_label.config(text=f"From: {from_currency_var.get()}")

from_currency.bind("<<ListboxSelect>>", set_from_currency)

from_currency_label = Label(frame, text="Select From Currency", bg="#2c2f33", fg="white", font=("Arial", 10))
from_currency_label.pack()

# To currency dropdown
scrollbar2 = Scrollbar(frame)
scrollbar2.pack(side=RIGHT, fill=Y)

to_currency_var = StringVar()
to_currency = Listbox(frame, font=("Arial", 12), width=22, yscrollcommand=scrollbar2.set)
for curr in currencies.keys():
    to_currency.insert(END, curr)

scrollbar2.config(command=to_currency.yview)
to_currency.pack(pady=5)

def set_to_currency(event):
    index = to_currency.curselection()
    if index:
        to_currency_var.set(to_currency.get(index))
        to_currency_label.config(text=f"To: {to_currency_var.get()}")

to_currency.bind("<<ListboxSelect>>", set_to_currency)

to_currency_label = Label(frame, text="Select To Currency", bg="#2c2f33", fg="white", font=("Arial", 10))
to_currency_label.pack()

# Output Box (Separate Box)
output_box = Text(root, height=3, width=38, font=("Arial", 14), state="disabled",
                  relief="solid", borderwidth=3, bg="#ffffff")
output_box.pack(pady=10)

# Convert Button
convert_button = Button(root, text="Convert", font=("Arial", 16, "bold"),
                        bg="#1abc9c", fg="white", relief="flat", command=convert)
convert_button.pack(pady=10)

root.mainloop()
