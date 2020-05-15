# zip function
# user_id = ['user1', 'user2', 'user3']
# names = ['harshit', 'mohit', 'rohit']
# last_names = ['vashistha', 'vashistha', 'sharma']

# ('user1', 'harshit'), ('user2', 'mohit')
# print(dict(zip(user_id, names, last_names)))

# example = [('a',1), ('b', 2)]
# print(dict(example))


# THIS IS CHALLENGE

# define a function take any no of lists containing number
# [1,2,3] , [4,5,6], [7,8,9]
# return average
# (1+4+7)/3 , (2,5,8)/3 , (3,6,9)/3


# try to make this anonymous function in one line using lambda 😃😃
# def average_finder(*args):
#     average = []
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average


average_finder = lambda *args: [sum(pair) / len(pair) for pair in zip(*args)]

print(average_finder([1, 2, 3], [4, 5, 6], [7, 8, 9]))

print(tuple(zip([1,2,3,4],[1, 2, 3], [4, 5, 6], [7, 8, 9])))