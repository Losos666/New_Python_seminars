# напишите программу которая будет на вход принималь число N
# и выводить числа от -N до N
# пример - 
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


number_n = int(input('введите число N -> '))
for i in range(-number_n, number_n + 1): # range генерирует числа 
    print(i, end= ' ' )