from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 각 도시별로 1, 2.. 숫자로 번호 매기는 BFS
# 이 과정은 DFS로 진행해도 무방
def bfs1(x, y, cnt):
    q.append([x, y])
    c1[x][y] = cnt # 입력할 숫자. 매번 달라짐
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 땅이고 아직 색칠 안한 땅이면
                if a[nx][ny] == 1 and c1[nx][ny] == 0:
                    # 바로 색칠 해줘야 큐 사용량이 줌.(중요)
                    c1[nx][ny] = cnt
                    q.append([nx, ny])

# 도시별로 다리 길이 구하는 BFS
def bfs2(num):
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 만약 다른 도시 땅을 만났다면
                if a[nx][ny] == 1 and c1[nx][ny] != num:
                    # 그동안 간 경로 길이만큼 리턴해줌.
                    return c2[x][y]-1

                # 바다라면 + 이전에 발자국이 없는 땅이라면(최단거리)
                if a[nx][ny] == 0 and c2[nx][ny] == 0:
                    # 경로를 1씩 추가해줌. BFS만의 최단거리 업데이트 메커니즘.
                    c2[nx][ny] = c2[x][y] + 1
                    q.append([nx, ny])

n = int(input())
# 입력받은 리스트
a = [list(map(int, input().split())) for _ in range(n)]

# 도시별로 구분하기 위해 만든 리스트, BFS1로 학습할것.
c1 = [[0]*n for _ in range(n)]

#q, q2 = deque(), deque()
cnt = 1

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and c1[i][j] == 0:
            bfs1(i, j, cnt)
            cnt += 1 # 다른 값으로 색칠해야함

ans = sys.maxsize
for k in range(1, cnt):
    q = deque()
    # 최단 거리 측정 행렬
    c2 = [[0] * n for _ in range(n)]

    # 도시에 있는 모든 땅 큐에 저장
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and c1[i][j] == k:
                q.append([i, j])
                c2[i][j] = 1 # 도시 내 땅에 발자국 남기기
    res = bfs2(k)
    ans = min(ans, res) # 최솟값 계속 업데이트
print(ans)
