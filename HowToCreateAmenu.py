from tkinter import *



def donothing():
    print('ok, ok')

window = Tk()

menu = Menu(window)
window.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu) #cascade är dropdown functionality here u decide how the  submenu functions is gonna behave

subMenu.add_command(label='New project', command=donothing())
subMenu.add_command(label='New...', command=donothing())
subMenu.add_command(label='Save As', command=donothing())
subMenu.add_command(label='Save', command=donothing())
subMenu.add_separator()
subMenu.add_command(label='Exit', command=donothing())

editMenu=Menu(menu)
menu.add_cascade(label='Edit', menu= editMenu) # Cascade Dropdown functionality
editMenu.add_command(label='Redo', command=donothing() )


''' 
def menu(self): (self):


menu = Menu(self.master)
self.master.config(menu=menu)

file = Menu(menu)
file.add_command(label='Exit', command=self.client_exit)
menu.add_cascade(label='File', menu=file)

edit = Menu(menu)
edit.add_command(label='Undo')
menu.add_cascade(label='Edit', menu=edit)



'''
window.mainloop()
