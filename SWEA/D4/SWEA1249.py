# 보급로
import sys
sys.stdin = open('input.txt')

def bfs(r, c, val):
    global result
    Q = []
    Q.append((r, c, val))
    while Q:
        tmp_r, tmp_c, tmp_val = Q.pop(0)
        for k in range(4):
            nr = tmp_r + dr[k]
            nc = tmp_c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and tmp_val + arr[nr][nc] < visited[nr][nc]:
                visited[nr][nc] = tmp_val + arr[nr][nc]
                Q.append((nr, nc, tmp_val + arr[nr][nc]))
    return
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 100000
    visited = [[987654321] * N for _ in range(N)]
    bfs(0, 0, 0)
    result = visited[N-1][N-1]
    print('#{} {}'.format(tc, result))


