# Exercise 35: Branches and Functions


# form sys import exit  # 不需要导入


# 黄金屋
# 输入数字(字符串会转换为数字), 若 <50 则赢, 否则死
def gold_room():
    print("This room is full of gold.  How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


# 熊屋
# 第一次选择时熊未动, 不能偷蜂蜜否则死, 第一次要 taunt bear, 第二次要 open door
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then alaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


# 克苏鲁魔象屋
# 若输入包含 flee 的语句则会回到起点, 若输入包含 head 的语句则死, 输入其他则再选一次
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


# 死亡
def dead(why):
    print(why, "Good job!")
    # exit(0): 程序正常退出; exit(1): 有错退出; exit(2): 另一种错退出
    exit(0)


# 游戏起点
# left 是 bear_room, right is cthulhu_room, others 是 dead
def start():
    print("You are in a dark room.")
    print("There is a door to your left and right.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()


# strategy
'''
You are in a dark room.
There is a door to your left and right.
Which one do you take?
> left
    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    > take honey
        The bear looks at you then slaps your face off. Good job!
    > taunt bear
        The bear has moved from the door.
        You can go through it now.
        > take honey
            The bear looks at you then slaps your face off. Good job!
        > taunt bear
            The bear gets pissed off and chews your leg off.
        > open door
            This room is full of gold.  How much do you take?
            > how_much (假设how_much是一个数字)
                if <50
                    Nice, you're not greedy, you win!
                if >=50
                    You greedy bastard!
            > others
                Man, learn to type a number.
    > others
        I got no idea what that means.
> right
    Here you see the great evil Cthulhu.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat your head?
    > flee
        回到起点
    > head
        Well that was tasty! Good job!
    > others
        待在 Cthulhu_room 接着选
> others
    You stumble around the room until you starve.
'''
