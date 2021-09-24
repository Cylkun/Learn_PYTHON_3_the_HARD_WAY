# Exercise 40: Modules, Classes, And Objects


# 获取某样东西里包含的东西, 有3种方法
'''
# dict style
mystuff['apples']
print(mystuff['apples'])

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
'''


# 面向对象
'''
类 class
对象 object
实例 instance
定义函数 def
被访问的对象/实例的一个变量 self
继承 inheritance
组合 composition
属性 attribute
是什么 is-a
有什么 has-a
'''


# 类
'''
class X(Y):  # 创建一个属于 X 的类, 它是 Y 的一种
class X(object):  # (object) 可以省略不写
    def __init__(self, J)  # 类 X 有一个 __init__, 它接收 self 和 J 作为参数
class X(object):  # (object) 可以省略不写
    def M(self, J)  # 类 X 有一个函数 M, 它接收 self 和 J 作为参数
foo = X()  # 将 foo 设为类 X 的一个实例
foo.M(J)  # 从 foo 中找到函数 M, 并使用 self 和 J 调用它
foo.K = Q  # 从 foo 中获取属性 K, 并将其设为 Q
'''


# class Song(object): == class Song: 两种写法等价
class Song:

    # 类 Song 有一个 __init__, 它接收 self 和 lyrics 作为参数
    # 必须是两个下划线 __ 而不是一个下划线 _
    def __init__(self, lyrics):
        # 若不加 self, Python 不能区分定义的是一个局部变量还是一个属性
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


# happy_bday 是类 Song 的一个实例
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "so I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

# 从实例 happy_bday 中调用函数 sing_me_a_song
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


# output
'''

'''
