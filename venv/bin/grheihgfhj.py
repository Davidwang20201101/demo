# import tkinter
# from tkinter import ttk
# import datetime
#
# now = datetime.datetime.now()
# print(now)
# solar_month = [1,3,5,7,8,10,12]
# lunar_month = [4,6,9,11]
#
# def cal1():
#     global a,b,c,someday
#     a=int(text1.get('1.0',tkinter.END))
#     b=int(com.get())
#     c=int(com1.get())
#     someday = datetime.datetime(a,b,c)
#     r = abs((someday-now).days)
#     textr.delete('1.0',tkinter.END)
#     textr.insert(tkinter.END,str(r))
# win = tkinter.Tk()
# win.geometry("500x300+200+20")  # #窗口位置500后面是字母x
#
# '''
# 下拉菜单
# '''
# xVariable = tkinter.StringVar()  # #创建变量，便于取值
# x1V = tkinter.StringVar()
# labelx1 = tkinter.Label(win,text='第一组日期：')
# labelx1.grid(row=0,column=0)
# text1 = tkinter.Text(win,width=10,height=2)
# text1.grid(row=1,column=0)
# label0 = tkinter.Label(win,text='年')
# label0.grid(row=1,column=1)
# label1 = tkinter.Label(win,text='月')
# label1.grid(row=1,column=3)
# com = tkinter.ttk.Combobox(win, textvariable=xVariable,width=5)  # #创建下拉菜单
# com.grid(row=1,column=2)  # #将下拉菜单绑定到窗体
# com['value']=[1,2,3,4,5,6,7,8,9,10,11,12]# #给下拉菜单设定值
# com.current(1)
#
# max = 0
# com1 = tkinter.ttk.Combobox(win, textvariable=x1V,width=5)
# com1.grid(row=1,column=4)
# label2 = tkinter.Label(win,text='日')
# label2.grid(row=1,column=5)
#
#
# button1 = tkinter.Button(win,text='计算第一组按钮与今天日期差距',command=cal1)
# button1.grid(row=2,column=6)
# textr = tkinter.Text(win,width=5,height=1)
# textr.grid(row=2,column=7)
#
# def xFunc(event):
#     global max
#     # print(com.get())  # #获取选中的值方法1
#     # print(xVariable.get())  # #获取选中的值方法2
#     if int(com.get()) in solar_month:
#         print('in solar ')
#         max = 32
#     elif int(com.get()) in lunar_month:
#         max = 31
#     elif int(com.get()) == 2:
#         max = 29
#     com1['value'] = list(range(1,max))
#
# # print(type(max))
#
# com.bind("<<ComboboxSelected>>", xFunc)  # #给下拉菜单绑定事件
#
# win.mainloop()  # #窗口持久化

