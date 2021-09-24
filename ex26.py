# Exercise 26: Congratulations, Take A Test!


from sys import argv  # 没导入模块
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()  # 缺少命令行输入
print("How much do you weigh?", end=' ')  # 少一个 )
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv  # 没导入模块

txt = open(filename)  # 变量名错误

print("Here's your file {filename}:")
print(txt.read())  # txt 变量名写错

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())  # _read() 改为 .read()


print("Let's practice everything.")
# 分行输出时用 """...""", 而不是 '..."
print("""You\'d need to know \'about escapes
      with \\ that do \n newlines and \t tabs.""")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")  # 少一个 "
print(poem)
print("--------------")  # 少一个 "


five = 10 - (2 + 3)  # 多一个 -, 少 ( )
print(f"This should be five: {five}")  # 缺少 )


def secret_formula(started):  # 缺少 :
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)  # 函数返回值有三个, 缺 crates

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)  # startpoint 改为 start_point
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))


people = 20
cates = 30
dogs = 15


if people < cates:  # cats 改为 cates
    print("Too many cats! The world is doomed!")  # 缺少 ()

if people > cates:  # cats 改为 cates, < 改为 >
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:  # 缺少 :
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:  # 缺少 :
    print("People are less than or equal to dogs.")  # 缺少 #


if people == dogs:  # 等于用 ==, 不是 =
    print("People are dogs.")
