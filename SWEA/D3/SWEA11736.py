# 평범한 숫자
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N-1):
        if max(arr[i], arr[i-1], arr[i+1]) != arr[i] and min(arr[i], arr[i-1], arr[i+1]) != arr[i]:
            cnt += 1

    print('#{} {}'.format(tc, cnt))