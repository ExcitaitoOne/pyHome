#Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов

f1 = open("1.txt", "r").read().split(" ")
f2 = f1[0].split("x")
f3 = f1[4].split("x")
print(f1, f2, f3)
d1 = open("2.txt", "r").read().split(" ")
d2 = d1[0].split("x")
d3 = d1[4].split("x")
print(d1, d2, d3)
list1 = f1
f2[0] = int(f2[0])
d2[0] = int(d2[0])
list1[0] = f2[0] + d2[0]
f3[0] = int(f3[0])
d3[0] = int(d3[0])
list1[4] = f3[0] + d3[0]

list1[0] = str(list1[0])
list1[0] = list1[0] + "x"

list1[4] = str(list1[4])
list1[4] = list1[4] + "x"

f1[6] = int(f3[0])
d1[6] = int(d3[0])
list1[6] = f1[6] + d1[6]
list1[6] = str(list1[6])
list1[6] = str(list1[6])
print(list1)
m = open("sum.txt", "w")
for i in list1:
   m.write(i)

m.close()
