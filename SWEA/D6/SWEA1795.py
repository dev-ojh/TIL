import sys
sys.stdin = open('input.txt')


def dijkstra():
    for _ in range(N):
        min_idx = -1
        min_value = 987654321
        for i in range(N+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1
        for j in range(N+1):
            if not visited[j] and dist[j] > dist[min_idx] + G[min_idx][j]:
                dist[j] = dist[min_idx] + G[min_idx][j]
    return dist[N]


def dijkstra2():
    for _ in range(N):
        min_idx = -1
        min_value = 987654321
        for i in range(N+1):
            if not visited[i] and min_value > rest[i]:
                min_idx = i
                min_value = rest[i]
        visited[min_idx] = 1
        for j in range(N+1):
            if not visited[j] and rest[j] > rest[min_idx] + G[j][min_idx]:
                rest[j] = rest[min_idx] + G[j][min_idx]
    return rest[N]
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    G = [[987654321 for _ in range(N+1)] for _ in range(N+1)]
    dist = [987654321] * (N+1)
    rest = [987654321] * (N+1)
    dist[X] = 0
    rest[X] = 0
    visited = [0] * (N+1)

    for _ in range(M):
        start, end, w = map(int, input().split())
        G[start][end] = w
    dijkstra()
    visited = [0] * (N + 1)
    dijkstra2()
    for i in range(1, N+1):
        dist[i] += rest[i]
    print('#{} {}'.format(tc, max(dist[1:])))