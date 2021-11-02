# 두 전구
T = int(input())
for tc in range(1, T + 1):
    A, B, C, D = map(int, (input().split()))
    result = min(B, D) - max(A, C) if min(B, D) - max(A, C) > 0 else 0
    print('#{} {}'.format(tc, result))
