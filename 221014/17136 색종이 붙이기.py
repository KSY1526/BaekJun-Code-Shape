import sys
sys.setrecursionlimit(10**6)

lst = [list(map(int, input().split())) for _ in range(10)]

num = 10
ans = 26
papers = [5, 5, 5, 5, 5]


def check(x, y, k):
    if (x + k >= num) or (y + k >= num):
        return False

    for i in range(k+1):
        for j in range(k+1):
            if lst[x+i][y+j] == 0:
                return False
    return True

def change_0(lst, x, y, k):
    for i in range(k+1):
        for j in range(k+1):
            lst[x+i][y+j] = 0
    return

def change_1(lst, x, y, k):
    for i in range(k+1):
        for j in range(k+1):
            lst[x+i][y+j] = 1
    return

def dfs(x, y, cnt, paper):
    global ans

    if x == num:
        ans = min(ans, cnt)

    elif y == num:
        dfs(x+1, 0, cnt, paper)

    elif lst[x][y] == 1:
        for k in range(5):
            if not check(x, y, k): # 다 1인지 + 범위안에 있는지
                break

            if paper[k] == 0: # 이 색종이는 더 이상 못쓰는 경우.
                continue

            change_0(lst, x, y, k)
            paper[k] = paper[k] - 1

            dfs(x, y + k + 1, cnt+1, paper)

            paper[k] = paper[k] + 1
            change_1(lst, x, y, k)


    else: # lst[x][y] == 1이 아닌경우
        dfs(x, y+1, cnt, paper)
    
    return

dfs(0,0,0,papers)

if ans == 26:
    ans = -1
print(ans)






