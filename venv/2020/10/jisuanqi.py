from tkinter import *
import math

class calculator():


    def __init__(self):
        global tk
        tk = Tk ()
        tk.geometry('480x500')
        tk.title('计算器')

        show = Frame(width=600,height=300,bg='#dddddd')
        show.pack()
        self.sv = StringVar()
        self.sv.set('初始状态')

        show_label=Label(show,textvariable=self.sv, bg='#eeeeee',width=34,height=4,font=('黑体',18,'bold') ,justify=LEFT, anchor='e')
        show_label.pack(padx=10,pady=10)

        k_area = Frame(width=600,height=350,bg='#cccccc')
        k_area.pack()

        self.num1 = ''
        self.num2 = ''
        self.pms1 = []
        self.pms2 = []
        self.num1_list = []
        self.num2_list = []
        self.operate = []

        w=5
        h=1

        key_1 = Button(k_area, text='1',width=w,height=h,command=lambda: self.num_in('1'),bg='white',font=('黑体',30,'bold'))
        key_1.grid(row=1,column=0)
        key_2 = Button(k_area, text='2',width=w,height=h,command=lambda: self.num_in('2'),bg='white',font=('黑体',30,'bold'))
        key_2.grid(row=1,column=1)
        key_3 = Button(k_area, text='3',width=w,height=h,command=lambda: self.num_in('3'),bg='white',font=('黑体',30,'bold'))
        key_3.grid(row=1,column=2)
        key_4 = Button(k_area, text='4',width=w,height=h,command=lambda: self.num_in('4'),bg='white',font=('黑体',30,'bold'))
        key_4.grid(row=2,column=0)
        key_5= Button(k_area, text='5',width=w,height=h,command=lambda: self.num_in('5'),bg='white',font=('黑体',30,'bold'))
        key_5.grid(row=2,column=1)
        key_6= Button(k_area, text='6',width=w,height=h,command=lambda: self.num_in('6'),bg='white',font=('黑体',30,'bold'))
        key_6.grid(row=2,column=2)
        key_7= Button(k_area, text='7',width=w,height=h,command=lambda: self.num_in('7'),bg='white',font=('黑体',30,'bold'))
        key_7.grid(row=3,column=0)
        key_8= Button(k_area, text='8',width=w,height=h,command=lambda: self.num_in('8'),bg='white',font=('黑体',30,'bold'))
        key_8.grid(row=3,column=1)
        key_9= Button(k_area, text='9',width=w,height=h,command=lambda: self.num_in('9'),bg='white',font=('黑体',30,'bold'))
        key_9.grid(row=3,column=2)
        key_0= Button(k_area, text='0',width=w,height=h,command=lambda: self.num_in('0'),bg='white',font=('黑体',30,'bold'))
        key_0.grid(row=4,column=1)
        key_point = Button(k_area,text='.',width=w,height=h,command=lambda: self.num_in('0'),bg='white',font=('黑体',30,'bold'))
        key_point.grid(row=4,column=2)
        key_pms = Button(k_area,text='±',width=w,height=h,command=lambda: self.num_in('0'),bg='white',font=('黑体',30,'bold'))
        key_pms.grid(row=3,column=3)
        key_close = Button(k_area, text='Close', width=w, height=h,bg='red', command=self.close, font=('黑体', 30, 'bold'))
        key_close.grid(row=4,column=0)
        key_plus = Button(k_area,text='+',width=w,height=h,command=lambda: self.num_in('+'),bg='white',font=('黑体',30,'bold'))
        key_plus.grid(row=1,column=3)
        key_minus = Button(k_area,text='-',width=w,height=h,command=lambda: self.num_in('-'),bg='white',font=('黑体',30,'bold'))
        key_minus.grid(row=2,column=3)
        key_multiply = Button(k_area,text='×',width=w,height=h,command=lambda: self.num_in('×'),bg='white',font=('黑体',30,'bold'))
        key_multiply.grid(row=0,column=2)
        key_divide = Button(k_area,text='÷',width=w,height=h,command=lambda: self.num_in('÷'),bg='white',font=('黑体',30,'bold'))
        key_divide.grid(row=0,column=1)
        key_equal = Button(k_area,text='=',width=w,height=h,command=lambda: self.num_in(''),bg='white',font=('黑体',30,'bold'))
        key_equal.grid(row=4,column=3)
        key_c = Button(k_area,text='Clear',width=w,height=h,command=lambda: self.num_in('0'),bg='white',font=('黑体',30,'bold'))
        key_c.grid(row=0,column=0)
        key_del = Button(k_area,text='←',width=w,height=h,command=lambda: self.num_in('0'),bg='white',font=('黑体',30,'bold'))
        key_del.grid(row=0,column=3)

        tk.mainloop()
    def pms(self):
        if self.operate == []:
            self.num1_pms()
        else:
            self.num2_pms()
    def num1_pms(self):
        if self.operate == []:
            self.pms1 = ['-']
            self.sv.set(self.pms1 + self.num1_list + self.operate +self.pms2 +self.num2_list )
        else:
            self.pms1 = []
            self.sv.set(self.pms1 + self.num1_list + self.operate +self.pms2 +self.num2_list )
    def num2_pms(self):
        if self.operate == []:
            self.pms2 = ['-']
            self.sv.set(self.pms1 + self.num1_list + self.operate +self.pms2 +self.num2_list )
        else:
            self.pms2 = []
            self.sv.set(self.pms1 + self.num1_list + self.operate +self.pms2 +self.num2_list )

    def num_in(self,n):
        if self.operate == []:
            self.num1_in(n)
        else:
            self.num2_in(n)

    def num1_in(self, n):
        if n == '.'and n in self.num1_list:
              pass
        else:
            self.num1_list.append(n)
            self.sv.set(self.pms1 + self.num1_list + self.operate + self.pms2 + self.num2_list)

    def num2_in(self,n):
        if n == '.' and n in self.num2_list:
            pass
        else:
           self.num2_list.append(n)
           self.sv.set(self.pms1 + self.num1_list + self.operate + self.pms2 + self.num2_list)

    def operate_in(self, op):
        if self == '.' and n in self.num2_list:
             pass
        else:
           self.num2_list.append(n)
           self.sv.set(self.pms1 + self.num1_list + self.operate + self.pms2 + self.num2_list)

    def data_empy(self):
        self.num1 = ''
        self.num2 = ''
        self.pms1 = []
        self.pms2 = []
        self.num1_list = []
        self.num2_list = []
        self.operate = []
        self.sv.set(self.pms1 + self.num1_list + self.operate + self.pms2 + self.num2_list)

    def str_delete(self):
        if self.num2_list   != []:
            l=len(self.num2_list)
            self.num2_list.remove(self.num1_list[l - 1])
            self.sv.set(self.pms1 +self.num1_list +self.operate + self.pms2 +self.num2_list)
        elif self.num2_list   != [] and self.pms2 != []:
             self.pms2 = []
             self.sv.set(self.pms1 +self.num1_list +self.operate + self.pms2 +self.num2_list)
        elif self.num2_list   != [] and self.pms2 ==[] and self.operate != []:
             self.operate = []
             self.sv.set(self.pms1 +self.num1_list +self.operate + self.pms2 +self.num2_list)
        elif self.operate == [] and self.num1_list   != []:
            l = len(self.num1_list[l -1])
            self.pms1 = []
            self.sv.set(self.pms1 + self.num1_list + self.operate + self.pms2 + self.num2_list)
        else:
            pass
    def num_pro(self,n):
        if n == self.num1:
            if self.pms1 !=[]:
                self.num1 =self.pms1[0]
            else:
                self.num1 = ''
            for i in self.num1_list:
                self.num1 += i
            if '.' in self.num1_list:
                self.num1 = float(self.num1)
            else:
                self.num1 = int(self.num1)
        else:
            if self.pms2 !=[]:
                self.num2 = self.pms2[0]
            else:
                self.num2=''
            for i in  self.num2_list:
                self.num2 +=i
            if'.'in self.num2_list:
                self.num2 = float(self.num2)
            else:
                self.num2 = int(self.num2)
    def result(self):
            if self.num2_list == [] or self.num2_list == ['.']:
                pass
            else:
                self.num_pro(self.num1)
                self.num_pro(self.num2)
                if self.operate ==['+']:
                    r = self.num1 + self.num2
                    self.data_empy()
                    self.num1_list = list(str(r))
                    self.sv.set(self.pms1 + self.num1_list + self.operate + self.pms2 + self.num2_list)

                elif self.operate == ['-']:
                    r= self.num1   -   self.num2
                    self.data_empy()
                    self. num1_list = list(str(r))
                    self.sv.set(self.pms1 + self.num1_list + self.operate + self.pms2 + self.num2_list)

                elif self.operate == ['×']:
                    r = self.num1 *  self.num2
                    self.data_empy()
                    self.num1_list = list(str(r))
                    self.sv.set(self.pms1 + self.num1_list + self.operate + self.pms2 + self.num2_list)

                elif self.operate == ['÷']:
                    try:
                       r = self.num1 /  self.num2
                       self.data_empy()
                       self.num1_list = list(str(r))
                       self.sv.set(self.pms1 + self.num1_list + self.operate + self.pms2 + self.num2_list)
                    except ZeroDivisionError:
                        self.sv.set('除数不能为0')
                    except Exception:
                        pass







    def close (self):
        tk.destroy()

if  __name__=='__main__':


     cc = calculator()




