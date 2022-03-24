# Exercise 44: Inheritance Vs. Composition


class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

    def override(self):
        print("PARENT overried()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        # super(<class>, self): 找到类 <class> 的父类
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()

# 隐式继承
dad.implicit()
son.implicit()
print("\n")

# 显式覆盖
dad.override()
son.override()
print("\n")

# 替换
dad.altered()
son.altered()

print("\n---------------------\n")

class Other(object):

    def implicit(self):
        print("OTHER implicit()")

    def override(self):
        print("OTHER override()")

    def altered(self):
        print("OTHER altered()")


class Child2(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()
