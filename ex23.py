# Exercise 23: Strings, Bytes, and Character Encodings


# conversation
'''
>>> 0b1011010
90
>>> ord('z')
90
>>> chr(90)
'Z'
'''


import sys
script, encoding, error = sys.argv
# 下面的表达可以替换上面的语句
'''
from sys import argv
script, encoding, error = argv
'''


# 函数 main()
# 参数 language: 文件; encoding: 编码方式 utf-8; error: 命令行输入 strict
def main(language_file, encoding, errors):
    # 读取文件的一行, 文件结尾是空行(空字符串)
    line = language_file.readline()
    if line:
        # 打印该行
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


# 对 ex23_languages.txt 中每一行进行编码
def print_line(line, encoding, errors):
    next_lang = line.strip()  # 去掉每一行结尾的 \n
    # .encode() 编码字符串, 将需要的编码方式和错误处理方式传入 encode() 函数
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # .decode() 解码字符串
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


# languages = open("ex23_languages.txt")不行, 为什么? ex15 中可以不加
# encoding 在命令行中已经赋值过一次, 为什么还要赋值?
languages = open("ex23_languages.txt", encoding="utf-8")

# 函数 main()
# 命令行赋值 encoding, error
main(languages, encoding, error)


# output
# $ python ex23.py utf-8 strict
