# 1. Удалить из исходной строки все слова с "абв"
# 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'

str_list = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# str = str.split()
# print(str)

# str_list = str_list.split()
def strs(str):
    for item in str_list:
        if 'абв' in item:
            str_list.remove(item)
            print(str_list)
# strs(str_list)

res = list(filter(lambda item: 'абв' not in item, str_list.split()))
print(res)

# s = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# a = s.split()
# for item  in a:
#     if 'абв' in item:
#         a.remove(item)
# print(a)

# 1. Удалить из исходной строки все слова с "абв"
# my_str = 'Привет, Мир! Мы очабв любим Пайтонабв! Семинары'
# res = [word for word in my_str.split() if 'абв' not in word]
# print(' '.join(res))

