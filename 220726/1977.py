import math
m = int(input())
n = int(input())

m = math.sqrt(m)
n = math.sqrt(n)
tem = math.ceil(m)
sums = 0

while (n >= tem):
    sums += tem * tem
    tem += 1

if sums == 0:
    print(-1)
else:
    print(sums)
    print(math.ceil(m) * math.ceil(m))
