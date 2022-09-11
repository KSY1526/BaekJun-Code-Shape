n, k = map(int, input().split())

# 데이터 저장 행렬 (무게, 가치)
dat = []
for _ in range(n):
    dat.append(list(map(int, input().split())))

# dist[i][j] : i번째 제품까지 사용 + j인 무게 제한 상황에서
# 최대 가능한 가치 값 저장.
# 이 값을 i,j가 0일때부터 계속 업데이트 하여(동적 계획)
# 모든 물건 사용 + k인 무게 제한 상황에서 최대 가치값 구함.
dist = [ [0] * (k+1) for _ in range(n) ]

# 초기 값 넣기
dist[0] = [0] * dat[0][0] + [dat[0][1]] * (k+1 - dat[0][0])

for i in range(1, n):
    tem = dat[i][0] # 이번제품 무게 저장
    
    for j in range(k+1):
        # 이번제품보다 작은 무게는 업데이트가 안됨(넣을수가 없음)
        if j < tem:
            dist[i][j] = dist[i-1][j]
        else:
            # 이번 제품 신경 안쓰기 vs 이번제품 넣고 다른것들 빼기
            dist[i][j] = max(dist[i-1][j], dist[i-1][j-tem] + dat[i][1])

print(dist[n-1][k])





