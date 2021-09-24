# Exercise 13: Parameters, Unpacking, Variables


# 解包, 命令行输入参数才能得到正确结果
# argv 是 参数变量(argument variable)
# sys 是一个 模块(module)/库(library)
from sys import argv
# read the MYSS section for how to run this
# 将 argu 解包(unpack) 将参数赋值给左边的变量
# script: 脚本, 表示 .py 文件本身
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


# output
# $ cd C:\Users\CYLK_\Desktop\cylk\Projects\pythonProject\Learn_PYTHON_3_the_HARD_WAY
# $ python ex13.py first 2nd 3rd
'''
The script is called: ex13.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd
'''
