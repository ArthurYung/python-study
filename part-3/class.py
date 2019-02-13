# -*- coding: UTF-8 -*-
# 类


# 1.创建类:
# 注意：self为类的实例而非类本身
class firstClass:
  count = 4
  def prt(self, str):
    firstClass.count += 1
    self.name = str


# 2.__init__()
# 当类实例化时会自动调用
class secendClass:
  count = 4
  def __init__(self, name):
    self.name = name


# 3.类的继承
class child(secendClass): # 继承secendClass
  def myMethod(self):
    self.count = 5
    print '调用子类方法'


# 4.实例化
# 在 Python 中并没有new关键字，类的实例化类似函数调用方式
class1 = secendClass('ouyang')
class2 = secendClass('Arthur')
print class1.name


