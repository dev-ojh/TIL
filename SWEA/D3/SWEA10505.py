# 소득 불균형
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        if arr[i] <= sum(arr)/N:
            cnt += 1

    print('#{} {}'.format(tc, cnt))