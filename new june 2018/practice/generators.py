# generators
# generators are iterators

# iterator , iterable

l = [1, 2, 3]  # iterable

# for i in l:
#     print(i)

# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# next(l)


# for num in map(lambda a :a**2, l):
#     print(num)

# l = [1,4,9,16]
# memory  ---- [.............................................] , list
# memory ---- (9)


######################################

# create your first generator with generator function
# 1.) generator function

# 10 , 1 to 10

# def nums(n):
#     for i in range(1, n + 1):
#         yield (i)
#
# for num in nums(10):
#     print(num)


# def even_generator(n):
#     for num in range(2, n + 1, 2):
#             yield (num)
#
#
# even_nums = even_generator(20)
# for num in even_nums:
#     print(num)
#
# for num1 in even_nums:
#     print(num1)
##################################################
#
# square = (i ** 2 for i in range(1, 11))
#
# print(next(square))
# print(next(square))
# print(next(square))


#########################


import time

# list vs generator
# memory usage , time
# when to use list , when to use generator

t1 = time.time()
l = [i**2 for i in range(10000000)] # 10 million
print(time.time() - t1)

# t1 = time.time()
# g = (i ** 2 for i in range(10000000))  # 10 million
# print(time.time() - t1)