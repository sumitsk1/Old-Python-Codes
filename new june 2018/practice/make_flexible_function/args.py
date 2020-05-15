# *operator
# *args
# make flexible function

# def total(a,b):
#     return a+b
#
# print(total(4,6))


def all_total(*args):
    total=0
    for i in args:
        total=total+i
    print(total)


all_total(1,2,3,4,4,5,6,7,9,9,9)

########## args with normal argument
#
# def all_total(num1,*args):
#     total=0
#     print(num1)
#     for i in args:
#         total=total+i
#     print(total)
#
#
# all_total(1,2,3)




#######exercise


