import sys
import heapq
# 입력함수를 바꿔주지 않으면 시간초과
input = sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    tem = int(input())
    if tem == 0:
        if len(lst) == 0:
            print(0)
        else:
            print(heapq.heappop(lst))
    else:
        heapq.heappush(lst, tem)
