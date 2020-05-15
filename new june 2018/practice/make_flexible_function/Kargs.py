# # kwargs (keyword arguments)
# # **kwargs (double star operator)
#
# # kwargs as a parameter
# def func(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k} : {v}")
#
#
# # dictionary unpacking
# d = {'name': 'Harshit', 'age': 24}
# func(**d)



####all parameter

# # functions with all parameters
# # very important to understand
#
# # PADK
#
# # parameters
# # *args
# # default parameters
# # **kwargs
#
# def func(name, *args, last_name='unknown', **kwargs):
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)
#
#
# func('harshit', 1, 2, 3,'sk', a=1, b=2)

############ exercise


def reverse_cap(l,**kargs):
    if kargs.get("reverse_st")==True:
        return [name[::-1].title() for name in l]
    else:
        return [name.title() for name in l]
name=["sumit","amit" ]
print(reverse_cap(name,reverse_st=True))
