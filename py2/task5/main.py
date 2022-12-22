#Реализуйте алгоритм перемешивания списка.
# (рандомно поменять местами элементы списка между собой)
import random

print("Enter nuber")
n = int(input())
temp = 0
list1 = [random.randint(-n,n) for i in range(n)]
print(list1)
print(random.sample(list1,n))

