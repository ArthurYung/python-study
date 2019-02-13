# coding=utf-8
# 模块


# 1.引入模块方式
import function
import a, b
from function import firstFunc, secondFunc
from function import *


# 2.__init__.py
# 封装成包，支持层级引入模块

package
├── __init__.py
├── submodule.py
subpackage
├── letmodule.py
└── __init__.py

# letmodule.py
import package.submodule
