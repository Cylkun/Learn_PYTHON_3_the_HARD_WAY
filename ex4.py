# Exercise 4: Variables And Names


cars = 100  # 有100辆汽车
space_in_a_car = 4.0  # 一辆汽车可以搭载4名乘客
drivers = 30  # 有30名司机
passengers = 90  # 有90位乘客
cars_not_driven = cars - drivers  # 空闲的汽车数 = 汽车数 - 司机数
cars_driven = drivers  # 载人的汽车数 = 司机数
carpool_capacity = cars_driven * space_in_a_car  # 运输能力 = 载人的汽车数 * 每辆车载人数
# 每辆车的平均载人数 = 乘客数 / 载人的汽车数
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available. ")
print("There are only", drivers, "drivers available. ")
print("There will be", cars_not_driven, "empty cars today. ")
print("We can transport", carpool_capacity, "people today. ")
print("We have", passengers, "to carpool today. ")
# average_passengers_per_car = 3.0 而不是 3
print("We need to put about", average_passengers_per_car, "in each car. ")


# output
'''
There are 100 cars available.
There are only 30 dribers available.
There will be 70 empty cars today.
We can transport 120.0 people today.
We have 90 to carpool today.
We need to put about 3 in each car.  # 3.0 而不是 3, 是因为有除法吗
'''
