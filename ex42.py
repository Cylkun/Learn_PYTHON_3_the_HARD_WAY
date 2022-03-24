# Exercise 42: Is-A, Has-A, Objects, and Classes


# Animal is-a object (yes, sort of confusing) look at the extra credit
# 定义类 Animal, 继承(is-a)对象 object
class Animal(object):
    pass


# 定义类 Dog, 继承(is-a)父类 Animal
class Dog(Animal):

    def __init__(self, name):
        # (has-a)实例属性 name
        self.name = name


# 定义类 Cat, 继承(is-a)父类 Animal
class Cat(Animal):

    def __init__(self, name):
        # (has-a)实例属性 name
        self.name = name


# 定义类 Person 继承(is-a) object
class Person(object):

    def __init__(self, name):
        # (has-a)实例属性 name
        self.name = name

        # Person has-a pet of some kind
        # (has-a)实例属性 pet 默认为 None
        self.pet = None


# 定义类 Employee 继承(is-a) 父类 Person
class Employee(Person):

    def __init__(self, name, salary):
        # ?? hmm what is this strange magic?
        # super
        super(Employee, self).__init__(name)
        # (has-a)实例属性 salary
        self.salary = salary


# 定义类 Fish 继承(is-a) object
class Fish(object):
    pass


# 定义类 Salmon 继承(is-a)父类 Fish
class Salmon(Fish):
    pass


# 定义类 Halibut 继承(is-a)父类 Fish
class Halibut(Fish):
    pass


# (rover is-a Dog) has-a Rover
rover = Dog("Rover")

# (satan is-a Cat) has-a Satan
satan = Cat("Satan")

# (mary is-a Mary) has-a Mary
mary = Person("Mary")

# (mary has-a pet) is-a satan
mary.pet = satan

# (frank is-a Empoyee) has-a Frank, 120000
frank = Employee("Frank", 120000)

# (frank has-a pet) is-a rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()
