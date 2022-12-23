# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random
print("enter long list")
n = int(input())
list1 = [round(random.uniform(1,10),2) for i in range(n)]
print(list1)
i = 0
for i in range(n):
    list1[i] = list1[i] % 1
i = 0
for i in range(n):
    x = max(list1)
    m = min(list1)
print(f"максимальное = {x}")
print(f"минимальное = {m}")
summ = x - m
print(f"разность = {summ}")