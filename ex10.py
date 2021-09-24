# Exercise 10: What Was That?


# \t 相当于 缩进 8B
# \n 表示换行
tabby_cat = "\tI'm tabbbed in."
persian_cat = "I'm split\non a line."
# \后的一个字符会原样输出
backslash_cat = "I'm \\ a \\ cat."

# """...""" 内可放任意多行文本
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


# output
'''
    I'm tabbled in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
    * Cat food
    * Fishies
    * Catnip
    * Grass
'''


# 转义字符
# \\
# \'
# \"
# \a: ASCII响铃符(BEL)
# \b: ASCII退格符(BS)
# \f: ASCII禁止符(FF)
# \n: ASCII换行符(LF)
# \N{name}: Unicode
# \r: ASCII回车(CR)
# \uxxxx: 值为16位十六进制值 xxxx 的字符
# \Uxxxxxxxx: 值为32位十六进制 xxxxxxxx 的字符
# \v: ASCII垂直制表符(VT)
# \ooo: 值为八进制值 ooo 的字符
# \xhh: 值为十六进制值 hh 的字符
