# Exercise 38: Doing Things To Lists


ten_things = "Apples Oranges Crows Telephone Light Suger"

print("Wait there are not 10 things in that list. Let's fix that.")

# split: 将 ten_things 拆分成单词, 按顺序放入列表 stuff 中
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()  # pop() == pop(-1)
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
# more_stuff.pop() 的执行
'''
more_stuff.pop()  ==  pop(more_stuff)
more_stuff.pop(): 在 more_stuff 上调用 pop 函数
pop(more_stuff): 用 more_stuff 作为参数调用 pop 函数
'''
print(stuff.pop())
# ' '.join(stuff): stuff 中的项组合, 中间用空格连接. 与 split 互逆
print(' '.join(stuff))  # what? cool
# 输出索引序号 >=3 && <5 的元素, 中间用 # 连接
print('#'.join(stuff[3:5]))  # super stellar


# output
'''
Wait there are not 10 things in that list. Let's fix that.
Adding: Boy
There are 7 items now.
Wait there are not 10 things in that list. Let's fix that.
Adding: Girl
There are 8 items now.
Wait there are not 10 things in that list. Let's fix that.
Adding: Banana
There are 9 items now.
Wati there are not 10 things in that list. Let's fix that.
Adding: Corn
There are 10 items now.
# 输出列表时, 每一字符串项都要加引号
There we go: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
Let's do some things with stuff.
Oranges
Corn
Corn
Telephone#Light
'''
