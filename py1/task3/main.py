#Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
print('введите x и y')
x = int(input())
y = int(input())
if x > 0 and y > 0 or x > 0 and y == 0:
    print("Первая четверть")
elif x < 0 and y > 0 or x == 0 and y > 0:
    print("Вторая четверть")
elif x < 0 and y < 0 or x < 0 and y == 0:
    print("Третья четверть")
elif x > 0 and y < 0 or x == 0 and y < 0:
    print("Четвертая четверть")
else:
    print("х и y = 0")
