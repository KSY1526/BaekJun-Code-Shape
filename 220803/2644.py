people = int(input())
input1, input2 = map(int, input().split())
num = int(input())

lines = [ [0] for _ in range(people+1) ]

for _ in range(num):
    i, j = map(int, input().split())
    lines[i].append(j)
    lines[j].append(i)

ans = 101

def dfs(start, cnt):
    visited[start] = 1
    global ans
    if start == input2:
        ans = min(cnt, ans)
        return
    
    for i in lines[start][1:]:
        if visited[i] == 1:
            continue
        dfs(i, cnt+1)
        
for k in lines[input1][1:]:
    # 매번 방문기록 초기화
    visited = [0] * (people + 1)
    dfs(k, 1)

if ans == 101:
    ans = -1
print(ans)
