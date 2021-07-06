from tkinter import *

window = Tk()

def kg_conversion():
    print(e1_value.get())
    g = float(e1_value.get())*1000
    t1.insert(END,g)
    ounce = float(e1_value.get())*35.274
    t2.insert(END,ounce)
    pounds = float(e1_value.get())*2.20462
    t3.insert(END,pounds)

b1= Button(window, text = "Convert", command=kg_conversion,)
b1.grid(row=0, column=2)

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2=Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3=Text(window, height=1, width=20)
t3.grid(row=1, column=2)

e1=Label(window,text="Kg")
e1.grid(row=0,column=0)

window.mainloop()
