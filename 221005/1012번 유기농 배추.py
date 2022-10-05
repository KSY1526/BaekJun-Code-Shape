import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    lst = [[0] * n for _ in range(m)] # 2X2 리스트 생성, 가로 세로 바꿔서 실행함.
    for _ in range(k):
        x, y  = map(int, input().split())
        lst[x][y] = 1


    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    def dfs(x, y):
        lst[x][y] = 0

        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if n_x < 0 or n_y < 0 or n_x >= m or n_y >= n:
                continue
            elif (lst[n_x][n_y] == 1):
                dfs(n_x, n_y)

    ans = 0
    for i in range(m):
        for j in range(n):
            if lst[i][j] == 1:
                dfs(i, j)
                ans += 1

    print(ans)

