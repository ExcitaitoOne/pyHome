# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

list1 = []
print(f"Enter the sequence")
list1 = [int(input()) for i in range(5)]
print(list1)
long = len(list1)
i = 0
list2 = list1[0:0]
for i in range(long):
    if list1[i] in list2:
        continue
    list2.append(list1[i])
print(list2)
