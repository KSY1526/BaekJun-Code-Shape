import sys

n = int(input())
values = input()

number = [] # 숫자 저장
oper = [] # 기호 저장

for i, value in enumerate(values):
    if i % 2 == 0:
        number.append(int(value))
    else:
        oper.append(value)

maxs = -sys.maxsize

def operation(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def dfs(swichs, idx, opers, numbers):
    global maxs

    if len(opers) == idx: # 커서가 마지막 수식까지 도달했다면
        num_1 = numbers[0]
        cnt = 1

        for i in opers:
            num_2 = numbers[cnt]
            num_1 = operation(num_1, num_2, i)
            cnt += 1
        
        if num_1 > maxs:
            maxs = num_1

        return    

    if swichs: # 앞 연산자에서 괄호 사용
        # 연산 바로 해버리기
        tem = operation(numbers[idx],numbers[idx+1],opers[idx])
        dfs(False, idx, opers[:idx] + opers[idx+1:], numbers[:idx] + [tem] + numbers[idx+2:])
        #dfs(True, idx, opers[:idx] + opers[idx+1:], numbers[:idx] + [tem] + numbers[idx+2:])

    else:
        dfs(False, idx+1, opers, numbers)
        dfs(True, idx+1, opers, numbers)


dfs(True, 0, oper, number)
dfs(False, 0, oper, number)

print(maxs)


