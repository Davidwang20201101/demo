# message = "hello world"
# print ( message )

# a=1
# b=4
# c=a+b
# print (c)
# =  5

# a='1'
# b='4'
# c=a+b
# print (c)
# =  14

# str
# float
# int

# name = 'david'
# print(name.title())

# first_name ='ada'
# last_name = 'lovelace'
# full_name = first_name + ' ' + last_name
# print(full_name)

# first_name ='ada'
# last_name = 'lovelace'
# full_name = first_name + ' ' + last_name
# print(full_name.title())

# first_name ='ada'
# last_name = 'lovelace'
# full_name = first_name + ' ' + last_name
# print(full_name.title()+'hello!')

# a=0.1
# b=0.2
# print(a+b)

# 0 000
# 1 001
# 2 010
# 3 011
# 4 100
# 5 101
# 6 110
# 7 111
# 8 1000
# 9 1001

# a=3
# b=0.1
# print(a*b)

# bicycles = ['giant','BGM','GoodBoy']
# print(bicycles)

# bicycles = ['giant','BGM','GoodBoy']
# print(bicycles[1])

# bicycles = ['giant','BGM','GoodBoy']
# print(bicycles[0])

# bicycles = ['giant','BGM','GoodBoy']
# print('My First Bicycle is a ' + bicycles[-1].title())

# bicycles = ['giant','BGM','GoodBoy']

# bicycles[-1]='yamaha'

# print(bicycles)

# bicycles = ['giant','BGM','GoodBoy']
# print('My First Bicycle is a ' + bicycles[-1].title())
# bicycles.append('added')
# print('My First Bicycle is a ' + bicycles[-1].title())
# print(bicycles)

# bicycles = ['giant','BGM','GoodBoy']
# print('My First Bicycle is a ' + bicycles[-1].title())
# bicycles.append('added')
# bicycles.insert(0,'new brand')
# print('My First Bicycle is a ' + bicycles[-1].title())
# print(bicycles)
# 添加

# bicycles = ['giant','BGM','GoodBoy']
# print('My First Bicycle is a ' + bicycles[-1].title())
# del bicycles[-2]
# print(bicycles)
# 删除

# bicycles = ['Giant','BGM','GoodBoy']
# print('My First Bicycle is a ' + bicycles[-1].title())
# popped_bicycles=bicycles.pop()
# print(bicycles)
# 删除末尾

# FI 先进 frist in
# LO 后出 last out

# bicycles = ['giant','BGM','GoodBoy']
#            [   0       1      2    ]

from tkinter import *

def Calculate():
     a1 = int(text1.get('1.0',END))
     a2 = int(text2.get('1.0',END))
     a3 =a1+a2
     text3.delete('1.0',END)
     text3.insert(INSERT,a3)
from tkinter import *
def Add():
    a1 = int(text1.get('1.0', END))#从行首取到行尾
    a2 = int(text2.get('1.0', END))
    a3 = a1 + a2
    text3.delete('1.0', END)
    text3.insert(INSERT, a3)
def Subtract():
    a1 = int(text1.get('1.0', END))
    a2 = int(text2.get('1.0', END))
    a3 = a1 - a2
    text3.delete('1.0', END)
    text3.insert(INSERT, a3)
def Divide():
    a1 = int(text1.get('1.0', END))
    a2 = int(text2.get('1.0', END))
    a3 = a1 / a2
    text3.delete('1.0', END)
    text3.insert(INSERT, a3)
def Multiply():
    a1 = int(text1.get('1.0', END))
    a2 = int(text2.get('1.0', END))
    a3 = a1 * a2
    text3.delete('1.0', END)
    text3.insert(INSERT, a3)
root = Tk()
root.title('我的乘法计算器')
label1 = Label(root, text='First Number:')
label1.grid(row=0, column=0)
text1 = Text(root, width=30, height=1)
text1.grid(row=1, column=0)
label2 = Label(root, text='Second Number:')
label2.grid(row=2, column=0)
text2 = Text(root, width=30, height=1)
text2.grid(row=3, column=0)
label3 = Label(root, text='Result:')
label3.grid(row=4, column=0)
text3 = Text(root, width=30, height=1)
text3.grid(row=5, column=0)
button1 = Button(root, width=30, height=1, text='Add', command=Add)
button1.grid(row=6, column=0)
button2 = Button(root, width=30, height=1, text='Subtract', command=Subtract)
button2.grid(row=7, column=0)
button3 = Button(root, width=30, height=1, text='Divide', command=Divide)
button3.grid(row=8, column=0)
button4 = Button(root, width=30, height=1, text='Multiply', command=Multiply)
button4.grid(row=9, column=0)
mainloop()