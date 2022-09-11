n = int(input())

num = []

for _ in range(n):
    num.append(list(map(int, input().split())))

# 정렬에서 색깔 기준으로 정렬.
# 그 이후 같은 색깔 내 위치 순으로 정렬
num = sorted(num, key = lambda x : (x[1], x[0]))
cnt = len(num)

# 첫 값은 무조건 두번째 값에 화살표를 그음
# 마지막 값은 직전 값에 화살표를 그음
ans = (num[1][0] - num[0][0]) + (num[cnt-1][0] - num[cnt-2][0]) 

for i in range(1, cnt -1):
    col = num[i][1]
    # 이전 색깔과 다른 색깔인 경우
    if num[i-1][1] != col:
        # 다음 색깔이 지금 색깔과 같은게 보장되어 있으므로
        ans += (num[i+1][0] - num[i][0])
    # 반대로 이전 색깔은 같은데 다음 색깔이 다른경우
    elif num[i+1][1] != col:
        ans += (num[i][0] - num[i-1][0])
    # 모든 색깔(이전과 다음 색깔)이 똑같은 경우.
    else:
        ans += min(num[i+1][0] - num[i][0], num[i][0] - num[i-1][0])

print(ans)

