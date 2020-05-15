
# def listcom(l):
#     list1=[i**2 for i in range(1,l+1)]
#     # for i in range(1,l+1):
#     #     list1.append(i**2)
#     return list1
#

# print(listcom(10))


# def list_compre(l):
#
#     list1=[]
#     for i in l:
#         list1.append(i[0])
#     return list1
#
# print(list_compre(["my","first","name",'is','sumit']))
#
# first_char=[i[0] for i in ["my","first","name",'is','sumit'] ]
#
# print(first_char)




############# list_comprehension with if

# def int_checker(l):
#     return [str(i) for i in l if (type(i)==int or type(i)==float)]
#
# print(int_checker([1,3,3.5,'sumit',[1,4,5.6]]))
#


############# list_comprehension with if  else


# def listcomifelse(l):
#     new_list=[]
#     for i in l:
#         if i%2==0:
#             new_list.append(i*2)
#         else:
#             new_list.append(-i)
#
#     return new_list
#
# print(listcomifelse([1,2,3,4,5,6,7,8,9,10]))



# def listcomifelse2(l):
#     return [i*2 if i%2==0 else -i for i in l]
#
#
# print(listcomifelse2([1,2,3,4,5,6,7,8]))


############ nested_list_comp

# nested_list_comp =[[[i for i in range(2,5)] for i in range (1,5)] for i in range(4)]
#
# print(nested_list_comp)



