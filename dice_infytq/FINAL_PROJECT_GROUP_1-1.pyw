import winsound
from tkinter import *
import tkinter.messagebox

window1 = Tk()
window1.geometry("400x300")
window1.title("ROLL DICE")
winsound.PlaySound("welcome2.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

def qu():
        winsound.PlaySound("quit.wav",winsound.SND_FILENAME)
        window1.destroy()



var = StringVar()
fn1 = StringVar()
fn2 = StringVar()
fn3 = StringVar()
fn4 = StringVar()
var_r1 = StringVar()
var_r2 = StringVar()
var_r3 = StringVar()
var_r4 = StringVar()
aaa=StringVar()
a='Player 1'
b='Player 2'
c='Player 3'
d='Player 4'


def dice11():
    global col1
    col1 = 'red'


def dice12():
    global col1
    col1 = 'blue'


def dice13():
    global col1
    col1 = 'green'


def dice14():
    global col1
    col1 = 'yellow'

def dice21():
    global col2
    col2 = 'red'


def dice22():
    global col2
    col2 = 'blue'


def dice23():
    global col2
    col2 = 'green'


def dice24():
    global col2
    col2 = 'yellow'

def dice31():
    global col3
    col3 = 'red'


def dice32():
    global col3
    col3 = 'blue'


def dice33():
    global col3
    col3 = 'green'


def dice34():
    global col3
    col3 = 'yellow'

def dice41():
    global col4
    col4 = 'red'


def dice42():
    global col4
    col4 = 'blue'


def dice43():
    global col4
    col4 = 'green'


def dice44():
    global col4
    col4 = 'yellow'


def name():
    winsound.PlaySound("play.wav",winsound.SND_FILENAME)
    def win():
            winsound.PlaySound("quit.wav",winsound.SND_FILENAME)
            window2.destroy()

    if var.get() == '   1 Player':
        
        def dic1 ():
            global a
            a=entry_2.get()
        window2 = Tk()
        window2.geometry("800x170")
        window2.title("1 PLAYER GAME")
        window2.config(bg='purple')
        label2 = Label(window2, text="Name Of Player", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                       bg='blue')
        label2.place(x=0, y=20)
        entry_2 = Entry(window2, textvar=fn1, width=20, font=('arial', 16, 'bold'))
        entry_2.place(x=300, y=20)
        q1 = Radiobutton(window2, text='Done', value="red", command=dic1)
        q1.config(width=6, font=('arial', 14, 'bold'), bg='pink',fg='black')
        q1.place(x=598, y=20)



        label3 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                       bg='blue')
        label3.place(x=0, y=50)
        r1 = Radiobutton(window2, text='Red', variable=var_r1, value="red", command=dice11)
        r1.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r1.place(x=300, y=53)
        r2 = Radiobutton(window2, text='Blue', variable=var_r1, value="blue", command=dice12)
        r2.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r2.place(x=400, y=53)
        r3 = Radiobutton(window2, text='Green', variable=var_r1, value="green", command=dice13)
        r3.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r3.place(x=500, y=53)
        r4 = Radiobutton(window2, text='Yellow', variable=var_r1, value="ywllow", command=dice14)
        r4.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r4.place(x=600, y=53)

        b11 = Button(window2, text="Play", width=12, bg='brown', fg='white', font=('arial', 14, 'italic'),
                     command=dice1)
        b11.place(x=200, y=130)
        b12 = Button(window2, text="Exit", width=12, bg='brown', fg='white', font=('arial', 14, 'italic'),
                     command=win)
        b12.place(x=350, y=130)


    elif var.get() == '   2 Player':
        def dic1 ():
            global a
            a=entry_2.get()
        def dic2 ():
            global b
            b=entry_21.get()
        window2 = Tk()
        window2.geometry("800x270")
        window2.title("2 PLAYER GAME")
        window2.config(bg='purple')
        label2 = Label(window2, text="Name Of Player 1", relief='solid', width=20, font=('arial', 16, 'bold'),
                       fg='white', bg='blue')
        label2.place(x=0, y=20)
        entry_2 = Entry(window2, textvar=fn1, width=20, font=('arial', 16, 'bold'))
        entry_2.place(x=300, y=20)
        q1 = Radiobutton(window2, text='Done',variable=aaa, value="red", command=dic1)
        q1.config(width=6, font=('arial', 14, 'bold'), bg='pink', fg='black')
        q1.place(x=598, y=20)
        label3 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                       bg='blue')
        label3.place(x=0, y=50)
        r1 = Radiobutton(window2, text='Red', variable=var_r1, value="red", command=dice11)
        r1.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r1.place(x=300, y=53)
        r2 = Radiobutton(window2, text='Blue', variable=var_r1, value="blue", command=dice12)
        r2.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r2.place(x=400, y=53)
        r3 = Radiobutton(window2, text='Green', variable=var_r1, value="green", command=dice13)
        r3.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r3.place(x=500, y=53)
        r4 = Radiobutton(window2, text='Yellow', variable=var_r1, value="ywllow", command=dice14)
        r4.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r4.place(x=600, y=53)

        label21 = Label(window2, text="Name Of Player 2", relief='solid', width=20, font=('arial', 16, 'bold'),
                        fg='white', bg='blue')
        label21.place(x=0, y=100)
        entry_21 = Entry(window2, textvar=fn2, width=20, font=('arial', 16, 'bold'))
        entry_21.place(x=300, y=100)
        q2 = Radiobutton(window2, text='Done',variable=aaa, value="re", command=dic2)
        q2.config(width=6, font=('arial', 14, 'bold'), bg='pink', fg='black')
        q2.place(x=598, y=100)
        label31 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                        bg='blue')
        label31.place(x=0, y=130)
        r11 = Radiobutton(window2, text='Red', variable=var_r2, value="red", command=dice21)
        r11.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r11.place(x=300, y=133)
        r21 = Radiobutton(window2, text='Blue', variable=var_r2, value="blue", command=dice22)
        r21.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r21.place(x=400, y=133)
        r31 = Radiobutton(window2, text='Green', variable=var_r2, value="green", command=dice23)
        r31.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r31.place(x=500, y=133)
        r41 = Radiobutton(window2, text='Yellow', variable=var_r2, value="ywllow", command=dice24)
        r41.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r41.place(x=600, y=133)

        b11 = Button(window2, text="Play", width=12, bg='brown', fg='white', font=('arial', 14, 'italic'),
                     command=dice2)
        b11.place(x=200, y=210)
        b12 = Button(window2, text="Exit", width=12, bg='brown', fg='white', font=('arial', 14, 'italic'),
                     command=win)
        b12.place(x=350, y=210)

    elif var.get() == '   3 Player':
        def dic1 ():
            global a
            a=entry_2.get()
        def dic2 ():
            global b
            b=entry_21.get()
        def dic3 ():
            global c
            c=entry_211.get()
        window2 = Tk()
        window2.geometry("800x350")
        window2.title("3 PLAYER GAME")
        window2.config(bg='purple')
        label2 = Label(window2, text="Name Of Player 1", relief='solid', width=20, font=('arial', 16, 'bold'),
                       fg='white', bg='blue')
        label2.place(x=0, y=20)
        entry_2 = Entry(window2, textvar=fn1, width=20, font=('arial', 16, 'bold'))
        entry_2.place(x=300, y=20)
        q1 = Radiobutton(window2, text='Done',variable=aaa,value='1', command=dic1)
        q1.config(width=6, font=('arial', 14, 'bold'), bg='pink', fg='black')
        q1.place(x=598, y=20)
        label3 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                       bg='blue')
        label3.place(x=0, y=50)
        r1 = Radiobutton(window2, text='Red', variable=var_r1, value="red", command=dice11)
        r1.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r1.place(x=300, y=53)
        r2 = Radiobutton(window2, text='Blue', variable=var_r1, value="blue", command=dice12)
        r2.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r2.place(x=400, y=53)
        r3 = Radiobutton(window2, text='Green', variable=var_r1, value="green", command=dice13)
        r3.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r3.place(x=500, y=53)
        r4 = Radiobutton(window2, text='Yellow', variable=var_r1, value="ywllow", command=dice14)
        r4.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r4.place(x=600, y=53)

        label21 = Label(window2, text="Name Of Player 2", relief='solid', width=20, font=('arial', 16, 'bold'),
                        fg='white', bg='blue')
        label21.place(x=0, y=100)
        entry_21 = Entry(window2, textvar=fn2, width=20, font=('arial', 16, 'bold'))
        entry_21.place(x=300, y=100)
        q2 = Radiobutton(window2, text='Done',variable=aaa,value='2', command=dic2)
        q2.config(width=6, font=('arial', 14, 'bold'), bg='pink', fg='black')
        q2.place(x=598, y=100)
        label31 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                        bg='blue')
        label31.place(x=0, y=130)
        r11 = Radiobutton(window2, text='Red', variable=var_r2, value="red", command=dice21)
        r11.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r11.place(x=300, y=133)
        r21 = Radiobutton(window2, text='Blue', variable=var_r2, value="blue", command=dice22)
        r21.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r21.place(x=400, y=133)
        r31 = Radiobutton(window2, text='Green', variable=var_r2, value="green", command=dice23)
        r31.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r31.place(x=500, y=133)
        r41 = Radiobutton(window2, text='Yellow', variable=var_r2, value="ywllow", command=dice24)
        r41.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r41.place(x=600, y=133)

        label211 = Label(window2, text="Name Of Player 3", relief='solid', width=20, font=('arial', 16, 'bold'),
                         fg='white', bg='blue')
        label211.place(x=0, y=180)
        entry_211 = Entry(window2, textvar=fn3, width=20, font=('arial', 16, 'bold'))
        entry_211.place(x=300, y=180)
        q3 = Radiobutton(window2, text='Done',variable=aaa,value='3', command=dic3)
        q3.config(width=6, font=('arial', 14, 'bold'), bg='pink', fg='black')
        q3.place(x=598, y=180)
        label311 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                         bg='blue')
        label311.place(x=0, y=210)
        r111 = Radiobutton(window2, text='Red', variable=var_r3, value="red", command=dice31)
        r111.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r111.place(x=300, y=213)
        r211 = Radiobutton(window2, text='Blue', variable=var_r3, value="blue", command=dice32)
        r211.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r211.place(x=400, y=213)
        r311 = Radiobutton(window2, text='Green', variable=var_r3, value="green", command=dice33)
        r311.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r311.place(x=500, y=213)
        r411 = Radiobutton(window2, text='Yellow', variable=var_r3, value="ywllow", command=dice34)
        r411.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r411.place(x=600, y=213)

        b11 = Button(window2, text="Play", width=12, bg='brown', fg='white', font=('arial', 14, 'italic'),
                     command=dice3)
        b11.place(x=200, y=290)
        b12 = Button(window2, text="Exit", width=12, bg='brown', fg='white', font=('arial', 14, 'italic'),
                     command=win)
        b12.place(x=350, y=290)

    elif var.get() == '   4 Player':
        def dic1 ():
            global a
            a=entry_2.get()
        def dic2 ():
            global b
            b=entry_21.get()
        def dic3 ():
            global c
            c=entry_211.get()
        def dic4 ():
            global d
            d=entry_2111.get()
        window2 = Tk()
        window2.geometry("800x420")
        window2.title("4 PLAYER GAME")
        window2.config(bg='purple')
        label2 = Label(window2, text="Name Of Player 1", relief='solid', width=20, font=('arial', 16, 'bold'),
                       fg='white', bg='blue')
        label2.place(x=0, y=20)
        entry_2 = Entry(window2, textvar=fn1, width=20, font=('arial', 16, 'bold'))
        entry_2.place(x=300, y=20)
        q1 = Radiobutton(window2, text='Done',variable=aaa,value='1', command=dic1)
        q1.config(width=6, font=('arial', 14, 'bold'), bg='pink', fg='black')
        q1.place(x=598, y=20)
        label3 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                       bg='blue')
        label3.place(x=0, y=50)
        r1 = Radiobutton(window2, text='Red', variable=var_r1, value="red", command=dice11)
        r1.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r1.place(x=300, y=50)
        r2 = Radiobutton(window2, text='Blue', variable=var_r1, value="blue", command=dice12)
        r2.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r2.place(x=400, y=50)
        r3 = Radiobutton(window2, text='Green', variable=var_r1, value="green", command=dice13)
        r3.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r3.place(x=500, y=50)
        r4 = Radiobutton(window2, text='Yellow', variable=var_r1, value="ywllow", command=dice14)
        r4.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r4.place(x=600, y=50)

        label21 = Label(window2, text="Name Of Player 2", relief='solid', width=20, font=('arial', 16, 'bold'),
                        fg='white', bg='blue')
        label21.place(x=0, y=100)
        entry_21 = Entry(window2, textvar=fn2, width=20, font=('arial', 16, 'bold'))
        entry_21.place(x=300, y=100)
        q2 = Radiobutton(window2, text='Done' ,variable=aaa,value='2', command=dic2)
        q2.config(width=6, font=('arial', 14, 'bold'), bg='pink', fg='black')
        q2.place(x=598, y=100)
        label31 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                        bg='blue')
        label31.place(x=0, y=130)
        r11 = Radiobutton(window2, text='Red', variable=var_r2, value="red", command=dice21)
        r11.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r11.place(x=300, y=130)
        r21 = Radiobutton(window2, text='Blue', variable=var_r2, value="blue", command=dice22)
        r21.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r21.place(x=400, y=130)
        r31 = Radiobutton(window2, text='Green', variable=var_r2, value="green", command=dice23)
        r31.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r31.place(x=500, y=130)
        r41 = Radiobutton(window2, text='Yellow', variable=var_r2, value="ywllow", command=dice24)
        r41.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r41.place(x=600, y=130)

        label211 = Label(window2, text="Name Of Player 3", relief='solid', width=20, font=('arial', 16, 'bold'),
                         fg='white', bg='blue')
        label211.place(x=0, y=180)
        entry_211 = Entry(window2, textvar=fn3, width=20, font=('arial', 16, 'bold'))
        entry_211.place(x=300, y=180)
        q3 = Radiobutton(window2, text='Done',variable=aaa,value='3', command=dic3)
        q3.config(width=6, font=('arial', 14, 'bold'), bg='pink', fg='black')
        q3.place(x=598, y=180)
        label311 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'), fg='white',
                         bg='blue')
        label311.place(x=0, y=210)
        r111 = Radiobutton(window2, text='Red', variable=var_r3, value="red", command=dice31)
        r111.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r111.place(x=300, y=210)
        r211 = Radiobutton(window2, text='Blue', variable=var_r3, value="blue", command=dice32)
        r211.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r211.place(x=400, y=210)
        r311 = Radiobutton(window2, text='Green', variable=var_r3, value="green", command=dice33)
        r311.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r311.place(x=500, y=210)
        r411 = Radiobutton(window2, text='Yellow', variable=var_r3, value="ywllow", command=dice34)
        r411.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r411.place(x=600, y=210)

        label2111 = Label(window2, text="Name Of Player 4", relief='solid', width=20, font=('arial', 16, 'bold'),
                          fg='white', bg='blue')
        label2111.place(x=0, y=260)
        entry_2111 = Entry(window2, textvar=fn4, width=20, font=('arial', 16, 'bold'))
        entry_2111.place(x=300, y=260)
        q4 = Radiobutton(window2, text='Done',variable=aaa,value='4', command=dic4)
        q4.config(width=6, font=('arial', 14, 'bold'), bg='pink', fg='black')
        q4.place(x=598, y=260)
        label3111 = Label(window2, text="Enter Colour", relief='solid', width=20, font=('arial', 16, 'bold'),
                          fg='white', bg='blue')
        label3111.place(x=0, y=290)
        r1111 = Radiobutton(window2, text='Red', variable=var_r4, value="red", command=dice41)
        r1111.config(width=6, font=('arial', 14, 'bold'), bg='red')
        r1111.place(x=300, y=290)
        r2111 = Radiobutton(window2, text='Blue', variable=var_r4, value="blue", command=dice42)
        r2111.config(width=6, font=('arial', 14, 'bold'), bg='blue')
        r2111.place(x=400, y=290)
        r3111 = Radiobutton(window2, text='Green', variable=var_r4, value="green", command=dice43)
        r3111.config(width=6, font=('arial', 14, 'bold'), bg='green')
        r3111.place(x=500, y=290)
        r4111 = Radiobutton(window2, text='Yellow', variable=var_r4, value="ywllow", command=dice44)
        r4111.config(width=6, font=('arial', 14, 'bold'), bg='yellow')
        r4111.place(x=600, y=290)

        b11 = Button(window2, text="Play", width=12, bg='brown', fg='white', font=('arial', 14, 'italic'),
                     command=dice4)
        b11.place(x=200, y=370)
        b12 = Button(window2, text="Exit", width=12, bg='brown', fg='white', font=('arial', 14, 'italic'),
                     command=win)
        b12.place(x=350, y=370)
    else:
        exit()


