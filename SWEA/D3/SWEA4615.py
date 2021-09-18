# 오셀로
import pprint
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    dy = [1, 0, 1, -1, 0, -1, 1, -1]
    dx = [0, 1, 1, 0, -1, -1, -1, 1]
    cnt_black = 0
    cnt_white = 0
    if N == 4:
        arr[2][2] = arr[3][3] = 2
        arr[2][3] = arr[3][2] = 1
    if N == 6:
        arr[3][3] = arr[4][4] = 2
        arr[3][4] = arr[4][3] = 1
    if N == 8:
        arr[4][4] = arr[5][5] = 2
        arr[4][5] = arr[5][4] = 1
    for _ in range(M):
        x, y, color = map(int, input().split())
        arr[y][x] = color
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            while (N >= ny > 0) and (N >= nx > 0) and (arr[ny][nx] != 0):
                if arr[ny][nx] == color:
                    while ny != y or nx != x:
                        ny -= dy[i]
                        nx -= dx[i]
                        arr[ny][nx] = color
                    break
                else:
                    ny += dy[i]
                    nx += dx[i]
                        
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                cnt_black += 1
            elif arr[i][j] == 2:
                cnt_white += 1
    print(f'#{tc} {cnt_black} {cnt_white}')
    
