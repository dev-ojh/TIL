import sys
sys.stdin = open('input.txt')


def make_set(x):
    p[x] = x


def find_set(x):

    while x != p[x]:
        x = p[x]
    return x


def union(x, y):

    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = [0] * (N + 1)
    for i in range(1, N+1):
        make_set(i)
    for _ in range(M):
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
        union(a, b)
    cnt = set()
    for i in range(1, N+1):
        cnt.add(find_set(i))
    print('#{} {}'.format(tc, len(cnt)))