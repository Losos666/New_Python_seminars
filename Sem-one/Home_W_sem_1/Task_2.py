# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = 0
y = 2
left = not(x or y)
right = not(x and not y)
statement = left == right
print(statement)