# 같은 문자열이 반복되는 마디의 길이를 구하는 문제
# 마디 최대길이가 10이고 각 문자열 길이가 30

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    words = input() #단어입력
    
    for i in range(1, 11):  #길이가 10이니까 10길이까지 판별한다
        word = words[0 : i] #판별하고자하는 문자열
        cnt = 0
        for j in range(3):  #최대 반복횟수가 3번이므로(30/10) 3번 반복해서 문자열이 나오는지 확인
            if word == words[i * j : (i * j) + i]: #문자열이 나오는 횟수를 보기위한 판별문
                cnt += 1
            else:
                break
        if cnt == 3:
            print(f'#{test_case} {i}')
            break
            
    

