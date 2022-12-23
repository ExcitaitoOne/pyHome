# Напишите программу, которая найдёт
# произведение пар чисел списка. Парой считаем первый и
# последний элемент, второй и предпоследний и т.д.

import random

print("enter long list")
n = int(input())
summ = 0
list1 = [random.randint(1,10) for i in range(n)]
longest = len(list1) - 1
print(list1)
i = 0
for i in range(n):
    if i <= n/2:
        summ = list1[i] * list1[longest-i]
        print(f"sum = {summ}")