from tkinter import *
import numpy as np
from numpy import linalg

win = Tk()
win.geometry("600x400")
win.resizable(0, 0)
win.title("Calculator")

siz = 0
sizx = 0


def size1(n):
    global siz
    siz = n

    # Reset the background color of all buttons
    for button in [b1, b2, b3, b4, b5]:
        button.configure(bg="SystemButtonFace")

    # Change the background color of the selected button
    if n == 1:
        b1.configure(bg="#6BD0FF")
    elif n == 2:
        b2.configure(bg="#6BD0FF")
    elif n == 3:
        b3.configure(bg="#6BD0FF")
    elif n == 4:
        b4.configure(bg="#6BD0FF")
    elif n == 5:
        b5.configure(bg="#6BD0FF")


def size2(n):
    global sizx
    sizx = n

    # Reset the background color of all buttons
    for button in [c1, c2, c3, c4]:
        button.configure(bg="SystemButtonFace")

    # Change the background color of the selected button
    if n == 1:
        c1.configure(bg="#6BD0FF")
        calc(1)
    elif n == 2:
        c2.configure(bg="#6BD0FF")
        calc(2)
    elif n == 3:
        c3.configure(bg="#6BD0FF")
        calc(3)
    elif n == 4:
        c4.configure(bg="#6BD0FF")
        calc(4)


def calc(cal):
    if siz != 0 and sizx != 0:
        new_window = Tk()
        new_window.geometry("400x300")
        new_window.resizable(0, 0)
        new_window.title("Answer")
        new_window.configure(bg='#6BD0FF')

        inp = inputtxt.get(1.0, "end-1c")
        inp1 = inputtxt1.get(1.0, "end-1c")
        print(inp)
        ls = inp.split(",")
        ls1 = inp1.split(",")
        a = []
        b = []
        for i in ls:
            print(i)
            a.append(int(i))
        for j in ls1:
            b.append(int(j))
        # print(a,b)
        a = np.array(a)
        b = np.array(b)
        if cal == 1:
            l10 = Label(new_window, text="The Inner product is: " + str(np.inner(a, b)), font=('Arial 10 bold'))
            l10.place(relx=0.10, rely=0.30)
        if cal == 2:
            l10 = Label(new_window, text="The Outer product is:\n " + str(np.outer(a, b)), font=('Arial 10 bold'))
            l10.place(relx=0.10, rely=0.30)
        if cal == 3:
            l10 = Label(new_window, text="The Matrix product is: " + str(np.matmul(a, b)), font=('Arial 10 bold'))
            l10.place(relx=0.10, rely=0.30)
        if cal == 4:
            l10 = Label(new_window, text="The dot product is: " + str(np.dot(a, b)), font=('Arial 10 bold'))
            l10.place(relx=0.10, rely=0.30)


labelframe = LabelFrame(win, text="Matrix Calculator", font=('Century 20 bold'), labelanchor="n", bd=5, bg="black",
                        width=600, height=450, fg="white")
labelframe.pack(expand=True, fill=BOTH)

l1 = Label(labelframe, text="Matrix size", font=('Arial 18 bold'))
l1.place(relx=0.05, rely=0.10)

b1 = Button(labelframe, text="1*1", font=10, width=7, command=lambda: size1(1))
b2 = Button(labelframe, text="2*2", font=10, width=7, command=lambda: size1(2))
b3 = Button(labelframe, text="3*3", font=10, width=7, command=lambda: size1(3))
b4 = Button(labelframe, text="4*4", font=10, width=7, command=lambda: size1(4))
b5 = Button(labelframe, text="5*5", font=10, width=7, command=lambda: size1(5))

b1.place(relx=0.10, rely=0.30)
b2.place(relx=0.10, rely=0.40)
b3.place(relx=0.10, rely=0.50)
b4.place(relx=0.10, rely=0.60)
b5.place(relx=0.10, rely=0.70)

l1 = Label(labelframe, text="Enter comma separated values for:", font=('Arial 10 bold'))
l1.place(relx=0.45, rely=0.10)
l1 = Label(labelframe, text="Matrix 1", font=('Arial 10 bold'))
l1.place(relx=0.45, rely=0.25)
l1 = Label(labelframe, text="Matrix 2", font=('Arial 10 bold'))
l1.place(relx=0.45, rely=0.47)

inputtxt = Text(win, height=2, width=25)
inputtxt.place(relx=0.60, rely=0.30)
inputtxt1 = Text(win, height=2, width=25)
inputtxt1.place(relx=0.60, rely=0.50)

canvas = Canvas(labelframe)
canvas.place(relx=0.35, rely=0.05, relwidth=0.005, relheight=0.95)
canvas = Canvas(labelframe)
canvas.place(relx=0.35, rely=0.70, relwidth=0.90, relheight=0.005)

c1 = Button(labelframe, text="Inner product", font=10, width=17, command=lambda: size2(1))
c2 = Button(labelframe, text="Outer product", font=10, width=17, command=lambda: size2(2))
c3 = Button(labelframe, text="Matrix product", font=10, width=17, command=lambda: size2(3))
c4 = Button(labelframe, text="Dot", font=10, width=17, command=lambda: size2(4))

c1.place(relx=0.70, rely=0.85)
c2.place(relx=0.40, rely=0.75)
c3.place(relx=0.70, rely=0.75)
c4.place(relx=0.40, rely=0.85)

win.mainloop()
