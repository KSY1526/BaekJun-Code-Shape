import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

k = int(input())
INF = sys.maxsize

# 그래프 인접 리스트로 구현
graph = [ [] * (n+1) for _ in range(n+1) ]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append( (b,c) ) # a에서 b까지 c가중치

distance = [INF] * (n+1)
heap = []

def Dijkstra(start):
    distance[start] = 0
    # heap : (지나온 거리, 시작위치)
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)
        # 이미 더 좋은 방안으로 간 경우 (방문 한 노드인경우)
        if distance[now] < dist:
            continue

        for i in graph[now]: # i[0] : 위치, i[1] : 거리
            cost = dist + i[1] # 같던 거리 + 갈 거리

            # 지금 구한 길 vs 이전에 구한 최단경로
            if cost < distance[i[0]]: 
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))
        
Dijkstra(k)

for i in range(1,n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])




    