def dice1():
    winsound.PlaySound("play.wav",winsound.SND_FILENAME)
    def qu():
        winsound.PlaySound("quit.wav",winsound.SND_FILENAME)
        root.destroy()

    import tkinter as tk
    from random import randint

    def create_dice():
        dice = list()
        dice.append(draw_dice('dot0'))  
        dice.append(draw_dice('dot4'))  
        dice.append(draw_dice('dot3', 'dot5'))
        dice.append(draw_dice('dot2', 'dot4', 'dot6'))
        dice.append(draw_dice('dot1', 'dot2', 'dot6', 'dot9'))
        dice.append(draw_dice('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))
        dice.append(draw_dice('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))
        return dice

    def draw_dice(*args):
        w, h = 250, 250 
        x, y, r = 20, 20, 50  
        c = tk.Canvas(root, width=w, height=h, bg=col1) 
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)

        return c

    def click():
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

        t = 100 
        stop = randint(13, 18)
        for x in range(stop):
            dice_index = x % 6 + 1  
            dice_list[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list[dice_index].grid_forget())  
            t += 20

    root = tk.Tk()
    root.title("DICE ROLL")
    root.geometry("250x340")
    root.config(bg='pink')
    dice_list = create_dice()
    dice_list[0].grid(row=1, column=0, columnspan=3)

    labela = tk.Label(root, text=a, bg=col1, fg='black', width=16, font=('arial', 16, 'italic'))
    labela.place(x=0, y=262)
    button1 = tk.Button(root, text='Hit Me', bg=col1, fg='black', font=('arial', 11, 'bold'), command=click)
    button1.place(x=190, y=260)
    button2 = tk.Button(root, text="Quit", bg='brown', fg='white', font=('arial', 14, 'bold'), command=qu)
    button2.place(x=90, y=305)
    root.mainloop()

def dice2():
    winsound.PlaySound("play.wav",winsound.SND_FILENAME)
    def qu():
        winsound.PlaySound("quit.wav",winsound.SND_FILENAME)
        root.destroy()
    import tkinter as tk
    from random import randint

    def create_dice():
        dice = list()
        dice.append(draw_dice('dot0'))  
        dice.append(draw_dice('dot4'))  
        dice.append(draw_dice('dot3', 'dot5'))  
        dice.append(draw_dice('dot2', 'dot4', 'dot6'))  
        dice.append(draw_dice('dot1', 'dot2', 'dot6', 'dot9'))  
        dice.append(draw_dice('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))
        dice.append(draw_dice('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))  
        return dice

    def draw_dice(*args):
        w, h = 250, 250 
        x, y, r = 20, 20, 50  
        c = tk.Canvas(root, width=w, height=h, bg=col1) 
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)

        return c

    def create_dice2():
        dice = list()
        dice.append(draw_dice2('dot0')) 
        dice.append(draw_dice2('dot4'))  
        dice.append(draw_dice2('dot3', 'dot5'))  
        dice.append(draw_dice2('dot2', 'dot4', 'dot6'))  
        dice.append(draw_dice2('dot1', 'dot2', 'dot6', 'dot9'))
        dice.append(draw_dice2('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))
        dice.append(draw_dice2('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))  
        return dice

    def draw_dice2(*args):
        w, h = 250, 250 
        x, y, r = 20, 20, 50  
        c = tk.Canvas(root, width=w, height=h, bg=col2) 
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)  

        return c

    def click2():
        dice_list2=create_dice2()
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

        t = 100 
        stop = randint(13, 18)
        for x in range(stop):
            dice_index = x % 6 + 1
            dice_list2[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list2[dice_index].grid_forget()) 
            t += 20
        

    def click():
        dice_list=create_dice()
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
        t = 100  
        stop = randint(13, 18)  
        for x in range(stop):
            dice_index = x % 6 + 1
            dice_list[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list[dice_index].grid_forget())  
            t += 20

    root = tk.Tk()
    root.title("DICE ROLL")
    root.geometry("250x390")
    root.config(bg='pink')
    dice_list = create_dice()
    dice_list2 = create_dice2()
    dice_list[0].grid(row=1, column=0, columnspan=3)
    labela = tk.Label(root, text=a, bg=col1, fg='black',width=16, font=('arial', 16, 'italic'))
    labela.place(x=0, y=270)
    labelb = tk.Label(root, text=b, bg=col2, fg='black',width=16, font=('arial', 16, 'italic'))
    labelb.place(x=0, y=305)
    button1 = tk.Button(root, text='Hit Me', bg=col1, fg='black', font=('arial', 11, 'bold'), command=click)
    button1.place(x=190, y=268)
    button2 = tk.Button(root, text='Hit Me', bg=col2, fg='black', font=('arial', 11, 'bold'), command=click2)
    button2.place(x=190, y=303)
    button3 = tk.Button(root, text="Quit", bg='brown', fg='white', font=('arial', 14, 'italic'), command=qu)
    button3.place(x=85, y=350)
    root.mainloop()


def dice3():
    winsound.PlaySound("play.wav",winsound.SND_FILENAME)
    def qu():
        winsound.PlaySound("quit.wav",winsound.SND_FILENAME)
        root.destroy()
    import tkinter as tk
    from random import randint

    def create_dice():

        dice = list()
        dice.append(draw_dice('dot0'))
        dice.append(draw_dice('dot4'))
        dice.append(draw_dice('dot3', 'dot5'))
        dice.append(draw_dice('dot2', 'dot4', 'dot6'))
        dice.append(draw_dice('dot1', 'dot2', 'dot6', 'dot9'))
        dice.append(draw_dice('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))
        dice.append(draw_dice('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))
        return dice

    def draw_dice(*args):
        
        w, h = 250, 250
        x, y, r = 20, 20, 50
        c = tk.Canvas(root, width=w, height=h, bg=col1)
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)

        return c

    def create_dice2():
        dice = list()
        dice.append(draw_dice2('dot0'))  
        dice.append(draw_dice2('dot4'))  
        dice.append(draw_dice2('dot3', 'dot5')) 
        dice.append(draw_dice2('dot2', 'dot4', 'dot6'))
        dice.append(draw_dice2('dot1', 'dot2', 'dot6', 'dot9')) 
        dice.append(draw_dice2('dot1', 'dot2', 'dot4', 'dot6', 'dot9')) 
        dice.append(draw_dice2('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9')) 
        return dice

    def draw_dice2(*args):
        w, h = 250, 250 
        x, y, r = 20, 20, 50
        c = tk.Canvas(root, width=w, height=h, bg=col2) 
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)

        return c

    def click2():
        dice_list2 = create_dice2()
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

        t = 100 
        stop = randint(13, 18)  
        for x in range(stop):
            dice_index = x % 6 + 1  
            dice_list2[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list2[dice_index].grid_forget())  
            t += 20

    def click():
        dice_list = create_dice()
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

        t = 100 
        stop = randint(13, 18)
        for x in range(stop):
            dice_index = x % 6 + 1
            dice_list[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list[dice_index].grid_forget())  
            t += 20

    def create_dice3():
        dice = list()
        dice.append(draw_dice3('dot0'))
        dice.append(draw_dice3('dot4'))  
        dice.append(draw_dice3('dot3', 'dot5')) 
        dice.append(draw_dice3('dot2', 'dot4', 'dot6'))  
        dice.append(draw_dice3('dot1', 'dot2', 'dot6', 'dot9'))  
        dice.append(draw_dice3('dot1', 'dot2', 'dot4', 'dot6', 'dot9')) 
        dice.append(draw_dice3('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9')) 
        return dice

    def draw_dice3(*args):
        w, h = 250, 250 
        x, y, r = 20, 20, 50  
        c = tk.Canvas(root, width=w, height=h, bg=col3)
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)

        return c

    def click3():
        dice_list3 = create_dice3()
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

        t = 100  
        stop = randint(13, 18)
        for x in range(stop):
            dice_index = x % 6 + 1  
            dice_list3[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list3[dice_index].grid_forget())
            t += 20

    root = tk.Tk()
    root.title("DICE ROLL")
    root.geometry("250x420")
    root.config(bg='pink')
    dice_list = create_dice()
    dice_list2 = create_dice2()
    dice_list3 = create_dice3()
    dice_list[0].grid(row=1, column=0, columnspan=3)
    labela = tk.Label(root, text=a, bg=col1, fg='black', width=16, font=('arial', 16, 'italic'))
    labela.place(x=0, y=270)
    labelb = tk.Label(root, text=b, bg=col2, fg='black', width=16, font=('arial', 16, 'italic'))
    labelb.place(x=0, y=305)
    labelc = tk.Label(root, text=c, bg=col3, fg='black', width=16, font=('arial', 16, 'italic'))
    labelc.place(x=0, y=340)

    button1 = tk.Button(root, text='Hit Me', bg=col1, fg='black', font=('arial', 11, 'bold'), command=click)
    button1.place(x=190, y=268)
    button2 = tk.Button(root, text='Hit Me', bg=col2, fg='black', font=('arial', 11, 'bold'), command=click2)
    button2.place(x=190, y=303)
    button3 = tk.Button(root, text='Hit Me', bg=col3, fg='black', font=('arial', 11, 'bold'), command=click3)
    button3.place(x=190, y=338)
    button5 = tk.Button(root, text="Quit", bg='brown', fg='white', font=('arial', 14, 'italic'), command=qu)
    button5.place(x=85, y=380)
    root.mainloop()


def dice4():
    winsound.PlaySound("play.wav",winsound.SND_FILENAME)
    def qu():
        winsound.PlaySound("quit.wav",winsound.SND_FILENAME)
        root.destroy()

    import tkinter as tk
    from random import randint

    def create_dice():
        dice = list()
        dice.append(draw_dice('dot0'))  
        dice.append(draw_dice('dot4'))  
        dice.append(draw_dice('dot3', 'dot5'))  
        dice.append(draw_dice('dot2', 'dot4', 'dot6'))
        dice.append(draw_dice('dot1', 'dot2', 'dot6', 'dot9'))
        dice.append(draw_dice('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))  
        dice.append(draw_dice('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))  
        return dice

    def draw_dice(*args):
        w, h = 250, 250  
        x, y, r = 20, 20, 50  
        c = tk.Canvas(root, width=w, height=h, bg=col1)  
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)

        return c

    def create_dice2():
        dice = list()
        dice.append(draw_dice2('dot0')) 
        dice.append(draw_dice2('dot4'))  
        dice.append(draw_dice2('dot3', 'dot5'))  
        dice.append(draw_dice2('dot2', 'dot4', 'dot6'))  
        dice.append(draw_dice2('dot1', 'dot2', 'dot6', 'dot9'))  
        dice.append(draw_dice2('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))  
        dice.append(draw_dice2('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9')) 
        return dice

    def draw_dice2(*args):
        
        w, h = 250, 250 
        x, y, r = 20, 20, 50
        c = tk.Canvas(root, width=w, height=h, bg=col2) 
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)

        return c

    def click2():
        dice_list2 = create_dice2()
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
        t = 100 
        stop = randint(13, 18)
        for x in range(stop):
            dice_index = x % 6 + 1
            dice_list2[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list2[dice_index].grid_forget()) 
            t += 20

    def click():
        dice_list = create_dice()
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)
      

        t = 100
        stop = randint(13, 18)  
        for x in range(stop):
            dice_index = x % 6 + 1 
            dice_list[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list[dice_index].grid_forget()) 
            t += 20

    def create_dice3():
        dice = list()
        dice.append(draw_dice3('dot0')) 
        dice.append(draw_dice3('dot4'))  
        dice.append(draw_dice3('dot3', 'dot5'))
        dice.append(draw_dice3('dot2', 'dot4', 'dot6'))
        dice.append(draw_dice3('dot1', 'dot2', 'dot6', 'dot9'))
        dice.append(draw_dice3('dot1', 'dot2', 'dot4', 'dot6', 'dot9')) 
        dice.append(draw_dice3('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))
        return dice

    def draw_dice3(*args):

        
        w, h = 250, 250 
        x, y, r = 20, 20, 50
        c = tk.Canvas(root, width=w, height=h, bg=col3)
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)

        return c

    def click3():
        dice_list3 = create_dice3()
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

        t = 100
        stop = randint(13, 18)
        for x in range(stop):
            dice_index = x % 6 + 1
            dice_list3[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list3[dice_index].grid_forget())
            t += 20

    def create_dice4():
        dice = list()
        dice.append(draw_dice4('dot0'))
        dice.append(draw_dice4('dot4'))
        dice.append(draw_dice4('dot3', 'dot5'))
        dice.append(draw_dice4('dot2', 'dot4', 'dot6'))
        dice.append(draw_dice4('dot1', 'dot2', 'dot6', 'dot9'))
        dice.append(draw_dice4('dot1', 'dot2', 'dot4', 'dot6', 'dot9'))
        dice.append(draw_dice4('dot1', 'dot2', 'dot3', 'dot5', 'dot6', 'dot9'))
        return dice

    def draw_dice4(*args):
        w, h = 250, 250 
        x, y, r = 20, 20, 50
        c = tk.Canvas(root, width=w, height=h, bg=col4)
        dots = {
            'dot0': lambda x, y, r: c,
            'dot1': lambda x, y, r: c.create_oval(x, y, x + r, y + r, fill='black'),
            'dot2': lambda x, y, r: c.create_oval(x + 160, y, (x + 160) + r, y + r, fill='black'),
            'dot3': lambda x, y, r: c.create_oval(x, y + 80, x + r, (y + 80) + r, fill='black'),
            'dot4': lambda x, y, r: c.create_oval(x + 80, (y + 80), (x + 80) + r, (y + 80) + r, fill='black'),
            'dot5': lambda x, y, r: c.create_oval(x + 160, (y + 80), (x + 160) + r, (y + 80) + r, fill='black'),
            'dot6': lambda x, y, r: c.create_oval(x, y + 160, x + r, (y + 160) + r, fill='black'),
            'dot9': lambda x, y, r: c.create_oval(x + 160, y + 160, (x + 160) + r, (y + 160) + r, fill='black')
        }

        for arg in args:
            dots.get(arg)(x, y, r)

        return c

    def click4():
        dice_list4 = create_dice4()
        winsound.PlaySound("Rolling Dice.wav",winsound.SND_FILENAME|winsound.SND_ASYNC)

        t = 100
        stop = randint(13, 18)
        for x in range(stop):
            dice_index = x % 6 + 1
            dice_list4[dice_index].grid(row=1, column=0, columnspan=3)
            root.update()
            if x == stop - 1:
                break
            root.after(t, dice_list4[dice_index].grid_forget())
            t += 20

    root = tk.Tk()
    root.title("DICE ROLL")
    root.geometry("250x460")
    root.config(bg='pink')
    dice_list = create_dice()
    dice_list2 = create_dice2()
    dice_list3 = create_dice3()
    dice_lstt4 = create_dice4()
    dice_list[0].grid(row=1, column=0, columnspan=3)

    labela = tk.Label(root, text=a, bg=col1, fg='black', width=16, font=('arial', 16, 'italic'))
    labela.place(x=0, y=270)
    labelb = tk.Label(root, text=b, bg=col2, fg='black', width=16, font=('arial', 16, 'italic'))
    labelb.place(x=0, y=305)
    labelc = tk.Label(root, text=c, bg=col3, fg='black', width=16, font=('arial', 16, 'italic'))
    labelc.place(x=0, y=340)
    labeld = tk.Label(root, text=d, bg=col4, fg='black', width=16, font=('arial', 16, 'italic'))
    labeld.place(x=0, y=375)

    button1 = tk.Button(root, text='Hit Me', bg=col1, fg='black', font=('arial', 11, 'bold'), command=click)
    button1.place(x=190, y=268)
    button2 = tk.Button(root, text='Hit Me', bg=col2, fg='black', font=('arial', 11, 'bold'), command=click2)
    button2.place(x=190, y=303)
    button3 = tk.Button(root, text='Hit Me', bg=col3, fg='black', font=('arial', 11, 'bold'), command=click3)
    button3.place(x=190, y=338)
    button4 = tk.Button(root, text='Hit Me', bg=col4, fg='black', font=('arial', 11, 'bold'), command=click4)
    button4.place(x=190, y=373)
    button5 = tk.Button(root, text="Quit", bg='brown', fg='white', font=('arial', 14, 'italic'), command=qu)
    button5.place(x=85, y=415)
    root.mainloop()

def abt():
    tkinter.messagebox.showinfo("Information", "This project was given by :\n"
                                           ".                          Mrs. Kshama Tiwari")
def abt1():
    tkinter.messagebox.showinfo("Information", "This project is submitted by :\n"
                                           ".                            Ayush Kesari\n"
                                           ".                            Arsalan Ahmad Quarashi\n"
                                           ".                            Arjun Singh\n"
                                           ".                            Arpita Kesharwani\n")
menu = Menu(window1)
window1.config(menu=menu,bg='pink')

subm1 = Menu(menu)
menu.add_cascade(label="File", menu=subm1)
subm1.add_command(label="New")
subm1.add_command(label="Open")
subm1.add_command(label="Save")
subm1.add_command(label="Save As")
subm1.add_command(label="Exit", command=qu)

subm2 = Menu(menu)
menu.add_cascade(label="About", menu=subm2)
subm2.add_command(label="Given By", command=abt)
subm2.add_command(label="Done By", command=abt1)


label1 = Label(window1, text="WELCOME", relief='solid', width=500, font=('arial', 30, 'bold'), fg='white', bg='red')
label1.pack()

label2 = Label(window1, text="Select Number Of Players", relief='solid', width=40, font=('arial', 20, 'bold'),
               fg='white', bg='blue')
label2.pack()

list1 = ['   1 Player', '   2 Player', '   3 Player', '   4 Player']
droplist = OptionMenu(window1, var, *list1)
var.set("  Select Player")
droplist.config(width=20, height=2, font=('arial', 14, 'bold'), bg='green')
droplist.place(x=80, y=120)

b1 = Button(window1, text="Done", width=12, bg='brown', fg='white', font=('arial', 14, 'italic'), command=name)
b1.place(x=120, y=200)



window1.mainloop()

