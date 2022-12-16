# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения
# not(x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

print('Enter number x,y,z')
x = int(input())
y = int(input())
z = int(input())
boolean = bool
if not(x or y or z) == (not x and not y and not z):
    boolean = True
    print(boolean)
else:
    boolean = False
    print(boolean)
