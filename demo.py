import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def convert():
    try:
        amount = float(amnt_entry.get())
        from_curr = from_currency_var.get()
        to_curr = to_currency_var.get()

        if not from_curr or not to_curr:
            messagebox.showwarning("Input Error", "Please select both currencies.")
            return


        amount_in_usd = amount / currencies[from_curr]
        converted = amount_in_usd * currencies[to_curr]
        converted = round(converted, 4)

        converted_amount.configure(
            text=f"{amount} {from_curr} = {converted} {to_curr}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title('Currency Converter')
root.geometry('300x300')
root.configure(
    background='sky blue'
)
#Label(root,text='Currency Converter',font=10,bg='light blue',fg='white').pack(side=BOTTOM)

url = "https://v6.exchangerate-api.com/v6/ad61cf7006d8ccbfbcd7c378/latest/USD"
data = requests.get(url).json()
currencies = data['conversion_rates']
to_currency_var = StringVar()
from_currency_var = StringVar()
#to_currency_var.set('USD')

amnt_entry = Entry(root,font='bold 18',width=15)
amnt_entry.pack(padx=10,pady=5,fill=X)

from_currency = ttk.Combobox(root,values=list(currencies.keys()),font='bold 18',textvariable=from_currency_var)
from_currency.pack(padx=10,pady=5,fill=X)

to_currency = ttk.Combobox(root,values=list(currencies.keys()),font='bold 18',textvariable=to_currency_var)
to_currency.pack(padx=10,pady=5,fill=X)

converted_amount = Label(root,text='',font='bold 18')
converted_amount.pack(padx=10,pady=5,fill=X)

convert_button = Button(root,text='Convert',font='bold 18',bg='green',fg='white',command=convert)
convert_button.pack(padx=10,pady=5,fill=X)
root.mainloop()
