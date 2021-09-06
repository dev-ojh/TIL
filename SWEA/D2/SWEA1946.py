# 간단한 압축 풀기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    test=''
    for _ in range(N):
        char, M = input().split()
        test += char*int(M)
    print(f'#{tc}')
    for i in range(0, len(test),10):
        print(test[i:i+10])