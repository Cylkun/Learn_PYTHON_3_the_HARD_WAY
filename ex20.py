# Exercise 20: Functions And Files


from sys import argv

script, input_file = argv


# 输出文件全部内容
def print_all(f):
    # f 已经打开, 可以直接 .read()
    print(f.read())


# 移动读写指针到文件 f 起始位置
def rewind(f):
    f.seek(0)


# 打印 文件 f 第 line_count 行的内容
def print_a_line(line_count, f):
    print(line_count, f.readline())


# 调用 open(), 其后的文件操作都可以直接操作
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


# output
'''
First let's print the whole file:

line 1
line 2
line 3

Now let's rewind, kind of like a tape.
Let's print three lines:
1 line 1
# 注意, 这里有一行是空行, 完整一行的末位是换行符
2 line 2

3 line 3

'''
