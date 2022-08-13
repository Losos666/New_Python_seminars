my_str = '1, 22, 54, 76, 2'.split(',')
#что сделать с элементом, с каким элементом, условие
my_list = [int(item) for item in my_str if (item > 10)]
print(my_list)
