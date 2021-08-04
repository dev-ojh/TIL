# 파리 퇴치 NxN배열안에 존재하는 파리 숫자를
# MXM파리채 면적 안에 있는 최대 파리숫자를 출력

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    section = []
    for i in range(N):  # 파리가 들어있는 면적에 파리들을 각각 배치한다.
        section.append(list(map(int, input().split())))
    
    cnt = 0 #파리채 면적안의 파리수
    max = 0 #파리채 면적안 파리수의 최대값
    for i in range(N-M+1):  #파리채의 y좌표 시작점
        for j in range(N-M+1):  #파리채의 x좌표 시작점
            for m in range(M):  #파리채 y좌표
                for n in range(M):  #파리채 x좌표
                    cnt += section[i+m][j+n]    
            if max < cnt:   # 최대치 비교후 최대치 갱신
                max = cnt
            cnt = 0 #파리채 면적안 파리수를 다시 초기화
    print(f'#{test_case} {max}')
