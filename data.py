from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview
import tkinter.messagebox as msg  # alias

from validation import name_validator, price_validator

id_list = []


def reset_form():
    id.set(0)
    name.set("")
    price.set(0)
    quantity.set(0)


def add_click():
    if price.get() > 0 and quantity.get() > 0:
        product = (id.get(), price.get(), quantity.get(), name.get(),price.get()* quantity.get())
        table.insert("", END, values=product)
        total.set(total.get() + quantity.get() * price.get())
        reset_form()
        msg.showinfo("Save", "Saved Successful")
        id_list.append(id)

    else:
        msg.showerror("Save Error", "Invalid Data !!!")


win = Tk()
win.geometry("800x320")
win.title("Calculator")

# id
Label(win, text="id").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id).place(x=80, y=20)

# name
Label(win, text="name").place(x=20, y=70)
name = StringVar()
Entry(win, textvariable=name).place(x=80, y=70)

# quantity
Label(win, text="quantity").place(x=20, y=120)
quantity = IntVar()
Entry(win, textvariable=quantity).place(x=80, y=120)

# price
Label(win, text="price").place(x=20, y=170)
price = IntVar()
Entry(win, textvariable=price).place(x=80, y=170)

# Report
Label(win, text="Total").place(x=20, y=220)
total = IntVar()
Entry(win, textvariable=total, state="readonly").place(x=80, y=220)

# Table
table = Treeview(win, columns=[1, 2, 3, 4, 5], height=12, show="headings")

# Title
table.heading(1, text="id")
table.heading(2, text="name")
table.heading(3, text="price")
table.heading(4, text="quantity")
table.heading(5, text="Total")

# Width
table.column(1, width=60)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.place(x=300, y=30)

# Save
Button(win, text="Add", width=8, command=add_click).place(x=80, y=260)

win.mainloop()


print("test_project")