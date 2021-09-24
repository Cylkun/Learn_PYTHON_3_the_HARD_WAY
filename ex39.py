# Exercise 39: Dictionaries, Oh Lovely Dictionaries


# create a mapping of state to abreviation


# Conversation
'''
>>> things = ['a', 'b', 'c', 'd']
>>> print(things[1])
b
>>> things[1] = 'z'
>>> print(things[1])
z
>>> things
['a', 'b', 'c', 'd']
>>> stuff = {'name': 'Zed', 'age': 39, 'height': 6*12+2}
>>> print(stuff['name'])
Zed
>>> print(stuff['age'])
39
>>> print(sutff['height'])
74
>>> stuff['city'] = "SF"
>>> print(stuff['city'])
SF
>>> stuff[1] = "Wow"
>>> stuff[2] = "Neato"
>>> print(stuff[1])
Wow
>>> print(stuff[2])
Neato
>>> del stuff['city']  # del 删除
>>> del stuff[1]  # 报错, 字典不能用数字索引
>>> del stuff[2]  # 报错
>>> stuff
{'name': 'Zed', 'age': 39, 'height': 74}
'''


states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonvile'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
# states.items(): 将 states 中的 key 赋值给 state, value 赋值给 abbrev
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
# states.get(): 从 states 中获取 key 为 'Texas' 的项
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
# cities.get('TX', 'Does Not Exist'): 从 cities 中获取 key='TX' value='Does Not Exist'
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")


# output
'''
----------
NY State has: New York
OR State has: Portland
----------
Michigan's abbreviation is: MI
Florida's abbreviation is: FL
----------
Michigan has: Detorit
Florida has: Jacksonville
----------
Oregon is abbreviated OR
Florida is abbreviated FL
California is abbreviated CA
New York is abbreviated NY
Michigan is abbreviated MI
----------
CA has the city San Francisco
MI has the city Detroit
FL has the city Jacksonville
NY has the city New York
OR has the city Portland
----------
Oregon state is abbreviated OR
and has city Portland
Florida state is abbreviated FL
and has city Jacksonville
California state is abbreviated CA
and has city San Francisco
New York is abbreviated NY
and has city New Nork
Michigan is abbreviated MI
and has city Detroit
----------
Sorry, no Texas.
The city for the state 'TX' is: Does not Exist
'''
