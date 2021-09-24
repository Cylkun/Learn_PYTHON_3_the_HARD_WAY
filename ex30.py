# Exercise 30: Else And If


people = 30
cars = 40
trucks = 15


if cars > people:  # cars = 40 > people = 30
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:  # trucks = 15 < cars = 40
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people < trucks:
    print("Alright, let's just take the trucks.")
else:  # people = 30, trucks = 15
    print("Fine, let's stay home then.")


# output
'''
We should take the cars.
Maybe we could take the trucks.
Fine, let's stay home then.
'''
