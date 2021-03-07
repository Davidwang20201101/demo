# names =['Adeam','David','Lucy']
# print(names)
# names[2]='ass'
# print(names)
# names.insert(0,'billy')
# names.insert(2,'car')
# names.append('kris')
# names.remove('kris')
# print(names)
# 得到
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# ['Adeam', 'David', 'Lucy']
# ['Adeam', 'David', 'ass']
# ['billy', 'Adeam', 'car', 'David', 'ass']

# Process finished with exit code 0

# cars =['a','s','d','f']
# cars. sort()
# print(cars)
# 得到
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# ['a', 'd', 'f', 's']
#
# Process finished with exit code 0

# cars =['a','s','d','f']
# cars. sort(reverse=True)
# print(cars)
# 得到
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# ['s', 'f', 'd', 'a']

# Process finished with exit code 0

# cars =['a','s','d','f']
# print(cars)
# cars.reverse()
# print(cars)
# 得到————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# ['a', 's', 'd', 'f']
# ['f', 'd', 's', 'a']
#
# Process finished with exit code 0

# cars =['a','s','d','f']
# l=len(cars)
# print(len(cars))
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# 4
#
# Process finished with exit code 0
# nums =(3,4,5,6)
# print(max(nums))
# print(min(nums))
# 得到————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# 6
# 3

# Process finished with exit code 0
# cars =['a','s','d','f']
# cars.sort()#reverse=True
# print(cars)
# 得到————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# ['a', 'd', 'f', 's']
#
# Process finished with exit code 0

# names =['Adeam','David','Lucy']
# for name in names:
#     print(name)
#
# print(names)
# 得到————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# Adeam
# David
# Lucy
# ['Adeam', 'David', 'Lucy']

# names =['Adeam','David','Lucy']
# for name in names:    for loop ->for 临时变量 names是列表词
#      print(name)

# print(names)

# names = ['Adeam', 'David', 'Lucy']
# for name in names:
#       print(name .title()+",good evening ")
#       print(name)
#
# print(names)
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# Adeam,good evening
# Adeam
# David,good evening
# David
# Lucy,good evening
# Lucy
# ['Adeam', 'David', 'Lucy']
#
# Process finished with exit code 0

# names = ['Adeam', 'David', 'Lucy']
# for name in names:
#        print(name .title()+",good evening ")
#        print(name.title()+"have a nice day")
#
# print(names)
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# Adeam,good evening
# Adeamhave a nice day
# David,good evening
# Davidhave a nice day
# Lucy,good evening
# Lucyhave a nice day
# ['Adeam', 'David', 'Lucy']
#
# Process finished with exit code 0

# for value in range(1, 5):
#     print(value)
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# 1
# 2
# 3
# 4
#
# Process finished with exit code 0

# for value in range(1,11,2):
#      print(value)
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# 1
# 3
# 5
# 7
# 9
#
# Process finished with exit code 0

# for value in range(2,11,2):
#       print(value)
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# 2
# 4
# 6
# 8
# 10
#
# Process finished with exit code 0

# players =['a','b','c','d','e']
# print(players[0:3])
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# ['a', 'b', 'c']
#
# Process finished with exit code 0
# players =['a','b','c','d','e']
# print(players[2:4])
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# ['c', 'd']
#
# Process finished with exit code 0

# players =['a','b','c','d','e']
# print("there are the first these players on my team:")
# for player in players[:3]:
#     print(player.title())
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# there are the first these players on my team:
# A
# B
# C

# Process finished with exit code 0

# my_foods = ['pizza','carrot', 'cake','kfc']
# friend_foods = my_foods[:]
#
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
#
# print("my favorate foods are: ")
# print(my_foods)
#
# print("my favorate foods are: ")
# print(friend_foods)
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# my favorate foods are:
# ['pizza', 'carrot', 'cake', 'kfc', 'cannoli']
# my favorate foods are:
# ['pizza', 'carrot', 'cake', 'kfc', 'ice cream']

# Process finished with exit code 0

# tuple
# dimensions = (200,30,50)
# print(dimensions[0])
# print(dimensions[1])
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# 200
# 30

# Process finished with exit code 0

# dimensions = (200,30,50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions = (200,30,50)
# for dimension in dimensions:
#     print(dimension)
# print(dimensions)
# 得出————
# /Users/wangyueqiu/PycharmProjects/demo/venv/bin/python /Users/wangyueqiu/PycharmProjects/demo/venv/2020/10/25.py
# 200
# 30
# 200
# 30
# 50
# (200, 30, 50)

# Process finished with exit code 0