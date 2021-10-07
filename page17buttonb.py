

import Tkinter as tk 


 
win = tk.Tk()  
win.title("Python GUI App")# Label  
Lbl = tk.Label(win, text = "Button Not Click ")  
Lbl.pack()# Click event  
def click(): 
 action.configure(text = "Clicked") 	 
 Lbl.configure(foreground = 'red')  
 Lbl.configure(text = 'Button Clicked')# Adding Button  
action = tk.Button(win, text = "Click Me", command = click)  
action.pack()  
win.mainloop() 
