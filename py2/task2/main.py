# Напишите программу, которая
# принимает на вход число N и выдает набор произведений чисел от 1 до N.

print("Enter number")
n = int(input())
i = 0
sum = 1
for i in range(1,n+1):
   sum = sum * i
   print(sum)

