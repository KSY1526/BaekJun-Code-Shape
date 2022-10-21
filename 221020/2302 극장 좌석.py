n = int(input())
m = int(input())

value_lst = [0] * (m+1) # 차이 기록 리스트

pred = 0
for i in range(0, m):
    value = int(input())
    value_lst[i] = value - pred - 1
    pred = value

value_lst[m] = n - pred

maxs = max(value_lst)

cnt_lst = [1, 1]

if maxs >= 2:
    for i in range(2, maxs+1):
        tem = cnt_lst[i-2] + cnt_lst[i-1]
        cnt_lst.append(tem)

ans = 1

for i in value_lst:
    ans = ans * cnt_lst[i]

print(ans)
