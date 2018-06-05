from tkinter import *

root = Tk()
root.option_add('*tearOff', False)

menubar = Menu(root)
root.config(menu=menubar)
File = Menu(menubar)
Edit = Menu(menubar)
Help_ = Menu(menubar)
menubar.add_cascade(menu=File, label='File')
menubar.add_cascade(menu=Edit, label='Edit')
menubar.add_cascade(menu=Help_, label='Help')
File.add_command(label='New', command=lambda: print(" New File"))
File.add_separator()
File.add_command(label='Open', command=lambda: print("Open File"))
File.add_separator()
save = Menu(File)
File.add_cascade(menu=save, label='Save')
save.add_command(label='Save_as', command=lambda: print(" Save as"))
save.add_command(label='Save_all', command=lambda: print(" Save all"))

root.mainloop()