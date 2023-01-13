#вычислить число c заданной точностью d

print("enter number")
n = float(input())
print("enter d")
d = float(input())
s = str(d)
long = abs(s.find('.') - len(s)) - 1
summ = round(n, long)
print(summ)
