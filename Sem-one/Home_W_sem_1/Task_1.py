# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input(' day or 1 to 7 --> '))
if number < 6 :
    print('weekdays')
elif number >6 and number < 8:
    print('output')
elif number > 7:
    print('--Error--')