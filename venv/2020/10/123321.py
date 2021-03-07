# import time
# import datetime
# import pyautogui
# start1 = time.perf_counter()
# start = datetime.datetime.now()
#
# pyautogui.FAILSAFE = True
# a, b = pyautogui.position()
# m, n = pyautogui.size()
# print(a, b)
# pyautogui.hotkey('ctrl', 's')
# pyautogui.hotkey('ctrl', 'home')
# pyautogui.moveTo(x=365, y=536)
# pyautogui.click(x=365, y=536, click=1, button='left')
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.moveTo(x=660, y=1057)
# pyautogui.click(x=660, y=1057, click=1, button='left')
# pyautogui.moveTo(x=113, y=119)
# pyautogui.click(x=113, y=119, click=1, button='left')
# pyautogui.moveTo(x=88, y=200)
# pyautogui.click(x=88, y=200, click=1, button='left')


# from tkinter  import *
# import time
#
#
# class StopWatch(Frame):
#     '''实现一个秒表部件'''
#     msec = 50
#
#     def __init__(self, parent=None, **kw):
#         Frame.__init__(self, parent, kw)
#         self._start = 0.0
#         self._elapsedtime = 0.0
#         self._running = False
#         self.timestr = StringVar()
#         self.makeWidgets()
#         self.flag = True
#
#     def makeWidgets(self):
#         '''制作时间标签'''
#         l = Label(self, textvariable=self.timestr)
#         self._setTime(self._elapsedtime)
#         l.pack(fill=X, expand=NO, pady=2, padx=2)
#
#     def _update(self):
#         self._elapsedtime = time.time() - self._start
#         self._setTime(self._elapsedtime)
#         self._timer = self.after(self.msec, self._update)
#
#     def _setTime(self, elap):
#         '''将时间格式改为 分：秒：百分秒'''
#         minutes = int(elap / 60)
#         seconds = int(elap - minutes * 60.0)
#         hseconds = int((elap - minutes * 60.0 - seconds) * 100)
#         self.timestr.set('%2d:%2d:%2d' % (minutes, seconds, hseconds))
#
#     def Start(self):
#         if not self._running:
#             self._start = time.time() - self._elapsedtime
#             self._update()
#             self._running = True
#
#     def Stop(self):
#         '''停止秒表'''
#         if self._running:
#             self.after_cancel(self._timer)
#             self._elapsedtime = time.time() - self._start
#             self._setTime(self._elapsedtime)
#             self._running = False
#
#     def Reset(self):
#         '''重设秒表'''
#         self._start = time.time()
#         self._elapsedtime = 0.0
#         self._setTime(self._elapsedtime)
#
#     def stopwatch(self):
#         if self.flag == True:
#             self.pack(side=TOP)
#             Button(self, text='start', command=self.Start).pack(side=LEFT)
#             Button(self, text='stop', command=self.Stop).pack(side=LEFT)
#             Button(self, text='reset', command=self.Reset).pack(side=LEFT)
#             Button(self, text='quit', command=self.quit).pack(side=LEFT)
#         self.flag = False
#
#
# class Watch(Frame):
#     msec = 1000
#
#     def __init__(self, parent=None, **kw):
#         Frame.__init__(self, parent, kw)
#         self._running = False
#         self.timestr1 = StringVar()
#         self.timestr2 = StringVar()
#         self.makeWidgets()
#         self.flag = True
#
#     def makeWidgets(self):
#         l1 = Label(self, textvariable=self.timestr1)
#         l2 = Label(self, textvariable=self.timestr2)
#         l1.pack()
#         l2.pack()
#
#     def _update(self):
#         self._settime()
#         self.timer = self.after(self.msec, self._update)
#
#     def _settime(self):
#         today1 = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))
#         time1 = str(time.strftime('%H:%M:%S', time.localtime(time.time())))
#         self.timestr1.set(today1)
#         self.timestr2.set(time1)
#
#     def start(self):
#         self._update()
#         self.pack(side=TOP)
#
#
# if __name__ == '__main__':
#     def main():
#         root = Tk()
#         root.geometry('250x150')
#         frame1 = Frame(root)
#         frame1.pack(side=BOTTOM)
#         sw = StopWatch(root)
#         stpwtch = Button(frame1, text='秒表', command=sw.stopwatch)
#         stpwtch.pack(side=RIGHT)
#         mw = Watch(root)
#         mywatch = Button(frame1, text='时钟', command=mw.start)
#         mywatch.pack(side=LEFT)
#         root.mainloop()
#
#
#     main()
# from tkinter  import *
#
#
# from datetime import datetime
# now = datetime.now()
# def f1():
#     a1 = int(text1.get('1.0', END))
#     a2 = int(text2.get('1.0', END))
#     a3 = int(text3.get('1.0', END))
#
#     dt = datetime(a1,a2,a3)
#     r = dt - now
#     text3.delete('1.0', END)
#     text3.insert(INSERT, r)
# print(now)
#
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
# from datetime import datetime
# t = 1429417200.0
# print(datetime.fromtimestamp(t))

