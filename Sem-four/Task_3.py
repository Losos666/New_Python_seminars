# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 
 
# 1) с помощью математических формул нахождения корней квадратного уравнения 
 
# 2) с помощью дополнительных библиотек Python

# path = 'file_task_2.txt'
# with open(path, 'r') as my_file:
#     data = my_file.read()
# data = data.split()
# #разбивает по частям список

# data = data [:-2]  #убираем последние 2 символа
# print(data)

# new_data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])]
# print(data)

# d = data[1]**2 -4 * data[0] * data[2]
# print(d)

# x_1 = (-data[1] + d**0.5) / (2 * data[0])
# x_2 = (-data[1] - d**0.5) / (2 * data[0])

# print(x_1, x_2)




path = 'file_task_2.txt' 
with open(path, 'r') as my_file: 
    data = my_file.read() 
 
data = data.split() 
print(data) 
data = data[:-2] 
print(data) 
data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])] 
print(data) 
# D=b^2-4ac 
d = data[1]**2 - 4 * data[0] * data[2] 
print(d) 
# x=((-b+(d^(1/2)))/(2*a)) 
x_1 = (-data[1] + d**0.5) / (2 * data[0]) 
x_2 = (-data[1] - d**0.5) / (2 * data[0]) 
print(x_1, x_2)







# data = open('ert.txt', 'w') 
 
# data.writelines('\nLesson 5') 
 
# a = int(input('Введите a: ')) 
# b = int(input('Введите b: ')) 
# c = int(input('Введите c: ')) 
 
# d = b**2-4*c*a 
# x1 = (-b+d**0.5)/(2*a) 
# x2 = (-b-d**0.5)/(2*a) 
 
# data.writelines(f'\n {a}*x^2+{b}*x+{c}=0 \nx1 = {x1}, \nx2 = {x2}') 
# data.close

