num = int(input())
cnt = int(input())

visited = [0] * (num+1)
lines = [ [0] for _ in range(num+1) ]


for _ in range(cnt):
    i, j = map(int, input().split())
    lines[i].append(j)
    lines[j].append(i)

def dfs(x):
    visited[x] = 1
    
    for i in range(1, len(lines[x])):
        tem = lines[x][i]
        if visited[tem] == 1:
            continue
        dfs(tem)

dfs(1)

print(sum(visited) - 1)
