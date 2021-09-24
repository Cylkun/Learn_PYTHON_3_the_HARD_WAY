# Exercise 15: Reading Files


from sys import argv

script, filename = argv

# 打开文件 filename
# 将文件 filename 赋值给变量 txt
txt = open(filename)

print(f"Here's your file {filename}:")
# 读文件 txt
# 打印文件 txt 的内容
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

# 要先 open 之后再进行 read
txt_again = open(file_again)

print(txt_again.read())


# output
# $ cd C:\Users\CYLK_\Desktop\cylk\Projects\pythonProject\Learn_PYTHON_3_the_HARD_WAY
# $ python ex15.py ex15_sample.txt
'''
Here's your file ex15_sample.txt:
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.
# 文件最后一行是空行
Typt the filename again:
> ex15_sample.txt
This is stuff I typed into a file.
It is really cool stuff.
Lots and lots of fun to have in here.

'''
