#광이삼의 암벽등반

def dfs(r, c, move, cnt):
    global result
    visited[r][c] = 1
    if r == 0 and c == N-1:
        if result > cnt:
            result = cnt
            return
    if cnt >= result:
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N and not visited[nr][nc] and move > 0:
            if arr[nr][nc] == 1 and move == 1:
                dfs(nr, nc, L, cnt+1)
                visited[nr][nc] = 0
            elif arr[nr][nc] == 1:
                dfs(nr, nc, move-1, cnt)
                visited[nr][nc] = 0
            else:
                dfs(nr, nc, move-1, cnt)
                visited[nr][nc] = 0
    visited[r][c] = 0


T = int(input())
for tc in range(T):
    M, N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    result = 10
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    dfs(M-1, 0, L, 0)
    if result == 10:
        result = -1
    print(result)