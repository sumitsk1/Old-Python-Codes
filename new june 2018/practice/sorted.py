# fruits = ['grapes', 'mango', 'apple']
#
# fruits.sort()
# print(fruits)
#
# fruits2 = ('grapes', 'mango', 'apple')
# print(sorted(fruits2))
# #
# # fruits2.sort()
# # print(fruits2)
#
# fruits3 = {'grapes', 'mango', 'apple'}
# print(sorted(fruits3))
# print(fruits3)


guitars = [
    {'model': 'yamaha f310', 'price': 8400},
    {'model': 'faith naptune', 'price': 50000},
    {'model': 'faith apollo venus', 'price': 35000},
    {'model': 'taylor 814ce', 'price': 450000}
]

sorted_guitars = sorted(guitars, key=lambda d: d['price'], reverse=True)
print(sorted_guitars)

