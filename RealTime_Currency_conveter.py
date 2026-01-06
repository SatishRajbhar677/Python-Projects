from tkinter import *
from tkinter import ttk,ttk
from PIL import ImageTk
import requests


cor0 = "#FFFFFF"
cor1 = "#333333"
cor2 = "#EB5D51"

window = Tk()
window.title("Realtime Currency Conveter")
window.geometry("400x400")
window.configure(background=cor0)
window.resizable(False,False)

top = Frame(window,width=400,height=90,bg=cor2)
top.grid(row=0,column=0)

main=Frame(window,width=400,height=300,bg=cor0)
main.grid(row=1,column=0)

# icon = Image.open('D:\Downloads')
# icon = icon.resize((40, 40))
# icon = ImageTk.PhotoImage(icon)

app_name = Label(top,text="Realtime Currency Conveter",height=1,padx=13,pady=30,anchor=CENTER,font=("Arial",20,"bold"),bg=cor2,fg=cor0)
app_name.place(x=0,y=0)

result = Label(main,text=" ",width=16, height=1,pady=7,relief="solid",anchor=CENTER,font=("Ivy",15,"bold"),bg=cor0,fg=cor1)
result.place(x=50,y=10)

currency =['CAD','BRL','EUR','USD','INR']

From = Label(main,text="From",width=8,height=1,padx=0,pady=0,relief="flat",anchor=NW,font=("Arial",10,"bold"),bg=cor0,fg=cor1)
From.place(x=48,y=90)
combo1 = ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy",12,"bold"))
combo1['values'] = (currency)
combo1.place(x=50,y=115)


To = Label(main,text="To",width=8,height=1,padx=0,pady=0,relief="flat",anchor=NW,font=("Arial",10,"bold"),bg=cor0,fg=cor1)
To.place(x=158,y=90)
combo2 = ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy",12,"bold"))
combo2['values'] = (currency)
combo2.place(x=160,y=115)


value = Entry(main,width=22,justify=CENTER,font=("Ivy",12,"bold"),relief=SOLID)
value.place(x=50,y=155)

button = Button(main,text="Converter",width=19,padx=5,height=1,bg=cor2,fg=cor0,font=("Ivy",12,"bold"))
button.place(x=50,y=210)
window.mainloop()

