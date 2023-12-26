from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import clipboard as cb


root = Tk()
root.title('Text Editor')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

text = Text(root, undo=True)
text.grid(row=0, column=0)

# File Menu

global fileLocation


def newFile():
    text.delete(0.0, END)


def openFile():
    global fileLocation
    fileLocation = filedialog.askopenfilename()
    file1 = open(fileLocation, 'r')
    t = file1.read()
    text.delete(0.0, END)
    text.insert(INSERT, t)
    file1.close()


def saveFile():
    global fileLocation
    t = text.get('1.0', 'end-1c')
    file1 = open(fileLocation, 'w+')
    file1.write(t)
    file1.close()


def saveFileAs():
    global fileLocation
    t = text.get('1.0', 'end-1c')
    fileLocation = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[
                                                ('Text files', '*.txt')], title='Choose filename')
    file1 = open(fileLocation, 'w+')
    file1.write(t)
    file1.close()


def donothing():
    return 0


def exitWindow():
    answer = messagebox.askquestion(
        title='Exit', message='Do you want to quit?')
    if answer == 'yes':
        root.destroy()

# Edit Menu


def cutSelected():
    t = text.get(SEL_FIRST, SEL_LAST)
    text.delete(SEL_FIRST, SEL_LAST)
    cb.copy(t)


def copySelected():
    t = text.get(SEL_FIRST, SEL_LAST)
    cb.copy(t)


def pasteSelected():
    t = cb.paste()
    text.insert(INSERT, t)


def deleteSelect():
    text.delete(SEL_FIRST, SEL_LAST)


def selectAll():
    text.tag_add(SEL, '1.0', END)
    text.mark_set(INSERT, '1.0')
    text.see(INSERT)

# Help Menu


def helpIndex():
    messagebox.showinfo(
        title='Help', message='Go to www.matthieu-t.fr/dev\nto get more help')


def displayAbout():
    messagebox.showinfo(
        title='About...', message='Text Editor\n\nDevelopped by Matthieu TOURRETTE\nVersion: 0.0.1')


# Tkinter interface

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New', command=newFile)
filemenu.add_command(label='Open', command=openFile)
filemenu.add_command(label='Save', command=saveFile)
filemenu.add_command(label='Save as...', command=saveFileAs)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=exitWindow)

menubar.add_cascade(label='File', menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label='Undo', command=text.edit_undo)
editmenu.add_command(label='Redo', command=text.edit_redo)
editmenu.add_separator()
editmenu.add_command(label='Cut', command=cutSelected)
editmenu.add_command(label='Copy', command=copySelected)
editmenu.add_command(label='Paste', command=pasteSelected)
editmenu.add_separator()
editmenu.add_command(label='Delete', command=deleteSelect)
editmenu.add_command(label='Select All', command=selectAll)

menubar.add_cascade(label='Edit', menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='Help Index', command=helpIndex)
helpmenu.add_command(label='About...', command=displayAbout)

menubar.add_cascade(label='Help', menu=helpmenu)

root.config(menu=menubar)

scrollbar = Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.grid(row=0, column=1, sticky=NS)
text['yscrollcommand'] = scrollbar.set

# DO NOT TOUCH
root.mainloop()
