H, W, N, M = map(int, input().split())

x = H // (N+1)
if H % (N+1) > 0:
    x += 1

y = W // (M+1)
if W % (M+1) > 0:
    y += 1

print(x * y)


