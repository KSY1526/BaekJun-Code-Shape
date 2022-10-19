import sys
sys.setrecursionlimit(10**6)

N, L, R = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while (True):
    # 국경선 해제된 곳 기록하기 위한 리스트
    lst_X = [[False] * N for _ in range(N)] # 상하
    lst_Y = [[False] * N for _ in range(N)] # 좌우


    # 탐색을 통해 국경선 해제된 곳 기록
    for i in range(N):
        for j in range(N):
            x = i + 1
            if (x < N):
                tem = abs(lst[x][j] - lst[i][j])
                if (abs(tem) >= L) and (abs(tem) <= R):
                    lst_X[i][j] = True

            y = j + 1
            if (y < N):
                tem = abs(lst[i][y] - lst[i][j])
                if (abs(tem) >= L) and (abs(tem) <= R):
                    lst_Y[i][j] = True


    # 국경 해제된 곳 탐색해 연합 리스트 만들기

    def dfs(x, y, t_lst):
        t_lst.add((x,y))
        
        # 정방향 탐색
        if lst_X[x][y]:
            lst_X[x][y] = False
            dfs(x+1, y, t_lst)
        if lst_Y[x][y]:
            lst_Y[x][y] = False
            dfs(x, y+1, t_lst)

        # 역방향 탐색
        if x > 0:
            if lst_X[x-1][y]:
                dfs(x-1, y, t_lst)
        if y > 0:
            if lst_Y[x][y-1]:
                dfs(x, y-1, t_lst)

        

        return


    graphs = []

    for i in range(N):
        for j in range(N):
            tem_set = set()
            dfs(i, j, tem_set)

            if len(tem_set) > 1:
                graphs.append(tem_set)

    if len(graphs) == 0:
        break
    # 연합 그래프 바탕으로 인구 재배치하기
    for graph in graphs:
        _sum = 0
        for x, y in graph:
            _sum += lst[x][y]
        _sum = _sum // len(graph)
        for x, y in graph:
            lst[x][y] = _sum
    
    # 하루가 지났습니다.
    cnt += 1

print(cnt)
