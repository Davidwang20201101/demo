# names =['Lihua','Rain','Jack','Xiuxiu','Peiqi','Black']
# print('My friend is '+names[2].title())
# names.append('added')
# names.insert(1,'Jack')
# print('My friend is '+names[2].title())
# print(names)
# del names[3]
# print('names')
# B
# A
# B
# C
# D
# A
# B
# B
# D
# C
# A
# D
# C
# B
# C
# C
# C
# C
# C
# C
# fa/ lse/
# True
# False
# False
# False
# True
# True
# True
# False
# 无解
#
# 一次
# 1，11，2
# 一个等号代表的含义是赋值，两个等号代表判断两值是否相等

# meuns有：['mushrooms', 'olives', 'green peppers','pepperoni','pineapple', 'extra cheese']
# orders有： ['mushrooms','french fries','extra cheese']
# 把oder放到orders里面
# 如果orders里的东西在meuns里面的话
# 打印我们有order加句号
# 如果没有，
# 就打印对不起我们没有order加句号。

# 可以有不同的顺序。
#！-*- coding:utf-8 -*-

# names = ["Lihua","Rain","Jack","Xiuxiu","Peiqi","Black"]
# names.insert(-1,"Blue")
# names[names.index("Xiuxiu")] = "秀秀"
# names.insert(2,["oldboy","oldgirl"])
# print(names.index("Peiqi"))
# numbers = [1,2,3,4,2,5,6,2]
# names.extend(numbers)
# print(names)
#
# for index,i in enumerate(names):
#     if index%2==0:
#         names[index] = -1
#         print(index,i)
# print(names)

from tkinter import *

def Calculate():
     a1 = int(text1.get('1.0',END))
     a2 = int(text2.get('1.0',END))
     a3 =a1+a2
     text3.delete('1.0',END)
     text3.insert(INSERT,a3)

root = Tk()
root.title('DVD')
lable1 = Label(root, text='Frist Number:')
lable1.grid (row=0,column=0)
text1 = Text(root,width=30,height=1)
text1.grid(row=1,column=0)
label2= Label(root,text='Second Number:')
label2.grid(row=2,column=0)
text2 = Text(root,width=30,height=1)
text2.grid (row=3,column=0)
lable3 = Label(root, text='Result:')
lable3.grid(row=4,column=0)
text3 = Text(root,width=30,height=1)
text3.grid(row=5,column=0)
button1 = Button(root, text='Calulate',command=Calculate)
button1. grid (row=6,column=0)
mainloop()



