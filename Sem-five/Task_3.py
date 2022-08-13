f = lambda x: True if x > 10 else False
my_list_1 = ['A', 'B', 'C', 'D']
my_list_2 = [15, 76, 1, 98]
my_list_3 = [65, 68]


res = list(zip(my_list_1, my_list_2, my_list_3))
print(res)
