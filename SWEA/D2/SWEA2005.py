# 파스칼의 3각형
# 크기가 N인 파스칼의 삼각형 만들기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    result = [[1], [1, 1]]  # 파스칼 삼각형 윗부분 초기화
    for i in range(2, N):   # 2부터 삼각형 리스트에 입력하기 위함
        pascal=[]
        for j in range(i + 1):
            if j == 0 or j == i:    # 각 줄의 양끝의 경우 1
                pascal.append(1)
            else:   # 위의 두숫자를 합하여 아래의 칸을 채우는것
                pascal.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(pascal)   #전체 결과에 한줄을 추가함
    
    print(f'#{test_case}')
    for i in range(N):
        for j in range(i + 1):
            print(result[i][j], end=' ')
        print()




    