# Exercise 29: What If


people = 20
cats = 30
dogs = 15


if people < cats:  # people = 20 < cats = 30
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:  # people = 20 > dogs = 15
    print("The world is dry!")


dogs += 5  # dogs = 20

if people >= dogs:  # people = 20 >= dogs = 20
    print("People are greater than or equal to dogs.")

if people <= dogs:  # people = 20 <= dogs = 20
    print("People are less than or equal to dogs.")

if people == dogs:  # people = 20 == dogs = 20
    print("People are dogs.")


# output
'''
Too many cats! The world is doomed!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
'''
