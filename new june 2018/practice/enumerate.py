# We use enumerate function with for loop to track position of our
# item in iterable


# How we can do this without enumerate function
names = ['abc', 'abcdef', 'harshit']


# 0 -- 'abc'
# 1 -- 'abcdef'
# pos = 0
# for name in names:
#     print(f"{pos} ----> {name}")
#     pos += 1


# with enumerate function

# for pos, name in enumerate(names):
#     print(f"{pos} ----> {name}")


# Define a function that take two arguments
# 1.) list containing string
# 2.) string that want to find in your list
# and this function will return the index of string in your list and
# if string is not present then return -1

# def find_pos(l, target):
#     for pos, name in enumerate(l):
#         if name == target:
#             return pos
#     return -1
#
#
# print(find_pos(names, 'abcz'))

# for name in names:
#     print(f"{names.index(name)}-------{name}")




# find=lambda name,string:names.index(name) if name==string else -1
#
# for name in names:
#     print(find(name,'abcdef'))

# def position(l,string):
#     for pos,name in enumerate(l):
#         if name==string:
#             return pos
#     return -1
#
# print(position(names,"abcc"))



# def position(l,string):
#     for name in l:
#         if name==string:
#             return names.index(name)
#     return -1
#
# print(position(names,"abcdef"))
#
# # map function
#
# numbers = [1, 2, 3, 4]
#
#
# def square(a):
#     return a ** 2
#
#
# squares = list(map(lambda a: a ** 2, numbers))
# print(squares)
#
# # list comp
# squares_new = [i ** 2 for i in numbers]
# print(squares_new)
#
# new_list = []
# for num in numbers:
#     new_list.append(square(num))
#
# print(new_list)
#
# names = ['abc', 'abcd', 'abcde']
# length = list(map(len, names))
#
# print(length)

#filter function

num=[7,6,5,4]
sq=list(filter(lambda a:a%2!=0,num))
print(sq)
