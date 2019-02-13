# coding=utf-8
# 条件与循环


# 1.if条件语句
# 与js使用相同
if True: print 'True'


# 2.While语句
# while循环也可以使用else

count = 0
while count < 5:
  print count
  count += 1
else:
  print 'is over'


# 3.for-in 循环
# 与js使用相似
# else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。
list1 = [1, 2, 3, 4]
for i in list1:
  print i
else:
  print 'is over'


# 4.循环控制语句
#  4.1 break
#  break语句用来终止循环语句
for i in list1:
  if i == 2: break
  print i
else:
  print 'is over'

#  4.2 continue
#  跳过当前循环，继续下一循环
for i in list1:
  if i == 2: continue
  print i
else:
  print 'is over'

#  4.3 pass
#  占位符，不对循环体进行任何控制，当你没有想好函数的内容是可以用 pass 填充，使程序可以正常运行。

