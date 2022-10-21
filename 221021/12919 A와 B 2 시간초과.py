import sys
from collections import Counter
sys.setrecursionlimit(10**6)

S = input()
T = input()

s_count = Counter(S)
t_count = Counter(T)

t_len = len(T)

ans = 0

def dfs(s):
    global ans
    if len(s) == t_len:
        if s == T: # 문자열이 같다면
            ans = 1
        return

    # 백트레킹?
    if t_count['A'] - s_count['A'] > 0: # 'A'를 사용할 공간이 남아있다면
        s_count['A'] += 1
        dfs(s + 'A')
        s_count['A'] -= 1

    if t_count['B'] - s_count['B'] > 0: # 'B'를 사용할 공간이 남아있다면
        s_count['B'] += 1
        dfs((s + 'B')[::-1])
        s_count['B'] -= 1

    return

dfs(S)

print(ans)
