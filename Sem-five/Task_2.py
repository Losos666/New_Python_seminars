f = lambda x: True if x > 10 else False
my_list = [12, 54, 3, 65]


res = list(filter(f, my_list))

print(res)
