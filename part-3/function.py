# coding=utf-8
# 函数


# 1.函数参数
# 与es6相似，默认参数值可直接定义
def firstFunc(parm = 1):
  print parm
  return


# 2.不定长参数
# 加了星号（*）的变量名会存放所有未命名的变量参数
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return
printinfo( 70, 60, 50 )
# 输出:
# 70
# 60
# 50


# 2.具名函数
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()
def secondFunc(parm):
  print parm
  return

secondFunc('this is my first function')


# 3.匿名函数
# python的匿名函数类似于一个表达式, 使用 lambda 来创建.
sum = lambda arg1, arg2: arg1 + arg2
print "相加后的值为 : ", sum( 10, 20 )  # 30