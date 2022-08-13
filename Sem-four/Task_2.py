#  Задайте строку из набора чисел. Напишите программу, 
#  которая покажет большее и меньшее число.
#  В качестве символа-разделителя используйте пробел.

file_path = r'file.txt' 
with open(file_path,'r') as f: 
    mystr = f.read() 
print(mystr) 
mystr = mystr.split() 
 
print(mystr) 
for i in range(len(mystr)): 
    mystr[i] = int(mystr[i]) 
print(mystr) 
print(max(mystr)) 
print(min(mystr))


# list = ['1','3','8','2']
# data = open('euq.txt' , 'w')
# data.writelines(list)
# for i in 'ueq.txt':
#     maxx = list[0]
#     if maxx<list[1]:
#         maxx = list[1]
#     elif maxx<list[2]:
#             maxx = list[2]
#     elif maxx<list[3]:
#                 maxx = list[3]
# data.writelines(f'\nMax num: {maxx}')
# data.close

