import sys
input=sys.stdin.readline

r, c = map(int, input().split())

# 굳이 visited 변수 쓸필요 x
# 같은 알파벳이 있는지 여부를 따지면 커버 가능
# visited = [ [0] * c for _ in range(r) ]

lst = []
for i in range(r):
    tem = list(input())
    # 처음부터 알파벳이 아닌 아스키코드 값을 넣어주자
    lst.append(list(map(lambda x : ord(x) - 65, tem)))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
alph = [0] * 26
maxs = 0
def dfs(x, y):
    global maxs

    # if lst[x][y] in cnt: 은 시간초과 발생.
    # in 연산자가 시간을 많이 먹음
    if alph[lst[x][y]] == 1:
        maxs = max(maxs, sum(alph))
        return
    alph[lst[x][y]] = 1
    #visited[x][y] = 1
    
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or xx >= r or yy < 0 or yy >= c:# or visited[xx][yy] == 1:
            continue
        
        dfs(xx, yy)

    alph[lst[x][y]] = 0
    #visited[x][y] = 0
dfs(0,0)
print(maxs)
        
