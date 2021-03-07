# cars = ['audi','BMW','subaru','toyota']
#
# for car in cars:
#    if car =='BMW':
#        print(car.upper())
#    else:
#        print(car.title())
#
# Audi
# BMW
# Subaru
# Toyota

# bool 布尔值
# true   /  false

# == 疑问句？   发问 ：是xxxx吗？
# =陈述句。     定义变量：a里面是1
# !=否决疑问      发问： 不是xxx吗？
# bmw不等于Bmw

# age = 22
#
# if age > 12:
#     print('pass')
# else:
#     print('you cannot pass')

# pass

# 符合多个条件

# age_1 = 6
# age_2 = 30
# if age_1 >18 or age_2 > 18:
#     print('pass')
#
#     pass
#
#     只要有一个条件满足，则结果为true，如果都为Flase ，结果才是Flase
# age_1 = 6
# age_2 = 30
# if age_1 > 18 or age_2 > 18:
#     print('pass')
# else:
#     print('You cannot pass')

# requested_toppings=['mushrooms','onion','pineapple']
# b = 'mushrooms' in requested_toppings
# b2 = 'cheese'  in requested_toppings
# print(b)
# print(b2)
#
# True
# False

# 可以检查字符串是否在表格中
# if结构
#
# ...
# if conditional_test:
#     do code1
# else:
#     do code2
# ...

# 4岁以下免费
# 4-18岁半价
# 18岁全票

# age = 12
#
# if age < 4:
#     print('free')
# elif age < 18:  elif = eles + if
#     print('half')
# else:
#     print('full') else 只会出现在末尾
#  从小到大写
#     half

# age =int(input())
# print(age+1)

# age = 33
#
# if age < 2:
#     print('he is a infant')
# elif age < 4:
#     print('he is still baby')
# elif age < 13:
#     print('he is a cild')
# elif age < 20:
#     print('he is a teenager')
# elif age < 65:
#     print('he is a adult')
# else:
#     print('he is a old man' )
#
#     he is a adult

# requested_toppings = ['mushrooms','green peppers','extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('sorry, we are get out of green peppers.')
#     else:
#         print("adding" + requested_topping + '.')
#
# addingmushrooms.
# sorry, we are get out of green peppers.
# addingextra cheese.

# requested_toppings =[]
# if requested_toppings:
#     print('making your pizza!!!')
# else:
#     print('empty pizza!!!')
# empty pizza!!!

# available_toppings = ['mushrooms','green peppers','extra cheese','pineapple','onion']
#
# requested_toppings =['mushrooms','french fries','cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("adding"+requested_topping)
#     else:
#         print("sorry we don't have"+requested_topping + '.')
#
#         addingmushrooms
#         sorry
#         we
#         don
#         't havefrench fries.
#         sorry
#         we
#         don
#         't havecheese.

