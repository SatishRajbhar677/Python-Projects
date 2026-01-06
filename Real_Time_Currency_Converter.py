import customtkinter as ctk
from tkinter import messagebox, Listbox, Scrollbar, Toplevel, StringVar
import requests

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def fetch_rates():
    try:
        url = "https://v6.exchangerate-api.com/v6/ad61cf7006d8ccbfbcd7c378/latest/USD"
        data = requests.get(url).json()
        return data["conversion_rates"]
    except:
        messagebox.showerror("API Error", "Could not fetch currency data!")
        app.destroy()

def convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_var.get()
        to_curr = to_var.get()

        if "Select" in from_curr or "Select" in to_curr:
            messagebox.showwarning("Input Error", "Please select both currencies.")
            return

        result = (amount / currencies[from_curr]) * currencies[to_curr]
        output_label.configure(text=f"{amount} {from_curr} = {round(result,4)} {to_curr}")
    except:
        messagebox.showerror("Input Error", "Please enter a valid number")

class ScrollableDropdown(ctk.CTkEntry):
    def __init__(self, master, values, variable, placeholder, **kwargs):
        super().__init__(master, **kwargs)
        self.variable = variable
        self.values = values
        self.placeholder = placeholder

        self.insert(0, placeholder)
        self.configure(fg_color=("#2b2b2b"), text_color="#808080")

        self.bind("<Button-1>", self.show_dropdown)
        self.bind("<FocusIn>", self.remove_placeholder)
        self.dropdown = None

    def remove_placeholder(self, event=None):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self.configure(text_color="white")

    def show_dropdown(self, event=None):
        self.remove_placeholder()
        if self.dropdown:
            self.close_dropdown()

        self.dropdown = Toplevel(self)
        self.dropdown.wm_overrideredirect(True)
        self.dropdown.grab_set()

        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.winfo_height()
        self.dropdown.geometry(f"{self.winfo_width()}x200+{x}+{y}")
        self.dropdown.configure(bg="#1d1d1d")

        scrollbar = Scrollbar(self.dropdown)
        scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(
            self.dropdown, yscrollcommand=scrollbar.set,
            bg="#1d1d1d", fg="white", font=("Segoe UI", 12),
            selectbackground="#3db67d"
        )
        for item in self.values:
            self.listbox.insert("end", item)
        self.listbox.pack(side="left", fill="both", expand=True)
        self.listbox.bind("<ButtonRelease-1>", self.on_select)

        scrollbar.config(command=self.listbox.yview)

    def on_select(self, event):
        index = self.listbox.curselection()
        if index:
            value = self.listbox.get(index[0])
            self.variable.set(value)
            self.delete(0, "end")
            self.insert(0, value)
            self.configure(text_color="white")
        self.close_dropdown()

    def close_dropdown(self):
        if self.dropdown:
            self.dropdown.grab_release()
            self.dropdown.destroy()
            self.dropdown = None

app = ctk.CTk()
app.title("RealTime Currency Converter")
app.geometry("500x550")
app.attributes("-alpha", 0.92)

frame = ctk.CTkFrame(app, corner_radius=25)
frame.pack(padx=20, pady=20, fill="both", expand=True)

title = ctk.CTkLabel(frame, text="Currency Converter", font=("Segoe UI", 24, "bold"))
title.pack(pady=20)

currencies = fetch_rates()
currency_list = list(currencies.keys())

amount_entry = ctk.CTkEntry(frame, placeholder_text="Enter Amount", width=300, height=45, font=("Segoe UI", 16))
amount_entry.pack(pady=12)

from_var = StringVar(value="")
from_dropdown = ScrollableDropdown(
    frame, values=currency_list, variable=from_var,
    placeholder="Select From Currency",
    width=300, height=45, font=("Segoe UI", 16)
)
from_dropdown.pack(pady=12)

to_var = StringVar(value="")
to_dropdown = ScrollableDropdown(
    frame, values=currency_list, variable=to_var,
    placeholder="Select To Currency",
    width=300, height=45, font=("Segoe UI", 16)
)
to_dropdown.pack(pady=12)

convert_btn = ctk.CTkButton(frame, text="Convert", width=200, height=45, font=("Segoe UI", 17, "bold"), command=convert)
convert_btn.pack(pady=20)

output_label = ctk.CTkLabel(frame, text="", font=("Segoe UI", 18, "bold"), width=350)
output_label.pack(pady=20)

app.mainloop()