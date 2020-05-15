# any function simply return true if any of the item in the list is true

# all function simply return true if all of the item in the list is true


# list1=[1,0,0,0]
# list2=[1,1,1,1]
#
# print("list 1  ",all(list1))
#
# print("list 2  ",all(list2))


# now we have to check if all the number in the list is true

list3=[2,4,6,8]
list4=[1,2,3,4]

print(all([num1%2==0 for num1 in list3]))
print(all([num2%2==0 for num2 in list4]))



