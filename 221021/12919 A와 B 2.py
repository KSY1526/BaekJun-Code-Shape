# s -> t가 아닌 t -> s로
# s -> t로 하면 최대 문자열이 50이기 때문에 2의50승. 어마어마함
# 완성된 문자에서 탐색하면 경우의 수 줄일 수 있음
# 1) 뒤에 A 추가 : 뒷 문자가 A인 경우만 가능
# 2) B 추가 뒤 문자열 뒤집음 : 앞 문자가 B인 경우만 가능
# 미로를 풀때도 정답 위치에서 찾으면 쉽듯이로 기억.
import sys
sys.setrecursionlimit(10**6)

S = input()
T = input()

s_len = len(S)
ans = 0

def dfs(t):
    global ans
    if len(t) == s_len:
        if S == t: # 문자열이 같다면
            ans = 1
        return

    if t[-1] == 'A':
        dfs(t[:-1])

    if t[0] == 'B':
        dfs(t[1:][::-1])

    return

dfs(T)

print(ans)
