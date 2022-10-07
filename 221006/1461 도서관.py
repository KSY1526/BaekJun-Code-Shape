n,m = map(int, input().split())

ans = 0
lst = list(map(int, input().split()))

p_lst = [] # 양수 리스트
n_lst = [] # 음수 리스트

for i in lst:
    if i > 0:
        p_lst.append(i)
    else:
        n_lst.append(-i)

# 결국 가장 큰 값을 막차로 쓰는게 이동 경로를 최소화함
# (다른 경로는 다 0으로 돌아와서 책을 가져가야 하기 때문)

p_len = len(p_lst)
n_len = len(n_lst)

p_lst.sort(reverse= True)
n_lst.sort(reverse= True)

for i in range(0, p_len, m):
    ans += p_lst[i] * 2

for i in range(0, n_len, m):
    ans += n_lst[i] * 2

if p_len == 0:
    ans = ans - n_lst[0]

elif n_len == 0:
    ans = ans - p_lst[0]

elif p_lst[0] > n_lst[0]:
    ans = ans - p_lst[0]

else:
    ans = ans - n_lst[0]

print(ans)