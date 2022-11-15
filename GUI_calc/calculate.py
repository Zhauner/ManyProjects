import tkinter as tk

def add_number(numb):
    val = numbers.get() + str(numb)
    numbers.delete(0, tk.END)
    numbers.insert(0, val)

def add_operator(oper):
    value = numbers.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    numbers.delete(0, tk.END)
    numbers.insert(0,value+oper)

def delete_numbers():
    numbers.delete(0, tk.END)

def ravn():
    value = str(numbers.get())
    numbers.delete(0, tk.END)
    numbers.insert(0,eval(value))

win = tk.Tk()
photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)
win.config(bg='#696969')
win.title('Calculate')
win.geometry('240x270')
win.resizable(False, False)

numbers = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15, bd=3)
numbers.grid(row=0, column=0, columnspan=4, stick='we')

tk.Button(win, text='1', bd=5, font=('Arial', 13), command=lambda : add_number(1)).grid(row=1, column=0, stick='wens', padx=5, pady=5)
tk.Button(win, text='2', bd=5, font=('Arial', 13), command=lambda : add_number(2)).grid(row=1, column=1, stick='wens', padx=5, pady=5)
tk.Button(win, text='3', bd=5, font=('Arial', 13), command=lambda : add_number(3)).grid(row=1, column=2, stick='wens', padx=5, pady=5)
tk.Button(win, text='4', bd=5, font=('Arial', 13), command=lambda : add_number(4)).grid(row=2, column=0, stick='wens', padx=5, pady=5)
tk.Button(win, text='5', bd=5, font=('Arial', 13), command=lambda : add_number(5)).grid(row=2, column=1, stick='wens', padx=5, pady=5)
tk.Button(win, text='6', bd=5, font=('Arial', 13), command=lambda : add_number(6)).grid(row=2, column=2, stick='wens', padx=5, pady=5)
tk.Button(win, text='7', bd=5, font=('Arial', 13), command=lambda : add_number(7)).grid(row=3, column=0, stick='wens', padx=5, pady=5)
tk.Button(win, text='8', bd=5, font=('Arial', 13), command=lambda : add_number(8)).grid(row=3, column=1, stick='wens', padx=5, pady=5)
tk.Button(win, text='9', bd=5, font=('Arial', 13), command=lambda : add_number(9)).grid(row=3, column=2, stick='wens', padx=5, pady=5)
tk.Button(win, text='0', bd=5, font=('Arial', 13), command=lambda : add_number(0)).grid(row=4, column=0, stick='wens', padx=5, pady=5)

tk.Button(win, text='+',bd=5, font=('Arial', 13), fg='green',command=lambda : add_operator('+')).grid(row=1,column=3, stick='wens', padx=5, pady=5)
tk.Button(win, text='-',bd=5, font=('Arial', 13), fg='red',command=lambda : add_operator('-')).grid(row=2,column=3, stick='wens', padx=5, pady=5)
tk.Button(win, text='*',bd=5, font=('Arial', 13), fg='green',command=lambda : add_operator('*')).grid(row=3,column=3, stick='wens', padx=5, pady=5)
tk.Button(win, text='/',bd=5, font=('Arial', 13), fg='red',command=lambda : add_operator('/')).grid(row=4,column=3, stick='wens', padx=5, pady=5)

tk.Button(win, text='=', bd=5, font=('Arial', 13), fg='blue', command=ravn).grid(row=4,column=2, stick='wens', padx=5, pady=5)

tk.Button(win, text='DEL', bd=5, font=('Arial', 13), fg='blue', command=delete_numbers).grid(row=4,column=1, stick='wens', padx=5, pady=5)

#tk.Button(win, text='*').grid(row=,column=)
#tk.Button(win, text='/').grid(row=,column=)
#tk.Button(win, text='=').grid(row=,column=)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()