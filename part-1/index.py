# coding=utf-8
# 基础语法


# 1.缩进
# python需严格统一缩进规则
test1 = '1111'
if test1 == '1111':
  print 'is 1111'
elif test1 == '2222':
  print 'is 2222'
else:
  print 'is null'


# 2.换行
# 多行语句使用斜杠(\)，若语句包含[],{},()则无需斜杠
total = 3 + \
        4 + \
        5
tomal = [3, 4, 5,
        6, 7]