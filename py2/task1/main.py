#Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.

print("введите число")
x = float(input())
i = 0
ost = 0
summa = 0
longest = len(str(x))
while x % 10 != 0:
    x = x * 10
    print(x)

while i < longest:
    ost = x % 10
    x = x // 10
    print(f"i = {i}; {ost}")
    summa = summa + ost
    i+=1
print(summa)
