t = int(input())

# 1일때 1 총 1개
# 2일때 11, 2 총 2개
# 3일때 111, 12, 3 총 3개
# 4일때 1111, 112, 22, 13 총 4개
# 1111은 매번있음. 112, 22는 2일때 값에서 2만 붙임, 13은 1일때 값에서 3만 붙임
# 즉 array[i] = array[i-2] + array[i-3] 라고 생각할 수 있으나
# 이렇게 되면 2붙인 것과 3붙인 것이 겹치게 됨. (23, 32)

array = [1] * 10001 # 모든숫자가 1인 경우 존재

for i in range(2, 10001):
    array[i] += array[i-2] # 1과 2만 사용했을때

for i in range(3, 10001):
    array[i] += array[i-3] # 3을 사용했다면

for _ in range(t):
    print(array[int(input())])


