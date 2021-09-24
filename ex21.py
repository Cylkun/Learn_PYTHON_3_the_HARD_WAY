# Exercise 21: Functions Can Return Something


# 两数相加, 返回两数的和
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


# 两数相减, 返回两数的差
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


# 两数相乘, 返回两数的积
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


# 两数相除, 返回两数的商
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)  # age = 30 + 5
height = subtract(78, 4)  # height = 78 - 4
weight = multiply(90, 2)  # weight = 90 * 2
iq = divide(100, 2)  # iq = 100 / 2  # iq 为一位小数

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# what = age + (height - (weight * (iq / 2)))
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")


# output
'''
Let's do some math with just functions!
ADDING 30 + 5
SUBTRACTING 78 - 4
MULTIPLYING 90 * 2
DIVIDING 100 / 2
Age: 35, Height: 74, Weight: 180, IQ: 50.0
Here is a puzzle.
DIVIDING 50.0 / 2
MULTIPLYING 180 * 25.0
SUBTRACTING 74 - 4500.0
ADDING 35 + -4426.0
That becmoes: -4391.0 Can you do it by hand?
'''
