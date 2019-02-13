# coding=utf-8
# 高阶语法
# 配合后续学习


# 1.索引
# python的索引还具有截取的功能, [头下标:尾下标] 
print 'ABCDEFG'[1]   # B
print 'ABCDEFG'[1:4] # BCD
print 'ABCDEFG'[2:]  # CDEFG
print 'ABCDEFG'[:4]  # ABCD


# 2.修改全局变量
# 在函数或其它作用域内如果想修改全局变量，则需要使用 global 关键字定义
globalVar = 0
def changeGlobal():
  global globalVar
  globalVar = 4
print globalVar
changeGlobal()
print globalVar
