# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input())
f1 = 0
f2 = 1
i = 0
list1 = []
for i in range(n):
    f1, f2 = f2, f1 - f2
    f1 = f1 * -1
    f2 = f2 * -1
    list1.append(f1)
    list1.sort()
list1.append(0)
i=0
f1=0
f2=1
for i in range(n):
    f1, f2 = f2, f1 + f2
    list1.append(f1)
print(list1)
