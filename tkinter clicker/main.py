from tkinter import *
import time
import threading
from tkinter import messagebox

#DATA :

data = [0, 1, 5, 0, 1, 0, 200]

gift = [1]

#Functions :

def autoUnit():
    while True:
        if data[3] > 0:
            while True:
                time.sleep(2)
                data[0] = data[0] + data[5]
                moneyVL['text'] = data[0]


def click ():
    money = data[0]
    bonus = data[1]
    data[0] = money + bonus
    moneyVL['text'] = data[0]

def upgrade ():
    if data[0] < data[2]:
        pass
    else:
        bonus = data[1]
        data[1] = bonus * 2
        moneyBL['text'] = data[1]
        data[0] = data[0] - data[2]
        moneyVL['text'] = data[0]
        data[2] = data[2] * 4
        UpgradeB['text'] = 'Upgrade.\nCost : {}'.format(data[2])
        data[4] = data[4] + 1
        UpgradeLVLVL['text'] = data[4]

def BuyUnit ():
    if data[6] > data[0]:
        pass
    else:
        data[3] = data[3] + 1
        UnitsVL['text'] = data[3]
        data[5] = data[5] + 4
        data[0] = data[0] - data[6]
        moneyVL['text'] = data[0]
        data[6] = data[6] + 200
        BuyUnitsB['text'] = 'Buy Unit.\nCost : {}'.format(data[6])

def save ():
    s1 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\1money.txt', 'w')
    s1.write(str(data[0]))
    s1.close()
    s2 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\2bonus.txt', 'w')
    s2.write(str(data[1]))
    s2.close()
    s3 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\3UpCost.txt', 'w')
    s3.write(str(data[2]))
    s3.close()
    s4 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\4Units.txt', 'w')
    s4.write(str(data[3]))
    s4.close()
    s5 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\5UpLVL.txt', 'w')
    s5.write(str(data[4]))
    s5.close()
    s6 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\6UnitsB.txt', 'w')
    s6.write(str(data[5]))
    s6.close()
    s7 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\7UnitsCost.txt', 'w')
    s7.write(str(data[6]))
    s7.close()
    messagebox.showinfo('Внимание!', 'Сохранение прошло успешно!')

def load ():
    s1 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\1money.txt', 'r')
    s2 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\2bonus.txt', 'r')
    s3 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\3UpCost.txt', 'r')
    s4 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\4Units.txt', 'r')
    s5 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\5UpLVL.txt', 'r')
    s6 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\6UnitsB.txt', 'r')
    s7 = open(r'C:\Users\PK\Saved Games\Tkinter Clicker SAVE_DATA\7UnitsCost.txt', 'r')
    data[0] = int(s1.read())
    data[1] = int(s2.read())
    data[2] = int(s3.read())
    data[3] = int(s4.read())
    data[4] = int(s5.read())
    data[5] = int(s6.read())
    data[6] = int(s7.read())
    s1.close()
    s2.close()
    s3.close()
    s4.close()
    s5.close()
    s6.close()
    s7.close()
    moneyVL['text'] = data[0]
    moneyBL['text'] = data[1]
    UpgradeB['text'] = 'Upgrade.\nCost : {}'.format(data[2])
    UnitsVL['text'] = data[3]
    UpgradeLVLVL['text'] = data[4]
    BuyUnitsB['text'] = 'Buy Unit.\nCost : {}'.format(data[6])
    messagebox.showinfo('Внимание!', 'Загрузка прошла успешно!')

def checkgift ():

    def check ():
        if e1.get() == 'Pr0m1x' and gift[0] == 1:
            data[0] = data[0] + 2000
            gift[0] = 0
            moneyVL['text'] = data[0]
            messagebox.showinfo('Успешно', 'Промокод успешно применен!')

    wg = Tk()
    wg.geometry('200x70')
    wg.title('Введи промокод')

    e1 = Entry(wg, width = 29)
    e1.place(x = 10, y = 10)

    b1 = Button(wg, text = 'Проверить', width = 24, command = check)
    b1.place(x = 10, y = 35)

    wg.mainloop()

#Code :

w = Tk()

mainmenu = Menu(w)

w.config(menu=mainmenu)

filemenu = Menu(mainmenu)

filemenu.add_command(label="Сохранить", command = save)
filemenu.add_command(label="Загрузить", command = load)
filemenu.add_command(label="Промокод", command = checkgift)

mainmenu.add_cascade(label="Игра", menu=filemenu)

w.geometry('375x300')

th = threading.Thread(target = autoUnit, name='autoMoney')
th.start()
#Labels :

##money :

moneyVL = Label(text = data[0], font = ("Comic Sans MS", 25, "bold"))
moneyVL.place(x = 15, y = 25)

moneyVSL = Label(text = 'Money :', font = ("Comic Sans MS", 10, "bold"))
moneyVSL.place(x = 15, y = 10)

##moneyB :

moneyBL = Label(text = data[1], font = ("Comic Sans MS", 25, "bold"))
moneyBL.place(x = 15, y = 95)

moneyBSL = Label(text = 'Money Bonus :', font = ("Comic Sans MS", 10, "bold"))
moneyBSL.place(x = 15, y = 80)

##Units :

UnitsVL = Label(text = data[3], font = ("Comic Sans MS", 25, "bold"))
UnitsVL.place(x = 255, y = 25)

UnitsVSL = Label(text = 'Auto Units :', font = ("Comic Sans MS", 10, "bold"))
UnitsVSL.place(x = 255, y = 10)

##UpgradeLVL :

UpgradeLVLVL = Label(text = data[4], font = ("Comic Sans MS", 25, "bold"))
UpgradeLVLVL.place(x = 255, y = 95)

UpgradeLVLVSL = Label(text = 'Upgrade LVL :', font = ("Comic Sans MS", 10, "bold"))
UpgradeLVLVSL.place(x = 255, y = 80)

#buttons :

ClickB = Button (text = 'Click', height = 8, width = 13, command = click)
ClickB.place(x = 15, y = 150)

UpgradeB = Button (text = 'Upgrade.\nCost : {}'.format(data[2]), height = 8, width = 13, command = upgrade)
UpgradeB.place(x = 130, y = 150)

BuyUnitsB = Button (text = 'Buy Unit.\nCost : {}'.format(data[6]), height = 8, width = 13, command = BuyUnit)
BuyUnitsB.place(x = 245, y = 150)


w.mainloop()
