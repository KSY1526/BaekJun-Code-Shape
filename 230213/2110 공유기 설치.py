# 문제 정의 : 정해진 개수 c개의 공유기를 최대한 멀리 떨구기
# => 정해진 거리 미만으로 공유기 설치를 못할 때 공유기 설치 최대 갯수 구하기.

n, c = map(int, input().split())

# 공유기 정보 받기
lst = [int(input()) for _ in range(n)]

lst.sort()

start = 1
end = lst[-1] - lst[0]

result = 0

while (start <= end):
    mid = (start + end) // 2 # 정해진 거리

    cnt = 1 # 첫 위치에 무조건 설치

    old = lst[0]
    for i in range(1, len(lst)):
        if (lst[i] - old) >= mid: # 정해진 거리보다 짧으면
            cnt += 1 # 설치
            old = lst[i] # 다음 거리 구하기
    
    if cnt >= c: # 공유기를 너무 많이 깔았다 => 정해진 거리 늘려야.
        start = mid + 1
        result = mid

    else: # 공유기를 너무 적게 깔았다. => 정해진 거리 줄여야.(너무 규제가 심핟..)
        end = mid - 1

print(result)