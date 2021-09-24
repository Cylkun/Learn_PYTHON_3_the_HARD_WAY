# Exercise 31: Making Decisions


# 输出段落 print("""...""") 段落前若有输出时多数出一个空行, 后面没有多一个空行
print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

# 进入第一扇门
if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    # 1. Take the cake.
    if bear == "1":
        print("The bear eats your face off.  Good job!")
    # 2. Scream at the bear.
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    # 没有选择以上两个选项
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

# 进入第二扇门
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    # 1. Blueberries. or 2. Yellow jacket clothespins.
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    # 没有选择前两个选项
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

# 既没有进入第一扇门也没有进入第二扇门
else:
    print("You stumble around and fall on a knife and die.  Good job!")


# strategy
'''
You enter a dark room with two doors.
Do you go through door #1 or door #2?
> 1
    There's a giant bear here eating a cheese cake.
    What do you do?
    1. Take the cake.
    2. Scream at the bear.
    > 1
        The bear eats your face off.  Good job!
    > 2
        The bear eats your legs off.  Good job!
    > not 1 and not 2
        Well, doing ____ is probably better.
        Bear runs away.
> 2
    You stare into the endless abyss at Cthulhu's retina.
    1. Bluebetties.
    2. Yellow jacket clothespins.
    3. Undrstanding revolvrs yelling melodies.
    > 1 or 2
        Your body survives powered by a mind of jello.
        Good job!
    > not 1 and not 2
        The insanity rots your eyes into a pool of muck.
        Good job!
> not door #1 and not door #2
    You stumble around and fall on a knife and die.  Good job!
'''
