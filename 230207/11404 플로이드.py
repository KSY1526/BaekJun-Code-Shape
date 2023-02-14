n = int(input()) # 도시 개수, 최대 100
m = int(input()) # 버스 개수

_inf = 10000001 # 최대 100000까지 비용이 나오므로

lst = [[_inf] * (n+1) for _ in range(n+1)]

for _ in range(m):
    i, j, cost = map(int, input().split())
    if lst[i][j] > cost: # 중복 값(i->j 여러 버스)이 들어올 경우
        lst[i][j] = cost # 더 작은 값만 들어오게 처리


# 시간복잡도 n^3, but n = 100이므로 거뜬.
for k in range(1,n+1): # k : 중립 지역
    for i in range(1,n+1): # i : 출발 지역
        for j in range(1, n+1): # j : 도착 지역
            # i -> j 보다 i -> k -> j가 더 가깝다면
            if (i != j) and (lst[i][j] > lst[i][k] + lst[k][j]):
                lst[i][j] = lst[i][k] + lst[k][j]

# 경로가 없는 경우(i->i도 포함)
for i in range(1, n+1):
    for j in range(1, n+1):
        if (lst[i][j] == _inf): # 경로가 없는 경우 == _inf  
            lst[i][j] = 0

# 최종 출력
for i in range(1, n+1):
    print(*lst[i][1:]) # print(*list) : 리스트 출력