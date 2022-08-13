# Напишите программу , которая на вход принимает 5 чисел и находит максимально из них.
# пример
# - 1, 4, 8, 7, 5 - > 8
# - 78, 55, 36, 90, 2 -> 90

maxx = 0
for i in range(5): # счетчик колличества запросов числа
    x = int(input('-->'))
    if i == 0:
        maxx = x
    elif x > maxx:
        maxx = x
print(maxx)

##my_list = [5,2,3,4,5,6]
##i = 0
##maxx = my_list[0]
##while i < len(my_list): (len пробежать по списку for i in range(len(my_list)):
##     if my_list[i] > maxx:
##      maxx = my_list[i]
##  i+=1
## print(maxx)
