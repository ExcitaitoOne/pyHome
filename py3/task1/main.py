#Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

print("Enter long list")
n = int(input())
i = 0
list1 = [random.randint(1,10) for i in range(n)]
print(list1)
i = 0
summ = 0
for i in range(n):
    if i % 2 != 0:
       summ += list1[i]
print(f"sum = {summ}")