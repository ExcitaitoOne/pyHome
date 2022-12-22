# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
print("Enter number")
n = int(input())
i = 1
a = 0
list1 = [(1+1/i)**i for i in range(1,n+1)]
print(list1)
l = sum(list1)
print(l)



