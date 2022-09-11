import heapq
import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

heap1 = [] # 중앙값 이전 힙(최대 힙)
heap2 = [] # 중앙값 이후 힙(최소 힙)

if n == 1:
    print(lst[0])
elif n == 2:
    print(lst[0])
    if lst[0] < lst[1]:
        print(lst[0])
    else:
        print(lst[1])
else:
    print(lst[0])
    if lst[0] < lst[1]:
        heapq.heappush(heap1, -lst[0])
        heapq.heappush(heap2, lst[1])
        print(lst[0])
    else:
        heapq.heappush(heap1, -lst[1])
        heapq.heappush(heap2, lst[0])
        print(lst[1])
        
    swichs = True
    for i in lst[2:]:
        if swichs: # 현재 짝수개일때
            swichs = False
            tem = - heap1[0] # 최댓값(추출 우선순위)는 0 인덱스에 존재

            if tem < i: # 꺼낸 친구가 더 작다면
                heapq.heappush(heap2, i)
                tem2 = heapq.heappop(heap2) # 최솟값 추출
                print(tem2)
                heapq.heappush(heap1, -tem2)
            else: # 더 크다면
                print(tem)
                heapq.heappush(heap1, -i)
                
        else: # 현재 홀수개일때
            swichs = True
            tem = - heap1[0] # 최댓값(추출 우선순위)는 0 인덱스에 존재

            if tem < i: # 꺼낸 친구가 더 작다면
                print(tem)
                heapq.heappush(heap2, i)
                
            else: # 더 크다면
                tem2 = - heapq.heappop(heap1)
                heapq.heappush(heap2, tem2)
                heapq.heappush(heap1, - i)
                print(-heap1[0])
    
