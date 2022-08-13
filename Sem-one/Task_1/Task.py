number1 = int(input('введите первое число = '))
number2 = int(input('введите второе число = '))

if ((number2 == number1 * number1) or (number1 == number2 * number2)):
    print (f'yes')
else:
    print (f' no')

## тернарный оператор 
## print('yas' if ((a == b*b) or (b == a*a)) else 'no')