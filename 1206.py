# 猴子吃桃问题：
# 猴子第一天吃了若干个桃子，当即吃了一半，还不解馋，又多吃了一个； 第二天，吃剩下的桃子的一半，还不过瘾，又多吃了一个；以后每天都吃前一天剩下的一半多一个，到第10天想再吃时，只剩下一个桃子了。问第一天共吃了多少个桃子？
# x=1
#
# for peach in range(9):
#        x=(x+1)*2
#        print(x)
# 1234四个数字，能组成那些3位数
# numbers=(1,2,3,4)
# for i in numbers:
#        for j in numbers:
#               for k in numbers:
#                      print(i,j,k)
# 1234四个数字，能组成那些个位相同3位数
# numbers=(1,2,3,4)
# for i in numbers:
#         for j in numbers:
#                for k in numbers:
#                       if(i!=j) and (i!=k) and(j!=k):
#                           print(i,j,k)
# "水仙花数"是一个 3 位数，它的每个位上的数字的 3次方之和等于它本身，是这个三位数本身。
# for i in range(1,10):
#     for j  in range(0,10):
#         for k in range(0,10):
#             if i*100+j*10+k== i**3 + j**3 +k ** 3:
#               print(i,j,k)
# "玫瑰花数"是一种四位数，它每一位上的四个数，每一个数的四次方之和，是这一四位数本身，找出所有的玫瑰花数
# for i in range(1,10):
#      for j  in range(0,10):
#          for k in range(0,10):
#              for n in range(0,10):
#                  if i*1000+j*100+k*10+n == i**4+j**4+k**4+n**4:
#                      print(i,j,k,n)
# 两个乒乓球队，各出三人，每人只比一场。甲队有abc三人，乙队有xyz三人。抽签决定比赛名单。a不和x比，c不和x和z比
# for i in range(0,3):
#     for j in range (0,3):
#         for k in range (0,3):
#             if(i!=j)and(i!=k)and(j!=k):
#                 if(i!=0)and(k!=0)and(k!=2):
#                    print(i,j,k)
# 有n个人围成一圈，从第一个人开始报数，从一到三，只要报到3的人就出去，问留下来的是第几号位

import tkinter
top=tkinter . Tk()

lable = tkinter.Label(top,text='Kuga',width=90,height=5,bg="red",font=("Arial",12))
lable .pack()

lable = tkinter.Label(top,text='Agito',width=90,height=5,bg="orange",font=("Arial",12))
lable .pack()

lable = tkinter.Label(top,text='Ryuki',width=90,height=5,bg="yellow",font=("Arial",12))
lable .pack()
 