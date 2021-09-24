# Exercise 5: More Variables And Printing


my_name = 'Zed A. Shaw'  # 变量赋值
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = "White"
my_hair = "Brown"

print(f"Let's talk about {my_name}.")  # 输出 格式化字符串 f:格式化
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")


# output
'''
Let's talk about Zed A. Shaw.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 35, 74, and 180 I get 289.
'''
