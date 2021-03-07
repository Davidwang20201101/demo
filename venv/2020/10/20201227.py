# import tkinter
# top=tkinter . Tk()
# lable = tkinter.Label(top,text='Hello world')
# lable .pack()
# tkinter.mainloop()

# import tkinter
# top=tkinter . Tk()
#
# lable = tkinter.Label(top,text='Kuga',width=90,height=5,bg="red",font=("Arial",12))
# lable .pack()
#
# lable = tkinter.Label(top,text='Agito',width=90,height=5,bg="orange",font=("Arial",12))
# lable .pack()
#
# lable = tkinter.Label(top,text='Ryuki',width=90,height=5,bg="yellow",font=("Arial",12))
# lable .pack()
#
# tkinter.mainloop()

# from tkinter import *
#
# def Calculate():
#     a1 = int(text1.get('1.0',END))
#     a2 = int(text2.get('1.0',END))
#     a3 =a1+a2
#     text3.delete('1.0',END)
#     text3.insert(INSERT,a3)
# root = Tk()
# root.title('My title')
# lable1 = Label(root, text='Frist Number:')
# lable1.grid (row=0,column=0)
# text1 = Text(root,width=30,height=1)
# text1.grid(row=1,column=0)
# label2= Label(root,text='Second Number:')
# label2.grid(row=2,column=0)
# text2 = Text(root,width=30,height=1)
# text2.grid (row=3,column=0)
# lable3 = Label(root, text='Result:')
# lable3.grid(row=4,column=0)
# text3 = Text(root,width=30,height=1)
# text3.grid(row=5,column=0)
# button1 = Button(root, text='Calulate',command=Calculate)
# button1. grid (row=6,column=0)
# mainloop()
# from tkinter import *
# def Add():
#     a1 = int(text1.get('1.0', END))#从行首取到行尾
#     a2 = int(text2.get('1.0', END))
#     a3 = a1 + a2
#     text3.delete('1.0', END)
#     text3.insert(INSERT, a3)
# def Subtract():
#     a1 = int(text1.get('1.0', END))
#     a2 = int(text2.get('1.0', END))
#     a3 = a1 - a2
#     text3.delete('1.0', END)
#     text3.insert(INSERT, a3)
# def Divide():
#     a1 = int(text1.get('1.0', END))
#     a2 = int(text2.get('1.0', END))
#     a3 = a1 / a2
#     text3.delete('1.0', END)
#     text3.insert(INSERT, a3)
# def Multiply():
#     a1 = int(text1.get('1.0', END))
#     a2 = int(text2.get('1.0', END))
#     a3 = a1 * a2
#     text3.delete('1.0', END)
#     text3.insert(INSERT, a3)
# root = Tk()
# root.title("Jason's Calculator")
# label1 = Label(root, text='First Number:')
# label1.grid(row=0, column=0)
# text1 = Text(root, width=30, height=1)
# text1.grid(row=1, column=0)
# label2 = Label(root, text='Second Number:')
# label2.grid(row=2, column=0)
# text2 = Text(root, width=30, height=1)
# text2.grid(row=3, column=0)
# label3 = Label(root, text='Result:')
# label3.grid(row=4, column=0)
# text3 = Text(root, width=30, height=1)
# text3.grid(row=5, column=0)
# button1 = Button(root, width=30, height=1, text='Add', command=Add)
# button1.grid(row=6, column=0)
# button2 = Button(root, width=30, height=1, text='Subtract', command=Subtract)
# button2.grid(row=7, column=0)
# button3 = Button(root, width=30, height=1, text='Divide', command=Divide)
# button3.grid(row=8, column=0)
# button4 = Button(root, width=30, height=1, text='Multiply', command=Multiply)
# button4.grid(row=9, column=0)
# mainloop() 

from tkinter import *
import math

class calculator():

    def __init__(self):
        global tk
        tk = Tk ()
        tk.geometry('480 x 500')
        tk.title('计算器')

        show = Frame(width=600,height=300,bg='#dddddd')
        show.pack
        self.sv = StringVar()
        self.sv.set('初始状态')

        show_label=Label(show,textvariable=self.sv, bg='#eeeeee',width=34,height=4,font=('黑体',18,'bold') ,justify=LEET, anchor='e')
        show_label.pack(padx=10,pady=10)

        k_area = Frame(width=600,height=350,bg='cccccc')
        k_area.pack()
