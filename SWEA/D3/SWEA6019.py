# 기차 사이의 파리
T = int(input())
for tc in range(1, T+1):
    D, A, B, F = map(int, input().split())
    result = D / (A+B) * F
    print('#{} {}'.format(tc, result))