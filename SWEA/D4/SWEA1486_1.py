import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    n = len(height)
    result = 200000
    for i in range(1 << n):
        tmp = []
        for j in range(n):
            if i & (1 << j):
                tmp.append(height[j])
        if sum(tmp) >= B and sum(tmp) - B < result:
            result = sum(tmp) - B
    print('#{} {}'.format(tc, result))