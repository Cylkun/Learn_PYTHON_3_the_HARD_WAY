# Exercise 11: Asking Questions


# 每一行 print 后面加了 end=' ', 告诉 print 不要用换行符结束这一行跑到下一行去
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"so, you're {age} old, {height} tall and {weight} heavy.")

# 试试 x = int(input())


# output
'''
How old are you? 25
How tall are you? 168
How much do you weight? 53
So, you're 25 old, 168 tall and 53 heavy.
'''
