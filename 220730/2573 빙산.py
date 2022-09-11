import sys
# dfs 사용시 파이썬 재귀 에러 해결
# 10 ** 6으로 하면 메모리 초과 생김
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
ices = []

visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, j):
    if (ices[i][j] <= 0) or (visited[i][j] == True):
        return
    visited[i][j] = True
    
    
    for k in range(4):
        dfs(i + dx[k], j + dy[k])
        
    return
    


for _ in range(n):
    tem = list(map(int, input().split()))
    ices.append(tem)


num = 0
swichs = True
while swichs:
    num = num + 1
    
    # 배열의 첫 행과 첫 열은 무조건 0이다.
    for i in range(1, n):
        for j in range(1, m):
            if ices[i][j] == 0:
                continue
            for k in range(4):
                if ices[i+dx[k]][j+dy[k]] == 0:
                    ices[i][j] = ices[i][j] - 1

                if ices[i][j] == 0:
                    # 방금 물로 바뀐 공간은 현재 얼음에 영향을 끼치지 못함.
                    # -1로 처리, 이후 0으로 변경
                    ices[i][j] = ices[i][j] - 1
                    break

    swichs = True
    for i in range(1, n):
        for j in range(1, m):
            # 처음으로 얼음 발견시 dfs 탐색
            if (ices[i][j] > 0) and (swichs):
                dfs(i, j)
                swichs = False

            # 방금 물로 바뀐 공간 0으로 다시 돌림.
            elif ices[i][j] == -1:
                ices[i][j] = 0
                

    # 만약 얼음을 발견하지 못했다면
    if swichs:
        print(0)
        break

    swichs = True
    
    for i in range(1, n):
        for j in range(1, m):
            # 얼음이 있는 곳인데 dfs로 방문하지 못했다면
            # 얼음이 분리된 것.
            if (ices[i][j] > 0) and (visited[i][j] == False):
                print(num)
                swichs = False
                break
        if swichs == False:
            break
        
    # 방문기록 초기화
    visited = [[False] * m for _ in range(n)]


        
