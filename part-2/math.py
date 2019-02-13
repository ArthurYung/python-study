# coding=utf-8
# 运算符


# 1.算数运算符
# + - * /(加减乘除)
# %(返回除法余数)
# **(幂运算)
# //(向下取整)

#  1.1 字符串的运算
#  字符串相加与js相似，字符串相乘则重复n次
print 'abc' + 'def' # 'abcdef'
print 'abc' * 3     # 'abcabcabc'

#  1.2 列表的运算与字符串运算相同
print [1, 2, 3] + [4, 5, 6] # [1, 2, 3, 4, 5, 6]
print [1, 2, 3] * 2         # [1, 2, 3, 1, 2, 3]


# 2.比较运算符
# 区别： <> 与!=一样也是表示比较不相等时返回True
print 3 <> 4 # True


# 3.逻辑运算符
#  3.1 and
#  同js中的 &&
a = 10
b = 20
reslute = a and b  # 20

#  3.2 or
#  同 js 中的 ||
reslute = a or b  # 10

#  3.3 not (x)
#  布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
reslute = not(a) # False


# 4.成员运算符
#  4.1 in
#  如果在指定的序列中找到值返回 True，否则返回 False。
list2 = [1, 2, 3, 4, 5 ]
string2 = '12345'
3 in list2     # True
'3' in string2 # True

#  4.2 not in
#  与 in 相反