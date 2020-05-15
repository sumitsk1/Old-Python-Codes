# You have to have a complete understanding of functions,
# first class function / closures
# then finally we will learn about decorators

# def square(a):
#     return a ** 2
#
#
# s = square
# print(s(7))
# print(s.__name__)
# print(square.__name__)
# print(s)
# print(square)

# map
# def square(a):
#     return a**2

# l = [1, 2, 3, 4]


# print(list(map(lambda a : a**2, l)))

# def my_map(func, l):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list
#
#
# def my_map2(func, l):
#     return [func(item) for item in l]
#
#
# print(my_map2(lambda a: a ** 3, l))
#

####################function returning function

# def outer_func():
#     def inner_func():
#         print('inside inner func')
#
#     return inner_func
#
#
# def outer_func2(msg):
#     def inner_func2():
#         print(f"message is {msg}")
#
#     return inner_func2
#
#
# var = outer_func2("hello there ! ")
# var()
#


#########################function returning function (closure) practice

def to_power(x):  # x = 3
    def calc_power(n):  # n = 2
        return n ** x

    return calc_power


cube = to_power(3)
print(cube(2))

square = to_power(2)
print(square(4))




power_of=lambda p,n:n**p
print(power_of(6,8))