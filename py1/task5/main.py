# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
import math

print("введите координаты 1 точки")
x1 = int(input())
y1 = int(input())
print("введите координаты 2 точки")
x2 = int(input())
y2 = int(input())
print(f"координаты: A{x1,y1}, B{x2,y2}")
res = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"растояние AB = {res}")