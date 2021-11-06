# 오목 판별
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                k = 1
                row = 1
                col = 1
                diag = 1
                diag2 = 1
                while k < 5:
                    if j+k < N and arr[i][j+k] == 'o':
                        row += 1
                    if i+k < N and arr[i+k][j] == 'o':
                        col += 1
                    if i+k < N and j+k < N and arr[i+k][j+k] == 'o':
                        diag += 1
                    if i+k < N and j-k >= 0 and arr[i+k][j-k] =='o':
                        diag2 += 1
                    k += 1
                if row >= 5 or col >= 5 or diag >= 5 or diag2 >=5:
                    result = 'YES'
                    break
        if result == 'YES':
            break
    print('#{} {}'.format(tc, result))