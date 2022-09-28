n = int(input())

house = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

def dfs(swichs, x, y):
    global cnt
    if (x == n) or (y == n) or (house[x][y] == 1):
        return
    if (x == n - 1) and (y == n-1):
        if swichs == 3 and (house[x][y-1] == 1 or house[x-1][y] == 1):
            return
        else:
            cnt += 1
            return

    if swichs == 1:
        dfs(1, x, y+1)
        dfs(3, x+1, y+1)
    
    elif swichs == 2:
        dfs(2, x+1, y)
        dfs(3, x+1, y+1)

    elif swichs == 3:
        if house[x][y-1] == 1 or house[x-1][y] == 1:
            return
        
        else:
            dfs(1, x, y+1)
            dfs(2, x+1, y)
            dfs(3, x+1, y+1)

# 이 부분 안하면 시간초과 남
if house[n-1][n-1] == 0:
    dfs(1,0,1)
print(cnt)



