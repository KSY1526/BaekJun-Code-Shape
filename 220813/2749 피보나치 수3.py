n = int(input())

x1 = 0
x2 = 1
#x3 = 1

if n == 1:
    print(x2)

else:
    for _ in range(n-1):
        x3 = (x1 + x2) % 1000000
        tem = x3
        x1 = x2
        x2 = tem

    print(x3)
