# N이 10이니깐 완전 탐색도 가능하지 않을까??
# 연결 성분 두 개로 나누고 인구수 비교.
# 연결 성분 두 개로 나누는 것은 백트래킹으로 하기.
# 연결성분이 되는지는 bfs로 확인

from collections import deque

N = int(input())

ans = 10000
graph = [[0] * (N+1) for _ in range(N+1)] # 1~N 까지이기 때문.

peoples = [0] + list(map(int, input().split()))

for i in range(1,N+1):
    lines = list(map(int, input().split()))
    for j in lines[1:]:
        graph[i][j] = 1

def check(v): # v : 요소 리스트 ex) [1,2,3]
    _visited = [False] * (N + 1)
    _visited[v[0]] = True
    q = deque()
    q.append(v[0])

    while q:
        value = q.popleft()

        for i in v:
            if graph[value][i] and _visited[i] == False:
                _visited[i] = True
                q.append(i)

    for i in v:
        if _visited[i] == False:
            #print(_visited)
            return False

    return True


# n : 첫번째 연결성분 원소 개수, cnt : 카운트 해주는 변수
def backtracking(n, cnt):
    global ans
    # 첫번째 연결성분 원소 모두 찾았을 때
    if cnt == n:
        v1 = []
        v2 = []
        v1_peo = 0
        v2_peo = 0
        for i in range(1, N+1):
            if visited[i] == True:
                v1.append(i)
                v1_peo += peoples[i]
            else:
                v2.append(i)
                v2_peo += peoples[i]

        if check(v1) and check(v2): # 연결성분이 되는지 확인
            ans = min(ans, abs(v1_peo - v2_peo))

        return            
    
    # 백트레킹 핵심부분.
    for i in range(1, N+1):
        if visited[i] == False:
            visited[i] = True
            backtracking(n, cnt+1)
            visited[i] = False

for i in range(1, N // 2 + 1):
    visited = [False] * (N+1)
    backtracking(i, 0)

if ans == 10000:
    ans = -1
print(ans)