# Задайте натуральное число N. Напишите
# программу, которая составит список простых множителей числа N.

print("Enter number: ", end=" ")
n = int(input())
def operator(n):
   i = 2
   list1 = []
   while i * i <= n:
       while n % i == 0:
           list1.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       list1.append(n)
   return list1
print(operator(n))
