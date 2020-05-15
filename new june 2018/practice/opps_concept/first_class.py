

# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD , constructor
# WHAT ARE ATTRIBUTES, INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT

# class Person:
#     def __init__(self, first_name, last_name, age):
#         # instace variables
#         print('init method  called')
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#
# p1 = Person('Harshit', 'Vashistha', 24)
# p2 = Person('Mohit', 'Vashistha', 19)
#
# print(p1.person_first_name)
# print(p2.person_first_name)



# class Person:
#     def __init__(self,first_name,last_name,age):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#
#     def full_name(self):
#         print(f"{self.first_name} {self.last_name}")
#
#
# p1=Person('sumit','kumar',18)
# p2=Person('mohit','sen',19)
#
# print(p1.first_name)
#
# p1.full_name()




class Laptop:
    dis_offer=50
    def __init__(self, brand, model_name, price):
        # instance variables
        self.brand = brand
        self.name = model_name
        self.price = price
        self.laptop_name = brand + ' ' + model_name

    def discount(self):
        offer = (self.dis_offer/100)*self.price
        return self.price - offer


laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('acer', 'au114tx', 50000)
# laptop2.dis_offer=100
print(laptop2.__dict__)
# print(laptop1.laptop_name)
print(laptop2.discount())










