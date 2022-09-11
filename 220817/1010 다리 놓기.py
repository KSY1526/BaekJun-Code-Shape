t = int(input())

for _ in range(t):
    # mCn을 구하면 됨 math.comb(m, n)
    # 다만 DP 방법으로 문제를 풀어봄
    n, m = map(int, input().split())
    tem = m - n
    dat = [ [0] * (tem+1) for _ in range(n+1) ]
    # [ 선택할 개수 ] [ m - n : 유동적인 개수 ]
    # 3,2 => 2,2 + 2,1 + 2,0
    # 2,2 => 1,2 + 1,1 + 1,0
    # 2,1 => 1,0 + 1,1
    # 1,2 => 3
    # 1,0 => 1
    # 1,1 => 2

    for i in range(tem+1):
        # 만약 1개를 선택한다면 경우의수 i+1
        # 초기값 깔아주기
        dat[1][i] = i+1

    if n > 1:
        for i in range(2, n+1):
            for j in range(tem+1):
                for k in range(j+1):
                    dat[i][j] += dat[i-1][k]

    print(dat[n][tem])
    
    
    
