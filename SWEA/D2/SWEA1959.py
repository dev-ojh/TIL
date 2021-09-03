# 2개의 숫자열
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_cnt = 0
    
    if N > M:
        for i in range(0, N-M+1):
            cnt = 0
            for j in range(M):
                cnt += B[j] * A[i+j]
            if max_cnt < cnt:
                max_cnt = cnt
    else:
        for i in range(0, M-N+1):
            cnt = 0
            for j in range(N):
                cnt += B[i+j] * A[j]
            if max_cnt < cnt:
                max_cnt = cnt
    print('#{} {}'.format(tc, max_cnt))