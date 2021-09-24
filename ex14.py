# Exercise 14: Prompting And Passing


from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
# 在 input 中对于 变量prompt 的输出不用加 "..."
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# 遇到想输出好几行话, 用 """...""" 就对了
# 好几行话输出时, 开头默认多一个 \n
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
""")


# output
# $ cd C:\Users\CYLK_\Desktop\cylk\Projects\pythonProject\Learn_PYTHON_3_the_HARD_WAY
# $ python ex14.py CYLK
'''
Hi CYLK, I'm the ex14.py script.
I'd like to ask you a few questions.
Do you like me CYLK?
> Yes
Where do you live CYLK?
> Hohhot
What kind of computer do you have?
> Surface Pro7

Alright, so you said Yes about liking me.
You live in Hohhot.  Not sure where that is.
And you have a Surface Pro7 computer.  Nice.
'''
