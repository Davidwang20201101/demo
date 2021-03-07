# class Myclass:
#     name='David'
#     def SayHi(self):
#         print('Hello %s'%self.name)
#
# mc = Myclass()
# print(mc.name)
#
# print(mc.name)
# mc.SayHi()

# class Car:
#     speed=0
#
#     def drive(self,distance):
#         time= distance / self.speed
#         print(time)
#
# car1 = Car()
# car1.speed = 60.0
# car1.drive(100.0)
# class Vehicle:
#     def __init__(self,speed):
#         self.speed = speed
#
#     def drive(self,distance):
#             print('need %f hour(s)'%(distance * self.speed))
#
# class Bike(Vehicle):
#     pass
#
# class  Car(Vehicle):
#     def __init__(self,speed,fuel):
#         Vehicle.__init__(self,speed)
#         self.fuel =fuel
#     def drive(self,distance):
#         Vehicle.drive(self,distance)
#         print('need %f fuels' %(distance * self.fuel))