# timestamp =  1970-1-1 00:00:00 UTC+0:00
#
# timestamp = 1970-1-1 08:00:00 UTC+8:00
#
# from datetime import datetime, timedelta
# now = datetime.now()
# now
# datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
# now + timedelta(hours=10)
# datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
# now - timedelta(days=1)
# datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
# now + timedelta(days=2, hours=12)
# datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)

# '''from tkinter import *
# from datetime import *
# from  tkinter  import ttk
# def Subtract_from_Current():
#     a1 = int(text1.get('1.0', END))
#     a2 = int(text2.get('1.0', END))
#     a3 = int(text3.get('1.0', END))
#     dt1 = date(a1,a2,a3)
#     Result = (date.today() - dt1).days
#     text7.delete('1.0', END)
#     text7.insert(INSERT, Result)
#
# def Subtract_from_Input():
#     a1 = int(text1.get('1.0', END))
#     a2 = int(text2.get('1.0', END))
#     a3 = int(text3.get('1.0', END))
#     a4 = int(text4.get('1.0', END))
#     a5 = int(text5.get('1.0', END))
#     a6 = int(text6.get('1.0', END))
#     dt1 = date(a1,a2,a3)
#     dt2 = date(a4,a5,a6)
#     Result = abs((dt2 - dt1).days)
#     text7.delete('1.0', END)
#     text7.insert(INSERT, Result)
#
# root = Tk()
# root.title("David's date calculator")
# label1 = Label(root, text='First Year')
# label1.grid(row=0, column=0)
# text1 = Text(root, width=20, height=1)
# text1.grid(row=1, column=0)
# label2 = Label(root, text='First Month')
# label2.grid(row=0, column=1)
# text2 = Text(root, width=20, height=1)
# text2.grid(row=1, column=1)
# label3 = Label(root, text='First Day')
# label3.grid(row=0, column=2)
# text3 = Text(root, width=20, height=1)
# text3.grid(row=1, column=2)
# label4 = Label(root, text='Second Year')
# label4.grid(row=2, column=0)
# text4 = Text(root, width=20, height=1)
# text4.grid(row=3, column=0)
# label5 = Label(root, text='Second Month')
# label5.grid(row=2, column=1)
# text5 = Text(root, width=20, height=1)
# text5.grid(row=3, column=1)
# label6 = Label(root, text='Second Day')
# label6.grid(row=2, column=2)
# text6 = Text(root, width=20, height=1)
# text6.grid(row=3, column=2)
# label7 = Label(root, text='Difference')
# label7.grid(row=0, column=3)
# text7 = Text(root, width=20, height=1)
# text7.grid(row=1, column=3)
# Button1 = Button(root, width=20, height=1, text='From Current', command=Subtract_from_Current)
# Button1.grid(row=4, column=0)
# Button2 = Button(root, width=20, height=1, text='From Input', command=Subtract_from_Input)
# Button2.grid(row=4, column=1)
'''# name = StringVar()
# players =ttk.Combobox(root, textvariable=name)["values"] = ('First Year', 'First Month', 'First Day', 'Second Year', 'Second Month', 'Second Day' )
# players.current(0)
# comvalue = tkinter.StringVar()
# comboxlist = ttk.Combobox(win, textvariable=comvalue)
# com["values"] = list (range(1,31))
# comboxlist.current(0)
# comboxlist.bind("<<ComboboxSelected>>", go)
# comboxlist.pack()
# win.mainloop()
# players.bind("<<ComboboxSelected>>", show_msg)
# players.pack()
# max =0
# com1 ==ttk.Combobox(win,textvariable=x1v)
# com1.pack()
#
# def xFunc(event)
#     global max
# l1=['1','3','5','7','8','10','12']
# if month in l1:
#     day = 31
# import tkinter
# from tkinter import ttk
#
# solar_month = [1,3,5,7,8,10,12]
# lunar_month = [4,6,9,11]
#
# win = tkinter.Tk()
# win.geometry("500x300+200+20")
#
# '''
# 下拉菜单
# '''
# xVariable = tkinter.StringVar()
# x1V = tkinter.StringVar()
#
# com = ttk.Combobox(win, textvariable=xVariable)
# com.pack()
# com["value"] = [1,2,3,4,5,6,7,8,9,10,11,12]
# com.current(0)
#
# max = 0
# com1 = ttk.Combobox(win, textvariable=x1V)
# com1.pack()
#
# def xFunc(event):
#     global max
#         # print(com.get())
#         # print(xVariable.get())
#     if int(com.get()) in solar_month:
#         print('in solar ')
#         max = 32
#     elif int(com.get()) in lunar_month:
#         max = 31
#     elif int(com.get()) == 2:
#         max = 29
# com1['value'] = list(range(1,max))
#
# print(type(max))
#
# com.bind("<<ComboboxSelected>>", xFunc)
#
# from datetime import datetime
# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))
# ('Mon, May 05 16:28')
#
# win.mainloop()

