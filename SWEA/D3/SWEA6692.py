# 월급상자
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sum_result = 0.0
    for _ in range(N):
        p, x = map(float, input().split())
        sum_result += p * x
    print('#{} {}'.format(tc, sum_result))