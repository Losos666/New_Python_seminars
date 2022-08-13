# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

from ast import Str


number = int(input('введите число --> '))
print(f"{number:b}")
retreat = ''
while number > 2:
    retreat = Str(number % 2) + retreat
    number = number // 2
retreat = retreat(number) + retreat
print(number)

# программа работает - но выдает ошибку (после вывода) 
#  retreat = Str(number % 2) + retreat
# TypeError: unsupported operand type(s) for +: 'Constant' and 'str'
