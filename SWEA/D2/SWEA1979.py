# N*N 퍼즐에서 검은색 부분(0으로 입력)을 제외하고
# 흰색부분(1으로 입력)에 K길이의 단어를 입력하고자함.
# 단어가 들어갈 수 있는 자리가 몇개인지 출력

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):   #기본 값들을 입력받는과정
    N, K = map(int, input().split())
    puzzle = [[0]*(N+2)]    # 첫행을 0으로 나열된 N보다 2긴 행을 입력(배열을 0으로 감싸기 위함)
    result = 0  # 출력하고자하는 공간 갯수를 초기화
    
    for i in range(1, N+1): # 0,1로 표현된 퍼즐을 입력받는 과정
        test = [0]  # 매행의 첫열도 0
        test += (list(map(int, input().split()))) #입력받는 값을 행에 저장
        test.append(0)  #매행의 마지막 열도 0
        puzzle.append(test)
    puzzle.append([0]*(N+2))    #마지막 행 역시 0으로 가득찬 리스트 입력
    
    for i in range(1, N+1): # 초기 0은 0으로 비어있는 행렬이므로 무시하고 1인 행렬부터 끝까지 입력
        for j in range(1, N-K+2):   # 역시 1부터 단어길이까지 핵심 변수 위치를 조정하며 조건에 맞는지 확인
            if puzzle[i][j] == 1 and puzzle[i][j+K] == 0 and puzzle[i][j-1] == 0: #양끝이 0이며 처음 위치가 1인지확인
                for k in range(1, K):   #단어길이만큼 1로채워져있는지 확인하고 조건을 만족하면 최종값에 1개 추가
                    if puzzle[i][j+k] != 1:
                        break
                else: 
                    result += 1

            if puzzle[j][i] == 1 and puzzle[j+K][i] == 0 and puzzle[j-1][i] == 0:   #행열 위치를 바꾸어 한번의 반복문에 모든것을 해결하기 위함
                for k in range(1, K):
                    if puzzle[j+k][i] != 1:
                        break
                else:
                    result +=1
        
    
    print(f'#{test_case} {result}')
