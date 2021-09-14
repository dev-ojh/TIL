# 진기의 최고급 붕어빵
T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    bread = list(map(int, input().split()))
    bread = sorted(bread)
    j = 0
    cnt = 0

    result = 'Possible'
    if bread[j] < M:
        result = 'Impossible'
    else:
        for i in range(1, 11112):
            if i % M == 0:
                cnt += K
            while j < N and bread[j] == i:
                if cnt == 0:
                    result = 'Impossible'
                    break
                cnt -= 1
                j += 1
            if result =='Imposiible' or j == N:
                break
    print(f'#{tc} {result}')