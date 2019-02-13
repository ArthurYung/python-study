# coding=utf-8
# 变量类型


# 1.定义变量: 
# 无需声明，随心所欲
test1 = '1111'
test2 = '2222'
test3 = test4 = test5 = '3333'
test6, test7 = '4444', '5555'


# 2.删除变量:
# 使用 del 关键字删除变量，解除对变量的引用
del test1
del test3, test4, test5


# 3.数据类型
# Numbers（数字）
# String（字符串）
# List（列表）
# Tuple（元组）
# Dictionary（字典)

#  3.1 Numbers（数字）
#  python中的数字有int, long, float, complex四种
int1 = 10               # 长度不超过sys.maxint
long1 = 32L             # 末尾添加L定义长整形
float1 = 0.32659
complex1 = -8.36-1.47j  #复数由real+imagj格式定义，complex1.real 和 complex1.imag可获取实部与虚部值

#  3.2 String (字符串)
#  与其它语言类似
str1 = 'Hello World!'

#  3.3 List (列表)
#  与js中的数组相似
list1 = [1, 2, 3, 4]

#  3.4 Tuple (元祖)
#  不能被修改的列表
tuple1 = ('1', 2, '3')

#  3.4 Dictionary（字典)
#  与json相似，但不能使用 Dictionary.keyName = value 定义
dictionary1 = {'a': '1', 'b': 2, 'c': '3'}