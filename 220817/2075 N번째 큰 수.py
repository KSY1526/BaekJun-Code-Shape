import sys
import heapq
input = sys.stdin.readline

n = int(input())
dat = []
lst = []

# 반복문 실시간으로 처리하지 않으면 공간초과
# 1500 * 1500 너무 메모리 큼
for _ in range(n):
    dat = list(map(int, input().split()))
    if not lst: # 첫 데이터라면
        for i in dat:
            heapq.heappush(lst, i)
    else:
        for i in dat:
            if lst[0] < i:
                heapq.heappop(lst)
                heapq.heappush(lst, i)

print(lst[0])
