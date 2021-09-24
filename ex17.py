# Exercise 17: More Files


from sys import argv
# 导入 exists 函数, 判断文件名字符串是否存在, 存在为 True, 不存在为 False
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# 先 open() 再 read() 再 len() 为什么?
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()  # 写什么都可以, 不影响 ex17_new_file.txt 的内容, 因为 out_file.write(indata) 中 indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)  # ex17_new_file.txt 的内容只与 ex17_test.txt 有关

print("Alright, all done.")

out_file.close()
in_file.close()


# output
# $ cd C:\Users\CYLK_\Desktop\cylk\Projects\pythonProject\Learn_PYTHON_3_the_HARD_WAY
# $ # first make a sample filename
# $ echo "This is a test file." > ex17_test.txt  # 用 echo 创建文件会报错, 改用 New-Item
# $ New-Item test.txt -type file -value "This is a test file."
# $ # then look at it
# $ cat ex17_test.txt
# $ # now run our script on it
# $ python ex17.py ex17_test.txt ex17_new_file
'''
Copying from ex17_test.txt to ex17_new_file.txt
The input file is 81 bytes long
Does the output file exist? False
Ready, hit RETURN to continue, CTRL-C to abort.
Again  # 写什么都可以, 不影响 ex17_new_file.txt 的内容
Alright, all done.
'''
