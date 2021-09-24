# Exercise 8: Printing, Printing


# 定义 函数(function) 让它返回 formatter变量 到其他字符串中
formatter = "{} {} {} {}"

'''
 formatter.format(...)  # 在 formatter 上调用 format
    1. 取 formatter = "{} {} {} {}"
    2. 调用 format函数
    3. 给 format 传递4个参数, 这些参数与 formatter变量 中的{}相匹配, 相当于将参数传递给 format
'''
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# True 和 False 是 关键字, "True" 和 "False" 是 字符串, 输出结果是一样
print(formatter.format(True, False, False, True))
# print(formatter.format('True', 'False', True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
# print中函数可以换行
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))


# output
'''
1 2 3 4
one two three four
True False False True
{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}
Try your Own text here Maybe a poem Or a song about fear
'''
