n = int(input())
dat = [0] * n
for i in range(n):
    dat[i] = int(input())

ans1 = [0] * n # 뒤에 안붙어있는 경우 최댓값 기록
ans2 = [0] * n # 뒤에 붙어있는 경우 최댓값 기록

ans1[0] = dat[0]
ans2[0] = dat[0]
if n > 1:
    ans1[1] = dat[1] # 뒤에 안 붙어 있어야
    ans2[1] = dat[0] + dat[1]

# ans1[2] = dat[2] + max(ans1[0], ans2[0]) 
# ans2[2] = dat[2] + ans1[1]

# ans1[3] = dat[3] + max(ans1[1], ans2[1]) 
# ans2[3] = dat[3] + ans1[2]
if n > 2:
    # 최댓값 계속 업데이트 하는 방식
    for i in range(2, n):
        ans1[i] = dat[i] + max(ans1[i-2], ans2[i-2])
        ans2[i] = dat[i] + ans1[i-1]
        
print(max(ans1[n-1], ans2[n-1]))
