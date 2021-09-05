#달팽이 숫자 출력


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    arr[0][0] = 1
    dr = [0, 1, 0, -1] 
    dc = [1, 0, -1, 0]
    cnt = 0
    tmp = 1
    r , c = 0 , 0
    while tmp < N*N :
        nr = r + dr[cnt]
        nc = c + dc[cnt]
        if 0 <= nr <N and 0 <= nc < N and arr[nr][nc]==0:
            arr[nr][nc] = arr[r][c] + 1
            tmp = arr[nr][nc]
            r, c = nr, nc
        else:
            cnt= (cnt + 1) % 4
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()