from tkinter import *   #used for graphical interface (GUI's)
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('clock')

def time():
    string = strftime('%H:%M:%S %p')  #converting data and time objects to their string representations
    label.config(text=string)
    label.after(1000,time)
label = Label(root, font=('DS-DIGIT.TTF', 80), background='black', foreground='cyan')
label.pack(anchor='center')

time()
mainloop()

