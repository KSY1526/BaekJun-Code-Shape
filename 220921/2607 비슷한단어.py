from collections import Counter

num = int(input())

f_word = input() # 첫번째 단어
f_word = Counter(f_word)

answer = 0

for i in range(num-1):
    n_word = input() # 새로운 단어
    lens = len(n_word) # 길이 저장
    n_word = Counter(n_word)
    ans = 1
    swichs1 = False
    swichs2 = False
    swichs3 = False
    for k, v in f_word.items():
        lens -= n_word[k] # 단어 길이 중 이 만큼의 단어는 사용했다.
        if abs(n_word[k] - v) > 1: # 기존단어와 새 단어의 글자 개수 차이가 2이상인 경우.
            swichs1 = True
            ans = 0 # 미련 없이 보내줌
            break

        elif (n_word[k] - v == 1): # 새로운 단어가 하나 더 많은 경우
            if swichs2: # 두번째로 적발된 경우
                swichs1 = True
                ans = 0 # 미련없이 보내줌
                break
            
            else:
                swichs2 = True
        
        elif (n_word[k] - v == -1): # 기존 단어가 하나 더 많은 경우
            if swichs3: # 두번째로 적발된 경우
                swichs1 = True
                ans = 0 # 미련없이 보내줌
                break
            else:
                swichs3 = True

    if swichs1 == False:
        if lens > 1: # 기존단어와 다른 쓰임이 1개 이상 있다
            ans = 0 # 보내줌
        elif lens == 1: # 스위치2가 켜저있으면 안됨. 스위치3은 괜찮음
            # ex) 기존단어 AABC, 새로운단어 AAABCD 불가능. 기존단어 AABC, 새로운단어 ABCD 가능. 
            if swichs2:
                ans = 0
    answer += ans        

print(answer)