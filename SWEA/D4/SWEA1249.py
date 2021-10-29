#보급로

    
T = int(input())


    
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 100000
    visited = [[0]*N for _ in range(N)]
    bfs(0, 0, 0)
    print('#{} {}'.format(tc, result))
    def bfs(r, c, val):
        global result
        Q = []
        Q.append((r, c, val))
        while Q:
            tmp_r, tmp_c, tmp_val = Q.pop(0) 
            if tmp_r == tmp_c == N-1:
                if result> tmp_val:
                    result = tmp_val
                    
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N and tmp_val + arr[nr][nc] < result:
                    Q.append((tmp_r, tmp_c, tmp_val + arr[nr][nc])
        
