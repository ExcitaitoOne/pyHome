#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в отдельном
# списке ( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

import random

print("Enter number")
n = int(input())
i = 0
a = 0
b = 0
print(f"Enter element list (less than {n})")
if a < n and b < n:
    a = int(input())
    b = int(input())
else:
    print("error")

list1 = [random.randint(-n,n) for i in range(n)]
list2 = [a,b]
print(list1)
print(f"{list2}")
summa = list1[list2[0]] * list1[list2[1]]
print(f"Произведение элементов = {summa}")
