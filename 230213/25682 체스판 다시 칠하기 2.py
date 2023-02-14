import sys

# 입력함수 효율적인 함수로 대체
input = sys.stdin.readline

n, m, k = map(int, input().split())

col_lst = [list(input()) for _ in range(n)]

# 누적합 공식 사용하여 cnt 구함.
def check(color):
    sum_lst = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n):
        for j in range(m):
            if (i+j) % 2 == 0:
                if col_lst[i][j] == color:
                    sum_lst[i+1][j+1] += 1
            else:
                if col_lst[i][j] != color:
                    sum_lst[i+1][j+1] += 1

            sum_lst[i+1][j+1] = sum_lst[i+1][j+1] + sum_lst[i][j+1] + sum_lst[i+1][j] - sum_lst[i][j]

    cnt = k * k + 1

    for i in range(0, n - k + 1):
        for j in range(0, m - k + 1):
            cnt = min(cnt, sum_lst[i+k][j+k] - sum_lst[i][j+k] - sum_lst[i+k][j] + sum_lst[i][j])

    return cnt

print(min(check('B'), check('W')))
