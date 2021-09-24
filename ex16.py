# Exercise 16: Reading And Writing Files


from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# open() 有三种模式, r(只读read), w(写入write), a(追加append), 默认 r(只读read)
# 先用 open() 打开文件, 将文件赋值给变量, 再对变量进行文件操作
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# truncate() 清空文件
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write  these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
# close() 保存刚刚写入的内容
target.close()


# output
# $ cd C:\Users\CYLK_\Desktop\cylk\Projects\pythonProject\Learn_PYTHON_3_the_HARD_WAY
# $ python ex16.py ex16_test.txt
'''
We're going to erase ex16_test.txt.
If you don't want that, hit CTRL-C (^C).
If you do want that, hit RETURN.
?
Opening tht file...
Truncating the file.  Goodbye!
Now I'm going to ask you for three lines.
line 1:This is test file of ex16.py
line 2: Hello, CYLK!
line 3: Hello, World!
I'm going to write these to the file.
And finally, we close it.
'''


# 命令(方法/函数)
'''
close: 关闭(保存)文件
read: 读文件
readline: 读文件的一行
truncate: 截断(清空)文件
write('stuff'): 写入stuff
seek(0): 移动读写指针, 将读写位置移动到文件开头
'''
