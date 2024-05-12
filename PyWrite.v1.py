import tkinter
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from PIL import Image, ImageTk
import os, customtkinter

file_state = False # refers to whether the file is saved or not

def open_file():
    file = fd.askopenfilename(defaultextension=".txt",
                              filetypes=[("All Files", "*.*"), ("Text File", "*.txt*")])
    if file != "":
        root.title(f"{os.path.basename(file)}")
        text.delete(1.0, END)
        with open(file, "r") as f:
            text.insert(1.0, f.read())
            f.close()
    else:
        file = None

    global file_state
    file_state = True

def new():
    root.title("Untitled - Pywrite")
    text.delete(1.0, END)
    global file_state
    file_state = False

def save():
    global text
    txt = text.get("1.0", "end-1c")
    saveloc = fd.asksaveasfilename()
    file = open(saveloc, "w+")
    file.write(txt)
    file.close()
    root.title(os.path.basename(saveloc))
    global file_state
    file_state = True

def close_app():
    root.destroy()

def func_copy():
    text.event_generate("<<Copy>>")

def func_cut():
    text.event_generate("<<Cut>>")

def func_paste():
    text.event_generate("<<Paste>>")

def select_all():
    text.tag_add(SEL, "1.0", END)
    text.mark_set(INSERT, "1.0")
    text.see(INSERT)
    return ''

def fontc():
    global text
    text.config(font=("Courier", 12))

def fonth():
    global text
    text.config(font=("Helvetica", 12))

def fontime():
    global text
    text.config(font=("Times New Roman", 12))

root=Tk()
root.title("Untitled - Pywrite")
root.geometry("800x500")
root.resizable(True, True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text = Text(root, font=("Courier", 12))
text.grid(sticky=NSEW)

scroll_bar = Scrollbar(text, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=Y)

scroll_bar.config(command=text.yview)
text.config(yscrollcommand=scroll_bar.set)

menu_bar = Menu(root)
menu = Menu(menu_bar, tearoff=False, activebackground="#ffcc00")
menu.add_command(label="New File", command=new)
menu.add_command(label="Open existing file", command=open_file)
menu.add_command(label="Save As", command=save)
menu.add_separator()
menu.add_command(label="Close File", command=close_app)
menu_bar.add_cascade(label="File", menu=menu)

edit_menu = Menu(menu_bar, tearoff=False, activebackground='#ffcc00')
edit_menu.add_command(label='Copy', command=func_copy)
edit_menu.add_command(label='Cut', command=func_cut)
edit_menu.add_command(label='Paste', command=func_paste)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', command=select_all)
fontmenu = Menu(edit_menu, tearoff=False, activebackground='#ffcc00')
fontmenu.add_command(label='Courier', command=fontc)
fontmenu.add_command(label='Helvetica', command=fonth)
fontmenu.add_command(label='Times New Roman', command=fontime)
edit_menu.add_cascade(label='Font', menu=fontmenu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)

icon = ImageTk.PhotoImage(Image.open('Pywrite_Logo_v2.png'))
root.iconphoto(False, icon)

root.update()
root.mainloop()

