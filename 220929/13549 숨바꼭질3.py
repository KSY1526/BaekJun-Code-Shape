from collections import deque

x = [-1] * 100001 # 위치

n, k = map(int, input().split())


queue = deque()
queue.append((0, n)) # (횟수, 시작위치)

while queue:
    que = queue.popleft()
    tem = que[1]
    while (tem < 100001) and (tem >= 0):
        if x[tem] == -1:
            x[tem] = que[0]      
            queue.append((que[0] + 1, tem + 1))
            queue.append((que[0] + 1, tem - 1))
            tem = tem * 2
        else:
            break

    if x[k] != -1:
        print(x[k])
        break
        
    