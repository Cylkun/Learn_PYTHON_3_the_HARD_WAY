# Exercise 6: Strings And Text


types_of_people = 10
# f"...{}..." 含有变量的句子
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}!"

# format 调用变量 hilarious 放入 joke_evaluation 中的 {} 中
# 一下两种写法相同
# cylk = 'CYLK'
# print(f"This is {cylk}")
# print("This is {}".format(cylk))
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# 输出时w和e之间没有空格
print(w + e)


# output
'''
There are 10 types of people.
Those who know binary and those who don't.
I said: There are 10 types of people.
I also said: 'Those who know binary and those who don't.'
Isn't that joke so funny? False
This is the left side of...a string with a right side.
'''
