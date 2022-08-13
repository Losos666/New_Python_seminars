# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,10
# - A (7,-5); B (1,-1) -> 7,21

import math 
coordinates_a = [7, -5] 
coordinates_b = [1, -1] 
distance = math.sqrt( ((coordinates_a[0] - coordinates_b[0]) ** 2)+((coordinates_a[1] - coordinates_b[1]) **2) ) 
print('{:.2f}'.format(distance))