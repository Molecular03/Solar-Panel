import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Solar Power Calculator')
root.iconphoto(False, tk.PhotoImage(file='sp.png'))
root.grid_columnconfigure(0, weight=1)
wwidth, wheight  = 1000, 800 

center_x = int(root.winfo_screenwidth()/2 - wwidth / 2) #Finds center width
center_y = int(root.winfo_screenheight()/2 - wheight / 2) #Finds center height

root.geometry(f'{wwidth}x{wheight}+{center_x}+{center_y}')
root.lift()

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text='Test').grid(column=0,row=0)

root.mainloop()
