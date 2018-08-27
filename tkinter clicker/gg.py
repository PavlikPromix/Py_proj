from tkinter import *


wg = Tk()
wg.geometry('200x70')
wg.title('Введи промокод')

e1 = Entry(wg, width = 29)
e1.place(x = 10, y = 10)

b1 = Button(wg, text = 'Проверить', width = 24)
b1.place(x = 10, y = 35)

wg.mainloop()
