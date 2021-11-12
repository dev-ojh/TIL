# 그래프의 삼각형
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x][y] = 1
    cnt = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if arr[i][j] == 1:
                for k in range(i+1, N+1):
                    if arr[j][k] == 1 and arr[i][k] == 1:
                        cnt += 1
    print('#{} {}'.format(tc, cnt))
