

import Tkinter as tk 
from Tkinter  import *
win=tk.Tk()
win.title("Python GUI App")# Label 

label=tk.Label(win,text="Button Not Click")
label.pack()
def click():
 action.configure(text="I have been clicked")
 label.configure(foreground='red')	
 label.configure(text='A red label')

action=tk.Button(win,text='Click me',command=click)

action.pack() 

win.mainloop()
