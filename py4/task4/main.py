#Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
from random import randint

x = 0
def XXX(x):
    x = randint(0,100)
    if x == 0:
        return
    return x

print("enter k ")
k = int(input())
if k == 0:
    print(0)
c = k
MyFile = open("textFor4.txt", "a+")
for i in range(k):
    MyFile.write(f"{XXX(x)}x**{c} + ")
    c = c - 1
MyFile.write(f"{XXX(x)} = 0")
MyFile.write("\n")
MyFile.close()



