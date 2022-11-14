import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Radiobutton
from tkinter.filedialog import asksaveasfilename
from tkinter import scrolledtext

def add_digit(digit):
    value= calc.get()
    if value[0]=='0':
        value = value[1:]
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)

def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)

def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value+value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))

def clear():
    calc.delete(0, tk.END)
    calc.insert(0,0)


def make_digit_button(digit):
    return tk.Button(tab1, text=digit, bd=5, font=('Arial', 15), command=lambda: add_digit(digit))

def make_operation_button(operation):
    return tk.Button(tab1, text=operation, bd=5, font=('Arial', 15), command=lambda: add_operation(operation))

def make_calc_button(operation):
    return tk.Button(tab1, text=operation, bd=5, font=('Arial', 15), command=calculate)

def make_clear_button(operation):
    return tk.Button(tab1, text=operation, bd=5, font=('Arial', 15), command=clear)

def clecked1():
   if selected.get()==0: messagebox.showinfo("You chosen","First")
   if selected.get()==1: messagebox.showinfo("You chosen","Second")
   if selected.get()==2: messagebox.showinfo("You chosen","Third")

def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text file", "*.txt")]
    )
    if not filepath:
        return
    with open(filepath, "w", encoding="UTF-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
        tab1dow.title(f"Work with - {filepath}")


tab1dow=Tk()
tab1dow.title("Tuchina Daria Alexandrovna")
tab1dow.geometry(f"280x310+100+200")
tab_control=ttk.Notebook(tab1dow)
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)
tab_control.add(tab1,text="The first")
tab_control.add(tab2,text="The second")
tab_control.add(tab3,text="The third")
tab_control.pack(expand=1,fill='both')

selected=IntVar()
selected.set(0)
rad1=Radiobutton(tab2,text="First",value=0,variable=selected)
rad2=Radiobutton(tab2,text="Second",value=1,variable=selected)
rad3=Radiobutton(tab2,text="Third",value=2,variable=selected)
rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)
btn1= Button(tab2,text="Click",command=clecked1)
btn1.grid(column=0,row=1)

calc = tk.Entry(tab1,justify=tk.RIGHT,font=('Times New Roman',15),width=15)
calc.insert(0,'0')
calc.grid(row=0,column=0,columnspan=4,stick='we',padx=5)
make_digit_button("1").grid(row=1, column=0,stick='wens', padx=5, pady=5)
make_digit_button("2").grid(row=1, column=1,stick='wens', padx=5, pady=5)
make_digit_button("3").grid(row=1, column=2,stick='wens', padx=5, pady=5)
make_digit_button("4").grid(row=2, column=0,stick='wens', padx=5, pady=5)
make_digit_button("5").grid(row=2, column=1,stick='wens', padx=5, pady=5)
make_digit_button("6").grid(row=2, column=2,stick='wens', padx=5, pady=5)
make_digit_button("7").grid(row=3, column=0,stick='wens', padx=5, pady=5)
make_digit_button("8").grid(row=3, column=1,stick='wens', padx=5, pady=5)
make_digit_button("9").grid(row=3, column=2,stick='wens', padx=5, pady=5)
make_digit_button("0").grid(row=4, column=0,stick='wens', padx=5, pady=5)
make_operation_button("+").grid(row=1, column=3,stick='wens', padx=5, pady=5)
make_operation_button("-").grid(row=2, column=3,stick='wens', padx=5, pady=5)
make_operation_button("*").grid(row=3, column=3,stick='wens', padx=5, pady=5)
make_operation_button("/").grid(row=4, column=3,stick='wens', padx=5, pady=5)

make_calc_button("=").grid(row=4, column=2,stick='wens', padx=5, pady=5)
make_clear_button("C").grid(row=4, column=1,stick='wens', padx=5, pady=5)


tab1.grid_columnconfigure(0,minsize=60)
tab1.grid_columnconfigure(1,minsize=60)
tab1.grid_columnconfigure(2,minsize=60)
tab1.grid_columnconfigure(3,minsize=60)
tab1.grid_rowconfigure(1,minsize=60)
tab1.grid_rowconfigure(2,minsize=60)
tab1.grid_rowconfigure(3,minsize=60)
tab1.grid_rowconfigure(4,minsize=60)


txt_edit=scrolledtext.ScrolledText(tab3,width=50,height=10,bg="white",fg="black")
txt_edit.grid(row=1, column=0, columnspan=2,padx=35)
btn_save = tk.Button(tab3,text="Save file", command=save_file)
btn_save.grid(row=5, column=0, padx=5, pady=5)


tab1dow.mainloop()