import tkinter
from tkinter import ttk
import datetime

now = datetime.datetime.now()
print(now)
solar_month = [1,3,5,7,8,10,12]
lunar_month = [4,6,9,11]

def cal1():
    global a,b,c,someday
    a=int(text1.get('1.0',tkinter.END))
    b=int(com.get())
    c=int(com1.get())
    someday = datetime.datetime(a,b,c)
    r = abs((someday-now).days)
    textr.delete('1.0',tkinter.END)
    textr.insert(tkinter.INSERT,r)
win = tkinter.Tk()
win.geometry("500x300+200+20")

'''
下拉菜单
'''
xVariable = tkinter.StringVar()
x1V = tkinter.StringVar()
labelx1 = tkinter.Label(win,text='第一组日期：')
labelx1.grid(row=0,column=0)
text1 = tkinter.Text(win,width=10,height=2)
text1.grid(row=1,column=0)
label0 = tkinter.Label(win,text='年')
label0.grid(row=1,column=1)
label1 = tkinter.Label(win,text='月')
label1.grid(row=1,column=3)
com = tkinter.ttk.Combobox(win, textvariable=xVariable,width=5)
com.grid(row=1,column=2)
com['value']=[1,2,3,4,5,6,7,8,9,10,11,12]
com.current(1)

max = 0
com1 = tkinter.ttk.Combobox(win, textvariable=x1V,width=5)
com1.grid(row=1,column=4)
label2 = tkinter.Label(win,text='日')
label2.grid(row=1,column=5)


button1 = tkinter.Button(win,text='计算第一组按钮与今天日期差距',command=cal1)
button1.grid(row=2,column=6)
textr = tkinter.Text(win,width=5,height=1)
textr.grid(row=2,column=7)

def xFunc(event):
    global max
    # print(com.get())  # #获取选中的值方法1
    # print(xVariable.get())  # #获取选中的值方法2
    if int(com.get()) in solar_month:
        print('in solar ')
        max = 32
    elif int(com.get()) in lunar_month:
        max = 31
    elif int(com.get()) == 2:
        max = 29
    com1['value'] = list(range(1,max))

# print(type(max))

com.bind("<<ComboboxSelected>>", xFunc)

win.mainloop()

