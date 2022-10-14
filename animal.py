# create a class called Animal- file name starts with a- class name starts with A
# add the common attributes/var behaviour/functions
# syntax class name: - class Animal:
class Animal: #follow the correct naming convention & best practices
    # we need to initialise with builtin method called __init__(self)
    # self refers to current class
    def __init__(self):# any attributes attached to the class should be part of init method
        # self.var = What you want to save var as
        self.alive = True
        self.spine = True
        self.eyes = True



# let's create some methods to add common behaviours
    def breathe(self):
        return "keep breathing to stay alive "
    # lets add one more behaviour
    def eat(self):
        return "time to eat!..."

# create an object of this class
cat = Animal() # creating an object of our Animal class
# print(cat.breathe()) # calling the method using object of the Animal class
# print(cat.eat())