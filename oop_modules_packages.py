# Lucky draw
# key word called import
# import random
#
# print(random.random())
# # each time it is run it generates a random number
#
# # calculate DOB or year of birth

# from random import *
# import math
# number = 23.66
# # any numbers - to round the figure up-
# # number .50 above round up 2
# # number 1.49 or less round down to 1
# print(math.ceil(number)) # ceil will round the figure up
# print(math.floor(number)) # floor will help you round the figure to bottom

#Don't Repeat Yourself (DRY)
# reusable- time efficent- cost efficent

#syntax def name():

# First Iteration below:
# def greeting():
#     # greet the user
#     print("Hello Dear ")
#
#     #pass
#     # keyword called pass
# # unless the function is called it does nothing
# greeting()

# def greet_user(name):
#     print("Hello Dear " + name) # adding 2 strings with user input()
#     #pass
# greet_user("Sparta")
#
# #lets create a function that takes int as an args
# def add(value1, value2): # take user input as int then add them together, display the outcome
#     print(value1 + value2)
#
# add(2, 2)

# def add(value1, value2): # take user input as int then add them together, display the outcome
#     print(" this function is to provide addition functionality ")
# #return statement
#     return value1 + value2
# # if you are using a return statement and calling the function- it need to be in a print statement
# print(add(2, 2))

# def multiply(value1, value2):
#     return value1 * value2
# print(multiply(2, 5))
#
# def divide(value1, value2):
#     return value1 / value2
# divide(8, 4)
# print(divide(8, 4))
#
# def modulo(value1, value2):
#     return value1 % value2
# modulo(10, 5)
# print(modulo(10, 5))