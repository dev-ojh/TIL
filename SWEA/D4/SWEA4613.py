T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    color = [[0]*3 for _ in range(N)]
    min_cnt = N*M
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                color[i][0] += 1
            elif arr[i][j] == 'B':
                color[i][1] += 1
            else:
                color[i][2] += 1
    
    for i in range(0, N-2):
        for j in range(N-2-i, 0, -1):
            k = N-2-(i+j)
            a, b = i, j
            cnt = 0
            cnt += color[0][1] + color[0][2]
            cnt += color[-1][0] + color[-1][1]
            while a:
                cnt += color[a][1]+color[a][2]
                a -= 1
                
            while b:
                cnt += color[b][0] + color[b][2]
                b -= 1
            while k:
                cnt += color[k][0] + color[k][1]
                k -= 1
            if cnt < min_cnt:
                min_cnt = cnt
            

                