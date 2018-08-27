from tkinter import *
from tkinter import filedialog as fd

def openfl():
    file_name = fd.askopenfilename()
    fi1e = open(file_name)
    f1re = fi1e.read()
    t1.delete(1.0, END)
    t1.insert(1.0, f1re)
    fi1e.close()

def savefl():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                        ("HTML files", "*.html;*.htm"),
                                        ("PY files", "*.py"),
                                                ("All files", "*.*") ))
    f = open(file_name, 'w')
    s = t1.get(1.0, END)
    f.write(s)
    f.close()

def open2(event):
    openfl()

def save2(event):
    savefl()

w = Tk()

mainmenu = Menu(w)

w.config(menu=mainmenu)

filemenu = Menu(mainmenu)

filemenu.add_command(label="Открыть", command = openfl)
filemenu.add_command(label="Сохранить", command = savefl)

mainmenu.add_cascade(label="Файл", menu=filemenu)

w.geometry('400x500')

w.title('Notepad')

t1 = Text(height = 28, width = 44)
t1.place(x = 20, y = 20)

w.bind('<Control-KeyPress-o>', open2)
w.bind('<Control-KeyPress-s>', save2)

w.mainloop()
