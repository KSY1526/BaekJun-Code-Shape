import copy
import sys
from itertools import permutations


# 남 -> 동 -> 북 -> 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def rotate(rcs):
    r, c, s = rcs

    # s번 반복, 이때 s는 점점 커지는 사각형 띠 의미
    for i in range(1, s + 1): 
        # 왼쪽 위 값을 초기값
        # 그렇다면 초기값을 저장한 후 밀어내야함
        # 그래서 남 -> 동 -> 북 -> 서 형식이 필요.
        tmp = matrix[r-1-i][c-1-i] 
        x = r-1-i
        y = c-1-i

        # 동남서북 회전 반복
        for j in range(4):
            
            # 숫자 이동을 2 * s번씩 반복
            for _ in range(2 * i):
                nx = x + dx[j]
                ny = y + dy[j]
                matrix[x][y] = matrix[nx][ny]
                x, y = nx, ny

        # 마지막 값 보정
        matrix[r-1-i][c-i] = tmp


n, m, k = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

rcs_input = [list(map(int, input().split())) for _ in range(k)]

ans = sys.maxsize
for rcss in permutations(rcs_input):
    matrix = copy.deepcopy(a)
    for rcs in rcss:
        rotate(rcs)
    for row in matrix:
        ans = min(ans, sum(row))
        
print(ans)
