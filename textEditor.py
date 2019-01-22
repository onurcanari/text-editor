from tkinter import *
import tkinter.scrolledtext as tkst
import tkinter.filedialog as tkfd
import tkinter.messagebox as tkmb
import os
def newFile(self):
    textArea.delete('1.0',END)
    root.title('Untitled - Ouur Text Editor')
    return

def openFile(self):
    file = tkfd.askopenfile(mode='rb', title='Select a file')
    if file!=None:
        root.title(os.path.basename(file.name) + ' - Ouur Text Editor')
        contents = file.read()
        textArea.delete('1.0',END)
        textArea.insert('1.0',contents)
        textArea.focus()
        file.close()

def saveFile(self):
    file = tkfd.asksaveasfile(mode="w")
    if file != None:
        root.title(os.path.basename(file.name) + ' - Ouur Text Editor')
        data = textArea.get('1.0',END+'-1c')
        file.write(data)
        textArea.focus()
        file.close()

def exit(self):
    sys.exit()

def about(self):
    tkmb.showinfo(title='Ouur',message='Created by Onurcan Ari')
    return



root = Tk(className="Untitled - Ouur Text Editor")
root.geometry("1024x720")

textArea = tkst.ScrolledText(master=root)

menu = Menu(root)
fileMenu = Menu(menu)
help = Menu(menu)
root.config(menu=menu)

menu.add_cascade(label="File",menu=fileMenu)
menu.add_cascade(label="Help",menu=help)
fileMenu.add_command(label="New File", command=newFile, accelerator='Ctrl+N')
fileMenu.add_command(label="Open File", command=openFile, accelerator='Ctrl+O')
fileMenu.add_command(label="Save File", command=saveFile, accelerator='Ctrl+S')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit, accelerator='Ctrl+Q')
help.add_command(label="About",command=about)

root.bind("<Control-s>",saveFile)
root.bind("<Control-n>",newFile)
root.bind("<Control-q>",exit)
root.bind("<Control-o>",openFile)

textArea.pack(expand=TRUE,side=LEFT,fill=BOTH)
textArea.focus()
root.mainloop()
