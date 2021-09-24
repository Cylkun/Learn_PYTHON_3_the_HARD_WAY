# Exercise 19: Functions And Variables


# 定义函数 cheese_and_crackers, 两个参数 cheeese_count 和 boxes_of_crackers
# 函数功能: 输出 cheese_count 和 boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
    # print(f"{a, b}")  # 输出为 (a, b)


# 运行 cheese_and_crackers 的方式一: 传入具体数值
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# 运行 cheese_and_crackers 的方式二: 传入变量
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# 运行 cheese_and_crackers 的方式三: 传入含有具体数值的算式
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# 运行 cheese_and_crackers 的方式四: 传入含有具体数值和变量的算式
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# output
'''
We can just give the function numbers directly:
You have 20 cheeses!
You have 30 boxes of crackers!
Man that's enough for a party!
Get a blanket.

OR, we can use variables from our script:
You have 10 cheeses!
You have 50 boxes of crackers!
Man that's enough for a party!
Get a blanket.

We can even do math inside too:
You have 30 cheeses!
You have 11 boxes of crackers!
Man that's enough for a party!
Get a blanket.

And we can combine the two, variables and math:
You have 110 cheeses!
You have 1050 boxes of crackers!
Man that's enough for a party!
Get a blanket.

'''
