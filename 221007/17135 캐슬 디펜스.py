from itertools import combinations
import copy

N, M, D = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

def atteck(x, d): # x는 행 위치, d는 현재 사거리
    start = max(0, x - d + 1)
    end = min(M-1, x + d - 1)

    swichs = False
    xx = 0
    yy = 0
    for i in range(start, end+1):
        # X : (현재 위치 - 좌우거리) = 상하거리
        if N - (d - abs(x - i)) < 0: # 중요한 예외처리
            continue
        tem = _lst[N - (d - abs(x - i))][i]

        if tem == 1:
            swichs = True
            xx = N - (d - abs(x - i))
            yy = i
            break

    return swichs, xx, yy

ans = 0


# 공격 (맞은 대상 기록)
# 맞은 적 제거(+ 기록)
# 적 한칸 전진
for peoples in combinations(range(M),3):
    cnt = 0
    _lst = copy.deepcopy(lst)
    for _ in range(N):
        recoder = []
        for i in peoples: # 궁수 공격
            for j in range(1, D+1): # 거리를 넓히며
                _swich, _x, _y = atteck(i, j)
                if _swich:
                    recoder.append([_x, _y])
                    break
        
        for k in recoder: # 맞은 적 제거
            if _lst[k[0]][k[1]] == 1:
                cnt += 1
                _lst[k[0]][k[1]] = 0

        _lst = [[0]*M] + _lst[:-1] # 적 한칸 전진

    ans = max(ans, cnt)

            
print(ans)



