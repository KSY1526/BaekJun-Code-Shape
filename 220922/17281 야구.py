from itertools import permutations

num = int(input())

lst = []

for _ in range(num):
    lst.append(list(map(int, input().split())))
    
idxs = [1,2,3,4,5,6,7,8]

maxs = -1

for idx in permutations(idxs, 8):
    orders = list(idx[:3]) + [0] + list(idx[3:])
    i = 0
    score = 0
    for n in range(num):
        out = 0
        base1, base2, base3 = 0, 0, 0
        tem = lst[n]
        while (out < 3):
            if tem[orders[i]] == 0:
                out += 1            
            elif tem[orders[i]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif tem[orders[i]] == 2:
                score += base2 + base3
                base1, base2, base3 = 0, 1, base1
            elif tem[orders[i]] == 3:
                score += base1 + base2 + base3
                base1, base2, base3 = 0, 0, 1
            elif tem[orders[i]] == 4:
                score += 1 + base1 + base2 + base3
                base1, base2, base3 = 0, 0, 0
            i = (i+1) % 9
        #score += sum(homes[:-3])

    if maxs < score:
        maxs = score

print(maxs)


