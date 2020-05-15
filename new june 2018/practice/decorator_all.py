# Decorators - enhance the functionality of other functions
# @ use for decorator

# def decorator_function(any_function):
#     def wrapper_function():
#         print('this is awesome function')
#         any_function()
#
#     return wrapper_function
#
#
# # this is awesome function
#
# @decorator_function  # shortcut
# def func1():
#     print('this is function 1 ')
#
#
# func1()
#
#
# @decorator_function
# def func2():
#     print('this is function 2')
#
#
# func2()
#
# # func1 = decorator_function(func1)
# # func1()

######################################################################
#
# def decorator_function(any_function):
#     def wrapper_function(*args, **kwargs):
#         print('this is awesome function')
#         return any_function(*args, **kwargs)
#
#     return wrapper_function
#
#
# @decorator_function
# def func(a):
#     print(f'this is function with argument {a}')
#
#
# func(5)
#
#
# @decorator_function
# def add(a, b):
#     return a + b
#
#
# print(add(2, 3))
#
# #################################
#
#
# from functools import wraps
#
#
# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         """ this is wrapper function """
#         print('this is awesome function')
#         return any_function(*args, **kwargs)
#
#     return wrapper_function
#
#
# @decorator_function
# def add(a, b):
#     ''' this is add function '''
#     return a + b
#
#
# print(add.__doc__)
# print(add.__name__)
#

###########################################################################################################


# from functools import wraps
#
#
# def only_int_allow(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         if all([type(arg) == int for arg in args]):
#             return function(*args, **kwargs)
#         print("Invalid arguments")
#
#         # data_types = []
#         # for arg in args:
#         #     data_types.append(type(arg)==int)
#         # if all(data_types):
#         #     return function(*args, **kwargs)
#         # else:
#         #     print("Invalid arguments")
#
#     return wrapper
#
#
# @only_int_allow
# def add_all(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total
#
#
# print(add_all(1, 2, 3, 4, 5))
#



###############################
#decorator with argument

from functools import wraps


def only_data_type_allow(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            print("Invalid arguments")

        return wrapper

    return decorator


@only_data_type_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string


print(string_join('harshit', 'vashisth', 'a', 8))